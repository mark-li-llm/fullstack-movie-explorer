import os
import random
import requests

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from dotenv import load_dotenv

from models import db, User, Review
from auth import auth_bp, login_manager, LoginUser
from config import Config

load_dotenv()

# --------------- Flask App Initialization ---------------
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)
app.register_blueprint(auth_bp, url_prefix='/auth')

login_manager.login_view = 'auth_bp.login'

FAVORITE_MOVIE_IDS = [238, 316029, 2501, 550, 680]  


# --------------- Routes ---------------
@app.route("/")
@login_required
def index():
    """
    Homepage: Randomly select a movie, display its information, show existing reviews and ratings,
    and provide a form for submitting new reviews and ratings.
    """
    movie_id = random.choice(FAVORITE_MOVIE_IDS)
    movie_data = get_movie_data(movie_id)
    if not movie_data:
        return "<h1>Movie data unavailable. Try again later.</h1>"

    title = movie_data.get("title", "Unknown Title")
    tagline = movie_data.get("tagline", "")
    genres = [g["name"] for g in movie_data.get("genres", [])]
    poster_path = movie_data.get("poster_path")
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
    wiki_url = search_wikipedia(title)

    existing_reviews = Review.query.filter_by(movie_id=movie_id).all()

    return render_template(
        "index.html",
        title=title,
        tagline=tagline,
        genres=genres,
        poster_url=poster_url,
        wiki_url=wiki_url,
        movie_id=movie_id,
        reviews=existing_reviews
    )


@app.route("/rate_comment", methods=["POST"])
@login_required
def rate_comment():
    """Process user-submitted rating and comment, and save them in the database."""
    movie_id = request.form.get("movie_id")
    rating = request.form.get("rating")
    comment = request.form.get("comment")

    if not movie_id:
        flash("Invalid movie ID", "error")
        return redirect(url_for("index"))

    new_review = Review(
        user_id=current_user.id,
        movie_id=int(movie_id),
        rating=int(rating) if rating else None,
        comment=comment
    )
    db.session.add(new_review)
    db.session.commit()
    flash("Review/Rating submitted!", "success")

    return redirect(url_for("index"))


def get_movie_data(movie_id: int):
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        print("TMDB_API_KEY not set in environment.")
        return None

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    try:
        response = requests.get(url, params={"api_key": api_key})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching TMDB data:", e)
        return None

def search_wikipedia(title: str):
    params = {
        "action": "opensearch",
        "search": title,
        "limit": 1,
        "namespace": 0,
        "format": "json"
    }
    try:
        response = requests.get("https://en.wikipedia.org/w/api.php", params=params)
        response.raise_for_status()
        data = response.json()
        return data[3][0] if data[3] else None
    except Exception as e:
        print("Error fetching Wikipedia data:", e)
        return None


# --------------- Startup ---------------
if __name__ == '__main__':
    # When testing locally, create the database tables for the first time
    # with app.app_context():
    #    db.create_all()
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
