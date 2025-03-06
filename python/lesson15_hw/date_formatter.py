"""Module with function that converts Ukrainian news article dates into a
standardized format (YYYY-MM-DD HH:MM)"""
import re
from datetime import datetime, timedelta
from typing import Optional


def format_article_date(article_date: str) -> Optional[str]:
    """
    Converts Ukrainian news article dates into a standardized format (
    YYYY-MM-DD HH:MM).

    Supports the following formats:
    - "10:35" → today's date with time
    - "Вчора, 22:42" → yesterday's date with time
    - "2 березня 2025, 21:59" → converted to "2025-03-02 21:59"

    :param article_date: The raw date string from the article.
    :return: A formatted date string in "YYYY-MM-DD HH:MM" format or None if
    the format is unknown.
    """
    month_map = {
        'січня': 'January',
        'лютого': 'February',
        'березня': 'March',
        'квітня': 'April',
        'травня': 'May',
        'червня': 'June',
        'липня': 'July',
        'серпня': 'August',
        'вересня': 'September',
        'жовтня': 'October',
        'листопада': 'November',
        'грудня': 'December'
    }

    pattern1 = r"\d{2}:\d{2}"
    pattern2 = r"Вчора, \d{2}:\d{2}"
    # pattern3 = r"\d{1,2} [а-яА-ЯёЁіІїЇєЄ]+ \d{4}, \d{2}:\d{2}"
    today = datetime.today()

    if re.match(pattern1, article_date):
        formatted_date = today.strftime('%Y-%m-%d')
        article_date = f"{formatted_date} {article_date}"
    elif re.match(pattern2, article_date):
        yesterday = today - timedelta(days=1)
        formatted_yesterday = yesterday.strftime('%Y-%m-%d')
        art_time = article_date.split(',')[1].strip()
        article_date = f"{formatted_yesterday} {art_time}"
    else:
        for ukr_month, eng_month in month_map.items():
            if ukr_month in article_date:
                article_date = article_date.replace(ukr_month, eng_month)
        date_obj = datetime.strptime(article_date, '%d %B %Y, %H:%M')
        article_date = date_obj.strftime('%Y-%m-%d %H:%M')
    return article_date


if __name__ == '__main__':
    DATE1 = '10:35'
    DATE2 = 'Вчора, 22:42'
    DATE3 = '2 березня 2025, 21:59'
    print(format_article_date(DATE1))
    print(format_article_date(DATE2))
    print(format_article_date(DATE3))
