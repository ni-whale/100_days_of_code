from flask import Flask, render_template
from post import Post

app = Flask(__name__)
blog_data = Post()
posts = blog_data.get_blogposts()  # we got all posts from API and now will pass them to UI


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<post_id>')
def get_post(post_id):
    for post in posts:
        if str(post["id"]) == post_id:
            chosen_post = post
    return render_template("post.html", post=chosen_post)

if __name__ == "__main__":
    app.run(debug=True)
