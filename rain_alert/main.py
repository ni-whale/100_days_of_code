import requests

API_KEY = '61ca6c3f53e8945e36f4b1d0941464e8'
ONE_CALL_API = 'https://api.openweathermap.org/data/2.5/onecall'

weather_params = {
    'lat': 47.8508,
    'lon': 35.1183,
    'units': "metric",
    'exclude': "current,minutely,daily",
    'appid': API_KEY
}

response = requests.get(ONE_CALL_API, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
