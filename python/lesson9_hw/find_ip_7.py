"""Module with function that finds ip_v4 address"""
import re


def extract_ipv4_addresses(text: str) -> list:
    """Function to extract all IPv4 addresses from a given text"""
    pattern = r"\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b"

    result = re.findall(pattern, text)
    output_list = []
    for ip_addr in result:
        if all(0 <= int(octet) <= 255 for octet in ip_addr):
            output_list.append(".".join(ip_addr))
    return output_list


if __name__ == "__main__":
    TEXT = """
    Valid IPs:
    192.168.1.1
    8.8.8.8
    255.255.255.255
    0.0.0.0
    
    Invalid IPs:
    256.256.256.256
    192.168.300.1
    192.168.1
    192.168.1.999
    some text
    2344532.1234234.1234.1
    """

    print(extract_ipv4_addresses(TEXT))
