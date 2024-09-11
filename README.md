# Capstone 1: PROJECT PROPOSAL

Tech Stack:
I will use Python/Flask for my project.

Focus:
My project will have a back-end focus, although there will be a functional front-end.

Project Type:
This will be a website that provides a platform for mental health research through gaming, with the potential to evolve into a mental health-focused video game platform.

Project Goal:
The goal is to create an app that serves as usable research to promote mental health awareness. The app will collect and analyze data on users’ experiences before and after playing specific games, aiming to improve mental health through tailored recommendations.

Target Users:
The app will primarily target teens and young adults, though it will be accessible to people of all ages interested in improving mental health through gaming.

Data Collection:
I will use data from the FreeToGame API (https://www.freetogame.com/api-doc) to access a variety of free games. Additionally, I will create my own API to collect and store user information and survey data before and after gameplay, tracking mental health indicators.

Database Schema:
The database will contain the following models:
  User: (ID, username, password)
  Game: (ID, name, type, user_id)
  Survey: (ID, before_survey (boolean), after_survey (boolean), user_id)

Potential Issues:
One challenge might be managing game and survey data within the database, especially as the survey data must persist even after user profile deletion. Another issue may be storing game information in a new database as well as storing survey information as there are both before and after surveys.

Security Considerations:
Sensitive information like usernames and passwords must be securely stored so no human-readable identifiers are linked to survey data and users’ passwords aren’t easily found.

Functionality:
The app will allow users to:
  Register/login/logout/delete their account
  Take surveys before and after playing games
  Be matched with games
  View progress based on survey results, with visual representations of overall trends across users.

User Flow:
  User registers or logs in
  User takes a before-survey
  User gets matched with 3 games
  User plays a game
  User takes an after-survey
  User sees a graph of their personal progress and population-wide data

Beyond CRUD Functionality:
The app will generate insights from the data collected, going beyond simple CRUD operations by using survey responses to match games and display user progress.

Stretch Goals:
Data visualization of user progress over time
Further game recommendations based on survey analysis
