"""Unit tests for webservice"""

import unittest
from unittest.mock import patch, Mock

from webservice import WebService


class TestWebService(unittest.TestCase):
    """Class to test webservice"""

    @patch("webservice.requests.get")
    def test_get_data_success(self, mock_get):
        """Method to test webservice success"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response
        service = WebService()
        result = service.get_data("https://test.com.ua")
        self.assertEqual(result, {"data": "test"})
        self.assertEqual(mock_get.return_value.status_code, 200)

    @patch("webservice.requests.get")
    def test_get_data_error(self, mock_get):
        """Method for testing webservice error"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"data": "Page not found"}
        mock_get.return_value = mock_response
        service = WebService()

        result = service.get_data("https://test.com.ua")
        self.assertEqual(result, {"data": "Page not found"})
        self.assertEqual(mock_get.return_value.status_code, 404)


if __name__ == '__main__':
    unittest.main()
