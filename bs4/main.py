from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
articles_texts = []
articles_links = []

for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

for i in range(len(articles)):
    print(f"{articles_texts[i]} - {articles_links[i]}, Score: {article_upvotes[i]}")
