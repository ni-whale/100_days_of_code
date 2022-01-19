from flask import Flask, render_template, request
import requests
import smtplib
import os


def email_sending(name: str, email: str, phone: str, message: str):
    my_email = os.environ.get('EMAIL')
    my_password = os.environ.get('PASSWORD')
    recipient = os.environ.get('RECIPIENT')

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"Subject:New message from the blog-post site\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}")


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


@app.route("/form-entry", methods=["POST", "GET"])
def receive_data():
    if request.method == 'GET':
        return render_template("contact.html", msg_sent=False)
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        email_sending(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)


if __name__ == "__main__":
    app.run(debug=True)
