import requests
import datetime as dt

MY_LAT = 47.220852
MY_LNG = 35.693699

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]  # taking only hour from the whole output
# ("2015-05-21T05:05:35+00:00")
sunset = data['results']['sunset'].split('T')[1].split(":")[0]

# print(f"sunrise = {sunrise} / sunset = {sunset}")

print(int(sunset) + 3)  # converting from UTC (standard output time for this API to EEST)

time_now = dt.datetime.now()
print(time_now)
