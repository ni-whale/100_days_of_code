import datetime
import requests

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

name = ''
gender = ''
age = ''

@app.route('/')
def home():

    return render_template('index.html', name=name, gender=gender, age=age)

@app.route('/guess/<username>')
def name_info(username):
    response_age = requests.get(f'https://api.agify.io?name={username}')
    response_gender = requests.get(f'https://api.genderize.io?name={username}')
    name = username.capitalize()
    age = response_age.json()['age']
    gender = response_gender.json()['gender']

    return render_template('index.html', name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/b077e3e0258a556214d2"
    responce = requests.get(blog_url)
    all_posts = responce.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)