from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    record = []
    for book in all_books:
        for value in book.values():
            record.append(value)
    for item in record:
        if record.index(item) == 1:
            item = f" - {item} - "
    print(record)
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        all_books.append(
            {
                "title": request.form['book_name'],
                "author": request.form['book_author'],
                "rating": request.form['rating']
            }
        )
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
