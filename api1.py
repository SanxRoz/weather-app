import unittest
from unittest.mock import patch
from flask import Flask
from backend import app

class TestWeatherAPIIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('backend.requests.get')
    def test_weather_handler_success(self, mock_get):
        # Mock the responses for the two API calls
        mock_get.side_effect = [
            # Mocking response for get_weather_data
            unittest.mock.Mock(json=lambda: [{'name': 'City', 'lat': 123, 'lon': 456}]),
            # Mocking response for get_weather_data_based_city
            unittest.mock.Mock(json=lambda: {'name': 'City', 'temperature': 25})
        ]

        # Send a POST request to the weather_handler
        response = self.app.post('/api/weather', json={'cityName': 'City'})

        # Assertions
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'City')
        self.assertIn('temperature', data)

if __name__ == '__main__':
    unittest.main()
