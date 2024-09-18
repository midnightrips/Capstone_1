"""Models for capstone."""

import datetime
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True) 
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    edited_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    games = db.relationship('Game', backref='user', lazy=True)
    surveys = db.relationship('Survey', backref='user', lazy=True)
    favorites = db.relationship('Favorite', backref='user', lazy=True)

    @classmethod
    def register(cls, username, password, email):
        """Register user with hashed password and return user."""
        hashed = bcrypt.generate_password_hash(password)

        hashed_utf8 = hashed.decode('utf8')

        return cls(username=username, password=hashed_utf8, email=email)

    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists and password is correct. Return user if valid; else return False."""

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False


class Game(db.Model):
    """Game."""

    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    played_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    favorited_by = db.relationship('Favorite', backref='game', lazy=True)

class Survey(db.Model):
    """Survey."""

    __tablename__ = "surveys"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    before_survey = db.Column(db.Boolean, nullable=False, default=False)
    after_survey = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Favorite(db.Model):
    """Favorite."""

    __tablename__ = "favorites"

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), primary_key=True, nullable=False)



def connect_db(app):
    db.app = app
    db.init_app(app)