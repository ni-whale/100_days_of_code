import requests

LINK = "https://rozetka.com.ua/samsung_sm_r180nzwasek/p238811953/"

headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Encoding': 'gzip, deflate',
}


response = requests.get(LINK, headers=headers)

response.raise_for_status()

print(response.text)
