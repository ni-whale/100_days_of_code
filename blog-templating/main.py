from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()


@app.route('/')
def home():
    result = post.get_posts()
    return render_template("index.html", posts=result)

@app.route('/post/<post_id>')
def get_blog(post_id):
    result = ...
    for uni_post in post.get_posts():
        if uni_post['id'] == post_id:
            result = uni_post
    print(result)
    return render_template("post.html", post=result)



if __name__ == "__main__":
    app.run(debug=True)
