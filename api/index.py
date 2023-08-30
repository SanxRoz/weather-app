from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "089a2f082671bfc9dc481b9a22a06340"

@app.route('/api/weather', methods=['POST'])
def weather_handler():
    if request.method == 'POST':
        data = request.get_json()
        city_name = data.get('cityName')

        try:
            weather_data = get_weather_data(city_name, 1, API_KEY)
            weather_data_city = get_weather_data_based_city(weather_data[0]['lat'], weather_data[0]['lon'], API_KEY)
            weather_data_city["name"] = weather_data[0]["name"]
            return jsonify(weather_data_city), 200
        except Exception as e:
            return jsonify({"message": str(e)}), 500
    else:
        return '', 405  # Method Not Allowed

def get_weather_data(city_name, limit, api_key):
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city_name,
        "limit": limit,
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()

def get_weather_data_based_city(latitude, longitude, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()