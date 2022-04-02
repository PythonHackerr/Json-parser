import unittest
from unittest.mock import patch
import json_parser


class TestRequests(unittest.TestCase):
    def setUp(self):
        self.url = "https://granny-crud.herokuapp.com/apis/getrecommendations/2"

    def test_invalid_dish(self):
        with self.assertRaises(KeyError):
            json_parser.get_recepie("Cookies")

    def test_invalid_dish(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value.ok = True
            mock_request.return_value.text = 'Success'
            data = json_parser.get_recepie("Waffles")
            mock_request.assert_called_with(
                "https://granny-crud.herokuapp.com/apis/getrecommendations/3")

    def test_if_url_found(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            self.assertTrue(json_parser.url_exists(self.url))

    def test_if_url_not_found(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 404
            self.assertFalse(json_parser.url_exists(self.url))


if __name__ == '__main__':
    unittest.main()
