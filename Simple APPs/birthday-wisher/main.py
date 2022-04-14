##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import os
import random
import credentials
import pandas
import smtplib

# --------------------------- CREDENTIALS --------------------------- #
df_birthdays = pandas.read_csv("birthdays.csv")
list_of_birthdays = df_birthdays.to_dict("records")
# print(list_of_birthdays)

my_email = credentials.my_email
my_password = credentials.my_password

# --------------------------- LOGIC --------------------------- #
random_letter = random.choice(os.listdir("letter_templates"))  # picking up a random letter from the project directory
with open(f"letter_templates/{random_letter}", "r") as data_file:
    letter = data_file.readlines()
    letter = ''.join(letter)

current_date = dt.datetime.now()
for record in list_of_birthdays:
    if record["month"] == current_date.month and record["day"] == current_date.day:
        personalised_letter = letter.replace('[NAME]', record['name'])
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=record['email'],
                msg=f"Subject:Happy Birthday!\n\n{personalised_letter}"
            )












