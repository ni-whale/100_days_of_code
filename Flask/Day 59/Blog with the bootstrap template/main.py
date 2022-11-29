from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_data = requests.get('https://api.npoint.io/dc89399832f0790a3177').json()

@app.route('/')
def home():
    return render_template('index.html', posts=blog_data)

@app.route('/post/<post_id>')
def get_post(post_id):
    for post in blog_data:
        if str(post["id"]) == post_id:
            chosen_post = post
    return render_template("post.html", post=chosen_post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)