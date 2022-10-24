import datetime

from flask import Flask, render_template

app = Flask(__name__)

name = ''
gender = ''
age = ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess/<name>')
def name_info():
    ...

if __name__ == "__main__":
    app.run(debug=True)