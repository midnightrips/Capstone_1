"""Capstone application."""

from flask import Flask, redirect, render_template, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
import os
from models import db, connect_db, User, Game, Survey, Favorite
from forms import AddUserForm, LoginForm, EditUserForm, BeforeSurveyForm, AfterSurveyForm
from sqlalchemy.exc import IntegrityError

base_URL = "https://www.freetogame.com/api"

CURR_USER_KEY = "curr_user"

app = Flask(__name__)
# Please do not modify the following line on submission
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///capstone-app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


app.config['SECRET_KEY'] = "12345"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

app_context = app.app_context()
app_context.push()
connect_db(app)
db.drop_all()
db.create_all()

##############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/register', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = AddUserForm()

    if form.validate_on_submit():
        try:
            user = User.register(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/register.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/register.html', form=form)
    
@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()
    flash("Logged out successfully!")
    return redirect('/login')

#################################################################################
# homepage route

@app.route('/')
def homepage():
    """Show homepage with games to play if user; redirect to registration page if not."""
    
    # add homepage route if user

    if not g.user:
        return render_template("/home-anon.html")

    return render_template('home.html')

####################################################################################
# Survey routes

@app.route('/start', methods=['GET', 'POST'])
def start():
    """Show 'before' survey and handle form submission."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    form = BeforeSurveyForm()

    if form.validate_on_submit():
        info = Survey(text=form.text.data)
        db.session.add(info)
        db.session.commit()

        return redirect(f"/game-choice")

    return render_template('surveys/before-survey.html', form=form)

@app.route('/game-choice', methods=['GET', 'POST'])
def choose_game():
    """Show game choices and handle game choice."""

    # get random list of 3 games from the api
