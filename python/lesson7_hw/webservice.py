"""Module with class for work with websites content"""
import requests


class WebService:
    """Class for work with websites content"""

    @staticmethod
    def get_data(url: str) -> dict:
        """Method for getting data from website"""
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            if response.headers.get("Content-Type", "").startswith(
                    "application/json"):
                return response.json()
            return {"error": "Response is not in JSON format."}
        except requests.exceptions.RequestException as err:
            return {"error": str(err)}


if __name__ == "__main__":
    URL_INP = "https://www.google.com"
    content = WebService.get_data(URL_INP)
    print(content)
