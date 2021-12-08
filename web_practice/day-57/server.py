from flask import Flask, render_template
from random import randint
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    random_number = randint(1, 10)
    temp = datetime.now()
    year = temp.strftime("%Y")
    name = "Nikita B."
    return render_template("index.html", num=random_number, year=year, name=name)


if __name__ == '__main__':
    app.run(debug=True)