"""Capstone application."""

from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
import os
from models import db, connect_db, User, Game, Survey, Favorite
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

base_URL = "https://www.freetogame.com/api"

app = Flask(__name__)
# Please do not modify the following line on submission
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///capstone-app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "12345"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

app_context = app.app_context()
app_context.push()
connect_db(app)
db.drop_all()
db.create_all()
