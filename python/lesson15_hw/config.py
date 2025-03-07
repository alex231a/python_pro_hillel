"""Config parameters for main_requests_version.py"""
from typing import Dict

BASE_URL = "https://ua.korrespondent.net/all/2025/march/4/"
FILE_NAME = "news.csv"
filter_d: Dict[str, str] = {"start_date": "2025-03-01 00:00",
                            "end_date": "2025-03-05 23:59"}
