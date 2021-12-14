import requests


class Post:
    def __init__(self):
        blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
        self.response = requests.get(blog_url)


    def get_posts(self):
        all_posts = self.response.json()
        return all_posts
