from bs4 import BeautifulSoup

with open("website.html", "r") as data_file:
    contents = data_file.read()

print(contents)