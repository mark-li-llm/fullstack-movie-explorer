# Milestone 2 - Movie Review App

## Deployed Application

https://keen-hangar-450103-i8.ue.r.appspot.com



---

## Requirements

- Python 3.7+
- PostgreSQL
- Flask==2.2.2
- requests==2.28.1
- python-dotenv==0.20.0
- Flask-Login==0.6.2
- Flask-SQLAlchemy==2.5.1
- psycopg2-binary==2.9.3
- gunicorn==20.1.0
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

