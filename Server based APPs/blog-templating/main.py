from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()


@app.route('/')
def home():
    result = post.get_posts()
    print(result)
    return render_template("index.html", posts=result)


@app.route('/post/<post_id>')
def get_blog(post_id):
    for uni_post in post.get_posts():
        if uni_post['id'] == int(post_id):
            return render_template("post.html", post=uni_post)


if __name__ == "__main__":
    app.run(debug=True)
