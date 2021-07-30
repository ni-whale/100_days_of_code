import smtplib
import datetime as dt
import random
import credentials

# --------------------------- CREDENTIALS --------------------------- #
my_email = credentials.my_email
my_password = credentials.my_password
recipient = credentials.recipient
app_password = credentials.app_password  # In case if I want use yahoo as primary email

# --------------------------- LOGIC --------------------------- #
with open("quotes.txt", "r") as data_file:
    list_of_quotes = data_file.readlines()


current_datetime = dt.datetime.now()
random_quote = random.choice(list_of_quotes)

if current_datetime.weekday() == 4:  # counts from Monday
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"Subject:Motivational quote of the day\n\n{random_quote}"
        )















