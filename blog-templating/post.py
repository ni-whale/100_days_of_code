import requests


class Post:
    def __init__(self):
        blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
        response = requests.get(blog_url)
        self.all_posts = response.json()

    def get_posts(self):
        pass
