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

if __name__ == "__main__":
    app.run(debug=True)