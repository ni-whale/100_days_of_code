import os

import requests
from twilio.rest import Client

API_KEY = os.environ.get('OWN_API_KEY')
ONE_CALL_API = 'https://api.openweathermap.org/data/2.5/onecall'
account_sid = os.environ.get("MY_ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

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

will_be_rain = False

for hour in weather_data['hourly'][:12]:  # Made a slice for the next 12 hours
    if hour['weather'][0]['id'] < 700:  # Everything that less that 700: rain/show/storm and etc.
        will_be_rain = True

if will_be_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="You better to take an umbrella☂️.",
        from_='+13126636183',
        to='+380503224985'
    )
    print(message.sid)

