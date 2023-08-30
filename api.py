import unittest
from unittest.mock import patch, Mock
from backend import app

class TestWeatherAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('backend.requests.get')
    def test_weather_handler(self, mock_get):
        # Mock the response for the get_weather_data function
        mock_response1 = Mock()
        mock_response1.json.return_value = [{
            "lat": 52.5200,
            "lon": 13.4050,
            "name": "Bogota"
        }]
        # Mock the response for the get_weather_data_based_city function
        mock_response2 = Mock()
        mock_response2.json.return_value = {
            "name": "Bogota",
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 25}
        }

        # Set the side_effect to return the mock responses in order
        mock_get.side_effect = [mock_response1, mock_response2]

        response = self.app.post('/api/weather', json={"cityName": "Tokio"})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "Bogota")
        self.assertEqual(data["weather"][0]["description"], "clear sky")
        self.assertEqual(data["main"]["temp"], 25)

if __name__ == '__main__':
    unittest.main()
