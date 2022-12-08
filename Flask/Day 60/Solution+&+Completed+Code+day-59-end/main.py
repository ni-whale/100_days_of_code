from flask import Flask, render_template, request, url_for, redirect
import requests

posts = requests.get("https://api.npoint.io/dc89399832f0790a3177").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form['email']
        phone_number = request.form['phone_number']
        message = request.form['message']
        print(f"{name} | {email} | {phone_number} | {message}")
        return render_template("contact.html")
    return render_template("contact.html", message="False")


if __name__ == "__main__":
    app.run(debug=True)
