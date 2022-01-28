from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import TextField


class SignupForm(FlaskForm):
    login = TextField('email')
    password = TextField('password')

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html', form=SignupForm)


if __name__ == '__main__':
    app.run(debug=True)