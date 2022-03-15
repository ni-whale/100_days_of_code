from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')
TMDB_API = "https://api.themoviedb.org/3/search/movie"
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_BEARER_TOKEN = os.getenv('TMDB_BEARER_TOKEN')


class EditForm(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    title = StringField(label="Movie title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# db.create_all()

def get_match_list(movie_title):
    TMDB_query = {
        'api_key': TMDB_API_KEY,
        'query': movie_title
    }
    response = requests.get(TMDB_API, params=TMDB_query)
    response.raise_for_status()
    movie_list = response.json()
    return movie_list


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    edit_form = EditForm()
    movie_by_id = Movie.query.get(movie_id)
    if request.method == "POST":
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_by_id, form=edit_form)


@app.route("/delete/<movie_id>")
def delete(movie_id):
    movie_by_id = Movie.query.get(movie_id)
    db.session.delete(movie_by_id)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", defaults={'movie_id': None}, methods=['GET', 'POST'])
@app.route('/add/<movie_id>', methods=['GET', 'POST'])
def add(movie_id):
    add_form = AddForm()
    if request.method == "POST":
        if movie_id is not None:
            print(movie_id)
            return redirect(url_for('home'))
        else:
            search_result = get_match_list(add_form.title.data)['results']
            return render_template('select.html', movies=search_result)

    return render_template('add.html', form=add_form)


if __name__ == '__main__':
    app.run(debug=True)
