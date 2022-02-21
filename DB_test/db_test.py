# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# Base = declarative_base()
#
# app = Flask(__name__)
# engine = create_engine('sqlite:///new-books-collection.db', echo=True)
#
#
# class Book(Base):
#     __tablename__ = 'books'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(250), unique=True, nullable=False)
#     author = Column(String(250), nullable=False)
#     rating = Column(Float, nullable=False)
#
#
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # CREATE RECORD
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.5)
# session.add(new_book)
# session.commit()
#
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# db.create_all()
#
# # CREATE RECORD
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()


book = Book.query.filter_by(title="Harry Potter").first()
print(book)

book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()
all_books = db.session.query(Book).all()
print(all_books)