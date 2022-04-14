import requests
import datetime as dt
import credentials
import smtplib

# --------------------------- CONST --------------------------- #
MY_LAT = 47.220852
MY_LNG = 35.693699
my_email = credentials.my_email
my_password = credentials.my_password
recipient = credentials.recipient
# --------------------------- DATA COLLECTING --------------------------- #
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(":")[0])  # taking only hour from the whole output
# ("2015-05-21T05:05:35+00:00")
sunset = int(data['results']['sunset'].split('T')[1].split(":")[0])

# --------------------------- LOGIC --------------------------- #
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds

print("-------- Reference info --------")
print(f"ISS - lat: {iss_latitude}, lng: {iss_longitude}\nsunrise = {sunrise + 3} / sunset = {sunset + 3}")  #
# converting from UTC (standard output time for this API) to EEST
print("------------- END --------------")

time_now = dt.datetime.now()
if time_now.hour > sunset:  # Checking if it's dark already
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LNG - 5 < iss_longitude < MY_LNG + 5:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient,
                msg=f"Subject:ISS is coming!\n\nLook up!"
            )
    else:
        print("Seems that ISS far away from your location. Try again later.")
else:
    print("Seems that it's still day in your town, come back after sunset.")


