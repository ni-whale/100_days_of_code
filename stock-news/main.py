import requests
import os
from dotenv import load_dotenv
import datetime as DT
from twilio.rest import Client

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

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
# print(stock_data)

last_two_days = list(stock_data['Time Series (Daily)'])[:2]  # Made a slice to get dates of 2 last days of trading
closure_positions = []
for day in last_two_days:
    closure_positions.append(float(stock_data['Time Series (Daily)'][day]['4. close']))

previous_day = closure_positions[0]
day_before_previous = closure_positions[1]
difference_in_cost = (previous_day-day_before_previous) / previous_day * 100  # calculating the difference in %
# between 2 days
headline_printout = ""
if difference_in_cost < 0:
    headline_printout = f"{STOCK}: 🔻{round(abs(difference_in_cost), 2)}%"
elif difference_in_cost > 0:
    headline_printout = f"{STOCK}: 🔺{round(difference_in_cost, 2)}%"
else:
    headline_printout = "Unknown state:("

if abs(difference_in_cost) >= 5:  # no depends on negativity of the cost
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    today = DT.date.today()
    week_ago = today - DT.timedelta(days=7)  # to get recent articles for the last 7 days
    news_params = {
        'q': COMPANY_NAME,
        'apiKey': NEWS_API_KEY,
        'language': 'en',
        'pageSize': 3,
        'sortBy': 'popularity',
        'from': week_ago
    }
    news_response = requests.get('https://newsapi.org//v2/everything', params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    message_to_send = [headline_printout]
    for article in news_data['articles']:
        article_issue_date = str(article['publishedAt']).split('T')[0]  # using ISO format of the date
        message_to_send.append(f"Title: {article['title']} - {article_issue_date}\nBrief: {article['description']}\n"
                               f"Link: {article['url']}")

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    account_sid = os.getenv("TWILIO_ACC_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{message_to_send[0]}\n{message_to_send[1]}\n{message_to_send[2]}\n{message_to_send[3]}",
        from_='+###',
        to='+###'
    )
    print(message.status)
else:
    print("The fluctuation was not interesting.")