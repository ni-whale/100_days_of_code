from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(1, 10)
    year = datetime.now().year
    name = "Nikita B."
    # return render_template("index.html", num=random_number, year=year, name=name)
    return "Hello, World!"

@app.route('/guess/<name>')
def guess(name):
    age_result = requests.get(f"https://api.agify.io?name={name}").json()['age']
    gender_result = requests.get(f"https://api.genderize.io?name={name}").json()['gender']

    return render_template("index.html", name=name.title(), age=age_result, gender=gender_result)

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
