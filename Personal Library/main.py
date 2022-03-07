from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy_utils.functions import database_exists

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# db.create_all()
all_books = db.session.query(Book).all()


@app.route('/')
def home():
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form['book_name'],
            author=request.form['book_author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit/<book_id>", methods=['GET', 'POST'])
def edit(book_id):
    book_by_id = Book.query.get(book_id)
    print(book_by_id.rating)
    if request.method == "POST":
        new_rating = request.form['n_rating']
        book_by_id.rating = float(new_rating)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book_by_id)



if __name__ == "__main__":
    app.run(debug=True)
