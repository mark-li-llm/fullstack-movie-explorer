# Milestone 3

This project leverages a full-stack architecture combining a Python + Flask backend with a React frontend. It incorporates various libraries and tools to streamline development and ensure code quality.

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** React, Node.js, NPM
- **Other Libraries:** Flask-CORS, Flask-Login, Black (for Python code formatting), ESLint (with Airbnb style guide) for JavaScript

## Setup Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/<your-github-username>/milestone2-<your-emory-id>.git
cd milestone2-<your-emory-id>
```

### 2. Create a Virtual Environment & Install Dependencies

Create a virtual environment and install the required Python packages:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

In the root directory, create a file named `.env` with the following content:

```bash
TMDB_API_KEY=your-tmdb-api-key
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://USERNAME:PASSWORD@HOST:PORT/DATABASE
```

> **Important:** The application requires these environment variables. It will raise errors if the `.env` file is missing or if any of the values are not provided.

### 4. Initialize the Database

Set up the database by running the following commands:

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 5. Run the Application Locally

#### Start the Flask Server

```bash
python app.py
```

#### Set Up and Launch the React Client

Open a new terminal, navigate to the client directory, install dependencies, and start the development server:

```bash
cd client
npm install
npm start
```

---
