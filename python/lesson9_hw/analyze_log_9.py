"""Module with program that parse log file and shows statistics"""

from typing import Dict
from find_ip_7 import extract_ipv4_addresses


class AnalyzeLog:
    """Class that analyzes logs"""

    def __init__(self, log_path: str):
        self.log_path = log_path

    def read_log(self) -> str:
        """Method reads logs"""
        with open(self.log_path, 'r', encoding='utf-8') as file:
            return file.read()

    def get_ip_addr_list(self) -> list:
        """Method extracts ip-addresses from text"""
        text = self.read_log()
        return extract_ipv4_addresses(text)

    def get_ip_statistic(self) -> dict:
        """Creates dictionary with statistics"""
        ip_list = self.get_ip_addr_list()
        statistic_dict: Dict[str, int] = {}
        for ip_addr in ip_list:
            statistic_dict[ip_addr] = statistic_dict.get(ip_addr, 0) + 1
        return statistic_dict


if __name__ == "__main__":
    analyzer = AnalyzeLog('webserver.log')
    stat_dict = analyzer.get_ip_statistic()
    for key, value in stat_dict.items():
        print(f"{key} ---> {value}")
