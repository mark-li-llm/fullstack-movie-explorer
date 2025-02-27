import os
import random
import requests

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from dotenv import load_dotenv

from models import db, User, Review
from auth import auth_bp, login_manager, LoginUser
from config import Config
from flask import Flask
from flask_cors import CORS


load_dotenv()


app = Flask(__name__)

CORS(
    app,
    supports_credentials=True,
    resources={r"/api/*": {"origins": "http://localhost:3000"}},
)

app.register_blueprint(auth_bp, url_prefix="/")
# app.register_blueprint(auth_bp, url_prefix="/api")
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)
# app.register_blueprint(auth_bp, url_prefix="/auth")

login_manager.login_view = "auth_bp.login"

FAVORITE_MOVIE_IDS = [238, 316029, 2501, 550, 680]


# --------------- Routes ---------------
@app.route("/")
@login_required
def index():
    movie_id = random.choice(FAVORITE_MOVIE_IDS)
    movie_data = get_movie_data(movie_id)
    if not movie_data:
        return "<h1>Movie data unavailable. Try again later.</h1>"

    title = movie_data.get("title", "Unknown Title")
    tagline = movie_data.get("tagline", "")
    genres = [g["name"] for g in movie_data.get("genres", [])]
    poster_path = movie_data.get("poster_path")
    poster_url = (
        f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
    )
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
        reviews=existing_reviews,
    )


from flask import jsonify


@app.route("/api/random_movie", methods=["GET"])
@login_required
def get_random_movie_api():
    movie_id = random.choice(FAVORITE_MOVIE_IDS)
    movie_data = get_movie_data(movie_id)
    if not movie_data:
        return jsonify({"error": "Movie data unavailable. Try again later."}), 500

    title = movie_data.get("title", "Unknown Title")
    tagline = movie_data.get("tagline", "")
    genres = [g["name"] for g in movie_data.get("genres", [])]
    poster_path = movie_data.get("poster_path")
    poster_url = (
        f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
    )
    wiki_url = search_wikipedia(title)

    existing_reviews = Review.query.filter_by(movie_id=movie_id).all()
    reviews_list = []
    for r in existing_reviews:
        reviews_list.append(
            {
                "id": r.id,
                "user_id": r.user_id,
                "movie_id": r.movie_id,
                "rating": r.rating,
                "comment": r.comment,
            }
        )

    return (
        jsonify(
            {
                "title": title,
                "tagline": tagline,
                "genres": genres,
                "poster_url": poster_url,
                "wiki_url": wiki_url,
                "movie_id": movie_id,
                "reviews": reviews_list,
            }
        ),
        200,
    )


@app.route("/api/rate_comment", methods=["POST"])
@login_required
def rate_comment_api():
    """Process user-submitted rating and comment, and save them in the database."""
    data = request.json
    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    movie_id = data.get("movie_id")
    rating = data.get("rating")
    comment = data.get("comment")

    if not movie_id:
        return jsonify({"error": "Invalid movie_id"}), 400

    new_review = Review(
        user_id=current_user.id,
        movie_id=int(movie_id),
        rating=int(rating) if rating else None,
        comment=comment,
    )
    db.session.add(new_review)
    db.session.commit()

    return jsonify({"message": "Review/Rating submitted!"}), 200


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
        "format": "json",
    }
    try:
        response = requests.get("https://en.wikipedia.org/w/api.php", params=params)
        response.raise_for_status()
        data = response.json()
        return data[3][0] if data[3] else None
    except Exception as e:
        print("Error fetching Wikipedia data:", e)
        return None


from flask import jsonify


@app.route("/api/comments", methods=["GET"])
@login_required
def get_comments_api():

    user_reviews = Review.query.filter_by(user_id=current_user.id).all()
    result = []
    for r in user_reviews:
        result.append(
            {
                "id": r.id,
                "movie_id": r.movie_id,
                "rating": r.rating,
                "comment": r.comment or "",
            }
        )
    return jsonify({"comments": result}), 200


@app.route("/api/comments", methods=["POST"])
@login_required
def save_comments_api():

    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    new_comments = data.get("comments", [])
    old_reviews = Review.query.filter_by(user_id=current_user.id).all()
    for rev in old_reviews:
        db.session.delete(rev)
    db.session.commit()

    for c in new_comments:
        new_rev = Review(
            user_id=current_user.id,
            movie_id=c.get("movie_id", 0),
            rating=c.get("rating", 0),
            comment=c.get("comment", ""),
        )
        db.session.add(new_rev)

    db.session.commit()
    return jsonify({"message": "Comments updated successfully"}), 200


# --------------- Startup ---------------
if __name__ == "__main__":
    # When testing locally, create the database tables for the first time
    # with app.app_context():
    #    db.create_all()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# if __name__ == "__main__":
#     app.run(debug=True)
