# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)  
    rating = db.Column(db.Integer)   
    comment = db.Column(db.Text)     

    user = db.relationship('User', backref='reviews')

    def __repr__(self):
        return f'<Review movie_id={self.movie_id} user_id={self.user_id} rating={self.rating}>'
