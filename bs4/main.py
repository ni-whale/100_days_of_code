from bs4 import BeautifulSoup
import requests

# response = requests.get("https://news.ycombinator.com/")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# articles = soup.find_all(name="a", class_="storylink")
# articles_texts = []
# articles_links = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     articles_texts.append(text)
#     link = article_tag.get("href")
#     articles_links.append(link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# temp1 = 0
# for i in range(len(article_upvotes)):
#     if article_upvotes[i] > temp1:
#         temp1 = article_upvotes[i]
#
# temp = article_upvotes.index(temp1)
# print(f"{articles_texts[temp]} - {articles_links[temp]}, Score: {article_upvotes[temp]}")

from requests_html import HTMLSession

# WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
# WEB_FILE = "100_best_movies.html"
#
#
# # Using requests_html to render JavaScript
# def get_web_page():
#     # create an HTML Session object
#     session = HTMLSession()
#     # Use the object above to connect to needed webpage
#     response = session.get(WEB_PAGE)
#     # Run JavaScript code on webpage
#     response.html.render()
#
#     # Save web page to file
#     with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
#         fp.write(response.html.html)
#
#
# def read_web_file():
#     try:
#         open(WEB_FILE)
#     except FileNotFoundError:
#         get_web_page()
#     finally:
#         # Read the web page from file
#         with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
#             content = fp.read()
#         return BeautifulSoup(content, "html.parser")
#
#
# # Read web file if it exists, load from internet if it doesn't exist
# result = read_web_file()


with open("100_best_movies.html", "r") as web_page:
    soup = BeautifulSoup(web_page, "html.parser")


movies_list_origin = [movie.getText().split(") ") for movie in soup.find_all(name="h3", class_="jsx-4245974604")]

movies_list_origin.reverse()
movie_list = []
for movie in range(len(movies_list_origin)):
    if len(movies_list_origin[movie]) == 2:
        movie_list.append(movies_list_origin[movie][1])
    else:
        movie_list.append(movies_list_origin[movie][0])

i = 0
for movie in movie_list:
    i = i + 1
    if movie == "12: The Godfather Part II":
        print(f"{i}) The Godfather Part II")
    else:
        print(f"{i}) {movie}")


# print("--------------------------")
# print(movies_list_origin)

