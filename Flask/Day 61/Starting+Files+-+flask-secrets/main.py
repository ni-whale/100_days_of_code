from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(max=30)])
    password = StringField('Password', [validators.Length(max=30)])


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        return f"<h1>email={form.email.data}, password={form.password.data}</h1>"
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)