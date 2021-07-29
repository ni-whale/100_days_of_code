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
list_of_quotes = []
temp = []
with open("quotes.txt", "r") as data_file:
    temp.append(data_file.readlines())
list_of_quotes = [quote for quote in temp]
current_datetime = dt.datetime.now()

# if current_datetime.weekday() == 3:  # counts from Monday
#     with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=recipient,
#             msg=f"Subject:Motivational quote of the day\n\n{random_quote}"
#         )

random_quote = list_of_quotes.index(random.randint(0, 102))

# print(list_of_quotes)
# print(len(list_of_quotes))














