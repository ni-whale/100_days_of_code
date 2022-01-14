from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = 'https://api.npoint.io/5c68d12ead0fe6b758e2'
response = requests.get(blog_url)
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<post_id>')
def get_blog(post_id):
    for uni_post in all_posts:
        if uni_post['id'] == int(post_id):
            return render_template("post.html", post=uni_post)


if __name__ == "__main__":
    app.run(debug=True)