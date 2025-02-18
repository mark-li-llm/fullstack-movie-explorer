# Milestone 2 - Movie Review App

## Deployed Application

https://keen-hangar-450103-i8.ue.r.appspot.com



---

## Requirements

- **Flask**: `3.1.0`
- **Werkzeug**: `3.1.3`
- **Flask-Login**: `0.6.3`
- **Flask-SQLAlchemy**: `3.1.1`
- **SQLAlchemy**: `2.0.38`
- **psycopg2-binary**: `2.9.10`
- **python-dotenv**: `1.0.1`
- **requests**: `2.31.0`
- **gunicorn**: `20.1.0`
---

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-github-username>/milestone2-<your-emory-id>.git
   cd milestone2-<your-emory-id>
   ```

2. **Create Virtual Environment & Install Dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # (On Windows: .\venv\Scripts\activate)
   pip install -r requirements.txt
   ```

3. **Create a `.env` File:**

   In the root directory, create a file named `.env` with the following variables:
   ```bash
   TMDB_API_KEY=your-tmdb-api-key
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://USERNAME:PASSWORD@HOST:PORT/DATABASE
   ```
   **Important:** The application will error if the `.env` file is missing or these values are not provided.

4. **Initialize the Database:**
   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. **Run the App Locally:**
   python app.py
---

