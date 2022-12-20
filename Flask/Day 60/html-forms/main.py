from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def recieve_data():
    if request.method == "POST":
        return f"<h1>Name: {request.form['name']}, Password: {request.form['password']}</h1>"


if __name__ == "__main__":
    app.run(debug=True)