# Movie Explorer

A Flask web application that randomly displays information about classic movies using TMDB and Wikipedia APIs. The app showcases movie details including title, tagline, genres, and poster image, along with a link to the corresponding Wikipedia page.

## Deployed Application

https://my-flask-service-403405868604.us-central1.run.app

## Features

- Randomly displays information from three classic movies:
- Shows movie title, tagline, and genres
- Provides link to corresponding Wikipedia page
- Error handling with user-friendly messages

## Technologies Used

- **Backend**: Python 3, Flask 2.2.5
- **Frontend**: HTML5, CSS3
- **APIs**: 
  - TMDB API (v3) for movie information
  - MediaWiki Action API for Wikipedia links
- **Additional Libraries**:
  - Werkzeug 2.2.2
  - requests 2.28.1
  - python-dotenv 0.20.0
- **Deployment**: Google Cloud Run

## Local Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Momo23569/project1-yli3466.git
   ```

2. **Set Up Python Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Install Dependencies**
   ```bash
   pip install Flask==2.2.5 Werkzeug==2.2.2 requests==2.28.1 python-dotenv==0.20.0
   ```

4. **Environment Variables**
   Create a `.env` file in the project root with:
   ```
   TMDB_API_KEY=your_tmdb_api_key
   ```

5. **Get TMDB API Key**
   - Create an account on [TMDB](https://www.themoviedb.org/)
   - Go to your account settings
   - Navigate to the API section
   - Generate a new API key

6. **Run the Application**
   ```bash
   python app.py
   ```

## Project Structure

```
├── app.py                 # Main Flask application with API integrations
├── templates/
│   └── index.html        # HTML template with embedded CSS
├── .env                  # Environment variables (not in repo)
├── requirements.txt      # Python dependencies
└── README.md            # Documentation
```

## Code Overview

### Key Components

1. **Flask Application (`app.py`)**
   - Random movie selection from predefined list
   - TMDB API integration for movie details
   - Wikipedia API integration for related links
   - Error handling for API failures

2. **Template (`index.html`)**
   - Responsive layout
   - Card-based design
   - Image hover effects


## Error Handling

- Graceful fallback for missing movie data
- User-friendly error messages
- Default values for missing movie properties
- Error logging for API failures


## Notes

- Keep the `.env` file secure and never commit it
- The movie list can be modified by updating `FAVORITE_MOVIE_IDS` in `app.py`
