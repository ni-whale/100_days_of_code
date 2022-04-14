from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_func():
        return f"<b>{function()}</b>"
    return wrapper_func


def make_emhasis(function):
    def wrapper_func():
        return f"<em>{function()}</em>"
    return wrapper_func


def make_underlined(function):
    def wrapper_func():
        return f"<u>{function()}</u>"
    return wrapper_func


@app.route('/')
def hello_world():
    return 'Hello, World!'


# different routs using tbe app.route decorator
@app.route('/bye')
@make_bold
@make_emhasis
@make_underlined
def bye():
    return "Bye!"


# Creating variable path and converting a path to a specific datatype
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you're {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
