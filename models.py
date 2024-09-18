"""Models for capstone."""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), primary_key=True, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True) 
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    edited_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)


class Game(db.Model):
    """Game."""

    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    played_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Survey(db.Model):
    """Survey."""

    __tablename__ = "surveys"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)





def connect_db(app):
    db.app = app
    db.init_app(app)