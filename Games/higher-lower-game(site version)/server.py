import random
from flask import Flask

app = Flask(__name__)

secret_number = random.randint(0, 9)
print(secret_number)

@app.route('/')
def title():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src=https://media.giphy.com/media/dwLk9Qb116F3y/giphy.gif>'


@app.route('/<int:number>')
def random_number_guess(number):
    if number == secret_number:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src=https://media.giphy.com/media/NohOlMRtBiGcg/giphy.gif>'
    elif number < secret_number:
        return '<h1 style="color: red">Too low, try again!</h1>' \
               '<img src=https://media.giphy.com/media/1xONIE9kieqf4VTX50/giphy.gif>'
    elif number > secret_number:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '<img src=https://media.giphy.com/media/oDK8A6xUNjD2M/giphy.gif>'


if __name__ == "__main__":
    app.run(debug=True)
