import os
import random
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

FAVORITE_MOVIE_IDS = [238, 316029, 2501]

@app.route("/")
def index():
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

    return render_template(
        "index.html",
        title=title,
        tagline=tagline,
        genres=genres,
        poster_url=poster_url,
        wiki_url=wiki_url
    )

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

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)