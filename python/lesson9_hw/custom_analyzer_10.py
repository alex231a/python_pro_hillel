"""Custom log parser"""
import re
from typing import Dict, Any


class LogParser:
    """Class for parsing a log string in the specified format"""

    # Pattern for parsing the log line
    pattern = re.compile(
        r'(?P<timestamp>\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}\.\d{3})\s+'  # 
        # Timestamp
        r'(?P<timezone>\w+)\s+'  # Timezone
        r'(?P<thread>[\w-]+\s+\([\w]+\))\s+'  # Thread
        r'(?P<log_level>\w+):\s+'  # Log level
        r'\[(?P<event_type>\w+)]\s+'  # Event type in square brackets
        r'(?P<message>[\w\s]+)\s*'  # Message
        r'(?P<key_values>.*)',  # Key-value pairs after the message
        re.DOTALL  # Allows matching multiline messages
    )

    def __init__(self, log_string: str):
        """
        Initializes the parser with the log string to be parsed.

        :param log_string: The log string to be parsed
        """
        self.log_string = log_string

    def parse_log(self) -> Dict[str, Any]:
        """
        Parses the log string and extracts information.

        :return: A dictionary with parsed log data.
        """
        match = self.pattern.match(
            self.log_string)
        if match:
            data = match.groupdict()
            key_value_pairs = dict(
                re.findall(r'(\w+)=([^,]+)', data["key_values"]))

            # Return the parsed data as a dictionary
            return {
                "timestamp": data["timestamp"],
                "timezone": data["timezone"],
                "thread": data["thread"],
                "log_level": data["log_level"],
                "event_type": data["event_type"],
                "message": data["message"],
                "key_values": key_value_pairs
            }
        print("No match found")
        return {}


if __name__ == "__main__":
    LOG_STRING = (
        "05/14/2021 17:45:59.452 EEST SharedThread-worker-thread-9 ("
        "LogNMERule) DEBUG: "
        "[CCR_RCVD] CCR Init received:d_k_defaultQCI=9, "
        "d_k_AoCAddress=Vodafone, "
        "d_k_ioAdapterCount=1, d_k_ioAdapterNamePrefix=Adapter, "
        "d_k_closeSessionOnError=false, "
        "MSISDN=380500000720, d_k_eventType=CCR, d_k_var_I=0, "
        "d_k_var_S=SUCCESS, "
        "d_k_needsLogging=false, d_k_HostName=Test, d_m_cc_Request_Type=1"
    )

    parser = LogParser(LOG_STRING)
    parsed_data = parser.parse_log()

    if parsed_data:
        print("Parsed Log Data:")
        for key, value in parsed_data.items():
            print(f"{key}: {value}")
