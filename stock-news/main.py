import requests
import os
from dotenv import load_dotenv

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

API_KEY = os.getenv('STOCK_API_KEY')
stocl_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': API_KEY
}

response = requests.get('https://www.alphavantage.co/query', params=stocl_parameters)
response.raise_for_status()
stock_data = response.json()
print(stock_data)
last_two_days = list(stock_data['Time Series (Daily)'])[:2]
for i in range(0, 2):
    for record in stock_data['Time Series (Daily)'][last_two_days[i]]['4. close']:
        print(record)


# print(list(stock_data['Time Series (Daily)'])[-1])



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

