"""Module with functions that parse data and save it into file"""
import asyncio
import csv
import logging
import os
import time
from datetime import datetime
from typing import Optional, List, Dict, Any

import aiohttp
from bs4 import BeautifulSoup

from lesson15_hw.analyze_csv_pandas import get_statistics_from_file, \
    analyze_keywords
from lesson15_hw.config import BASE_URL, FILE_NAME, filter_d
from lesson15_hw.date_formatter import format_article_date

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


async def fetch(session: aiohttp.ClientSession, url: str) -> Optional[str]:
    """Function to fetch data from url"""
    try:
        logging.info("Fetching %s", url)
        async with session.get(url, timeout=5) as response:
            if response.status == 200:
                return await response.text()
            logging.error("Error fetching %s, status code: %d", url,
                          response.status)
    except asyncio.TimeoutError:
        logging.error("Timeout error fetching %s", url)
    except aiohttp.ClientError as error:
        logging.error("Error fetching %s: %s", url, error)
    return None


async def get_page(session: aiohttp.ClientSession, url: str) -> Optional[
    BeautifulSoup]:
    """
    Fetches and parses the HTML content from a given URL.

    :param url: The URL of the webpage to fetch.
    :param session: An aiohttp.ClientSession object.
    :return: A BeautifulSoup object if successful, otherwise None.
    """
    response = await fetch(session, url)
    if response:
        return BeautifulSoup(response, "lxml")
    return None


def parse_news(soup, filter_date=None):
    """
    Parses the news articles from the given BeautifulSoup object.

    :param soup: BeautifulSoup object containing the parsed HTML page.
    :param filter_date: Dictionary of filters {"start_date": "2025-03-01
    00:00", "end_date": "2025-03-02 23:59"}.
    :return: A list of dictionaries containing article details (title, link,
    summary, date).
             Returns an empty list if no articles are found.
    """
    result = soup.find_all("div", {"class": "article article_rubric_top"})
    if not result:
        logging.warning("No articles found on the page.")
        return []

    output_list = []
    for item in result:
        article = {"title": None, "link": None, "summary": None, "date": None}

        try:
            article_tag = item.find("div", class_="article__title")
            if article_tag:
                title_link = article_tag.find("a")
                if title_link:
                    article["title"] = title_link.text.strip()
                    article["link"] = title_link.get("href")

            text_tag = item.find("div", class_="article__text")
            if text_tag:
                date_tag = text_tag.find("div", class_="article__date")
                # print(date_tag.text)
                if date_tag:
                    date_value = format_article_date(
                        date_tag.text.strip().split(" - ")[-1])
                    if isinstance(date_value, list):
                        article["date"] = date_value[0] if date_value else None
                    else:
                        article["date"] = date_value
                    # print(article["date"])
                    date_tag.extract()
                article["summary"] = text_tag.get_text(strip=True)
                # print(article["summary"])

            # date_tag = item.find("div", class_="article__date")
            # if date_tag:
            #     date_value = format_article_date(
            #         date_tag.text.strip().split(" - ")[-1])
            #     if isinstance(date_value, list):
            #         article["date"] = date_value[0] if date_value else None
            #     else:
            #         article["date"] = date_value
            #     print(article["date"])

        except AttributeError as error:
            logging.error("Missing field in article: %s", error)
            continue

        if filter_date and article["date"]:
            try:
                date_format = "%Y-%m-%d %H:%M"
                start_date = datetime.strptime(filter_date["start_date"],
                                               date_format)
                end_date = datetime.strptime(filter_date["end_date"],
                                             date_format)
                current_date = datetime.strptime(article["date"], date_format)
                if start_date <= current_date <= end_date:
                    output_list.append(article)
            except (ValueError, TypeError, KeyError) as error:
                logging.error("Error parsing date for article: %s", error)
        else:
            output_list.append(article)

    return output_list


def save_to_csv(input_data: List[dict], file_path) -> None:
    """
    Saves the parsed news data to a CSV file.

    :param input_data: List of dictionaries containing article details.
    :param file_path: Path to the CSV file.
    """
    if not input_data:
        logging.error("No data to write to CSV, change filters")
        return

    existing_titles = set()
    if os.path.exists(file_path):
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                existing_titles = {row["title"] for row in reader}
        except Exception as error:
            logging.error("Error reading existing CSV: %s", error)

    new_data = [item for item in input_data if
                item["title"] not in existing_titles]

    if not new_data:
        logging.info("No new data to add. Skipping write.")
        return

    try:
        write_mode = "a" if os.path.exists(file_path) else "w"
        with open(file_path, mode=write_mode, newline="",
                  encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=input_data[0].keys())

            if write_mode == "w":
                writer.writeheader()

            writer.writerows(new_data)
            logging.info("Added %d new records to %s", len(new_data),
                         file_path)
    except PermissionError:
        logging.error(
            "Error: Permission denied when trying to write to the file.")
    except IOError as error:
        logging.error("IO error occurred while writing to the file: %s", error)


def get_pagination_links(soup: BeautifulSoup) -> List[str]:
    """Extracts all pagination links from the page."""
    return list({str(link.get("href")) for link in
                 soup.select("ul.pagination li.pagination__item a") if
                 isinstance(link.get("href"), str)})


async def scrape_all_pages(start_url: str,
                           filter_date_inp: Optional[Dict[Any, Any]] = None) \
        -> \
                List[Dict[str, Optional[str]]]:
    """Scrapes news from multiple pages."""
    async with aiohttp.ClientSession() as session:
        soup = await get_page(session, start_url)
        if not soup:
            return []

        all_links = get_pagination_links(soup)
        all_links.insert(0, start_url)

        logging.info("Scraping %d pages asynchronously...", len(all_links))

        tasks = [get_page(session, page_url) for page_url in all_links]
        start_time = time.time()
        pages_soup = await asyncio.gather(*tasks)
        end_time = time.time()

        logging.info("All pages scraped in %.2f seconds.",
                     end_time - start_time)

        all_news = []
        for page_soup, page_url in zip(pages_soup, all_links):
            if page_soup:
                logging.info("Parsing page: %s", page_url)
                parsed_news = parse_news(page_soup, filter_date_inp)
                if parsed_news:
                    logging.info("Found %d articles on %s", len(parsed_news),
                                 page_url)
                    all_news.extend(parsed_news)

        logging.info("Total articles collected: %d", len(all_news))
        return all_news


if __name__ == "__main__":
    async def main():
        """Main function"""
        news = await scrape_all_pages(BASE_URL, filter_d)
        save_to_csv(news, FILE_NAME)
        get_statistics_from_file(FILE_NAME)
        analyze_keywords(FILE_NAME, top_n=10)


    asyncio.run(main())
