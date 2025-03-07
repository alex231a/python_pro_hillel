"""Module with functions that parse data and save it into file"""
import csv
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

import config
from lesson15_hw.analyze_csv_pandas import get_statistics_from_file
from lesson15_hw.date_formatter import format_article_date

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def get_page(url: str) -> Optional[BeautifulSoup]:
    """
    Fetches and parses the HTML content from a given URL.

    :param url: The URL of the webpage to fetch.
    :return: A BeautifulSoup object if successful, otherwise None.
    """
    try:
        logging.info("Fetching %s", url)
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        if not response.text:
            raise ValueError(f"Empty content received from {url}")

        logging.info("Parsing response from %s", url)
        soup = BeautifulSoup(response.text, "lxml")

        if soup is None:
            raise ValueError(f"Failed to parse the content from {url}")

        return soup

    except requests.exceptions.Timeout:
        logging.error("Request to %s timed out.", url)
    except requests.exceptions.TooManyRedirects:
        logging.error("Too many redirects while trying to reach %s.", url)
    except requests.exceptions.RequestException as error:
        logging.error("An error occurred while requesting %s: %s", url, error)
    except (TypeError, ValueError, AttributeError) as error:
        logging.error("Error during parsing with BeautifulSoup for %s: %s",
                      url, error)
    except Exception as error:
        logging.error("An unexpected error occurred: %s", error)

    return None


def parse_news(soup: BeautifulSoup,
               filter_date: Optional[Dict[Any, Any]] = None) -> List[
    Dict[str, Optional[str]]]:
    """
    Parses the news articles from the given BeautifulSoup object.

    :param soup: BeautifulSoup object containing the parsed HTML page.
    :param filter_date: Dictionary of filters {"start_date": "2025-03-01
    00:00", "end_date": "2025-03-02 23:59"}.
    :return: A list of dictionaries containing article details (title, link,
    summary, date).
             Returns None if no articles are found.
    """
    element: str = "div"
    element_attrs: Dict[str, str] = {"class": "article article_rubric_top"}
    result: List[BeautifulSoup] = soup.find_all(name=element,
                                                attrs=element_attrs)

    if not result:
        logging.warning("No articles found on the page.")
        return []

    output_list: List[Dict[str, Optional[str]]] = []

    for item in result:
        article: Dict[str, Optional[str]] = {"title": None, "link": None,
                                             "summary": None, "date": None}

        try:
            article_tag = item.find("div", class_="article__title")
            if article_tag:
                title_link = article_tag.find("a")
                if title_link and isinstance(title_link, Tag):
                    article["title"] = title_link.text.strip()
                    href_value = title_link.get("href")
                    article["link"] = href_value if isinstance(href_value,
                                                               str) else None

            text_tag = item.find("div", class_="article__text")
            if text_tag:
                summary_text = text_tag.get_text(strip=True)
                article["summary"] = summary_text

            date_tag = item.find("div", class_="article__date")
            if date_tag:
                date_text = date_tag.text.strip().split(" - ")[-1]
                if date_text:
                    article["date"] = format_article_date(date_text)

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
                current_date = datetime.strptime(article["date"],
                                                 date_format)
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
    if not input_data or len(input_data) == 0:
        logging.error("No data to write to CSV, change filters")
        return

    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=input_data[0].keys())
            writer.writeheader()
            writer.writerows(input_data)

            logging.info("Data successfully added to %s file", file_path)

    except PermissionError:
        logging.error(
            "Error: Permission denied when trying to write to the file.")

    except IOError as error:
        logging.error(
            "Error: An IO error occurred while writing to the file. "
            "Details: %s", error)

    except Exception as error:
        logging.error("An unexpected error occurred: %s", error)


def get_pagination_links(soup: BeautifulSoup) -> List[str]:
    """Extracts all pagination links from the page."""
    return list({str(link.get("href")) for link in
                 soup.select("ul.pagination li.pagination__item a") if
                 isinstance(link.get("href"), str)})


def scrape_all_pages(start_url: str,
                     filter_date_inp: Optional[Dict[Any, Any]] = None) -> List[
    Dict[str, Optional[str]]]:
    """Scrapes news from multiple pages."""
    soup = get_page(start_url)
    if not soup:
        return []

    all_links = get_pagination_links(soup)
    all_links.insert(0, start_url)

    all_news: List[Dict[str, Optional[str]]] = []
    for page_url in all_links:
        logging.info("Scraping page: %s", page_url)
        page_soup = get_page(page_url)
        if page_soup:
            parsed_news = parse_news(page_soup, filter_date_inp)
            if parsed_news:
                all_news.extend(parsed_news)
    return all_news


if __name__ == "__main__":
    save_to_csv(scrape_all_pages(config.BASE_URL, config.filter_d),
                config.FILE_NAME)
    get_statistics_from_file(config.FILE_NAME)
