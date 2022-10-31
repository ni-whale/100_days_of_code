import requests


class Post:
    def __init__(self):
        self.blog_url = 'https://api.npoint.io/b077e3e0258a556214d2'

    def get_blogposts(self):
        respond = requests.get(self.blog_url)
        posts = respond.json()
        return posts
