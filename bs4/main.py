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

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

temp1 = 0
for i in range(len(article_upvotes)):
    if article_upvotes[i] > temp1:
        temp1 = article_upvotes[i]

temp = article_upvotes.index(temp1)
print(f"{articles_texts[temp]} - {articles_links[temp]}, Score: {article_upvotes[temp]}")
