# Freelance Platform
Django web application for a freelance marketplace where users can create accounts, publish job/service listings, search and filter listings, and leave comments with ratings.


## Features
* User registration and login
* User profiles
* Create, update and delete job listings
* Job detail pages
* Image upload for listings and user profiles
* Search by title and description
* Filtering by category and tags
* Sorting by date, name and payment
* Comments and ratings
* View counter for job detail pages
* Django Admin customization with Jazzmin


## Tech Stack
* Python
* Django
* SQLite
* Django Templates
* Django Forms
* Django ORM
* Jazzmin
* HTML/CSS
* Git


## Project Structure
text
freelance-platform/
freelance/          # Job listings, categories, tags, comments
users/              # Registration, login, logout, user profiles
templates/          # HTML templates
freelance_project/  # Project settings and main URLs
manage.py
README.md


## Main Apps
### Users
The `users` app is responsible for:
* user registration;
* login and logout;
* profile page;
* user profile model with age and photo.

### Freelance
The freelance app is responsible for:
* job listings;
* categories and tags;
* search and filters;
* comments and ratings;
* job views counter.


## Installation
Clone the repository:
bash
git clone https://github.com/Saikal-03/freelance-platform.git
cd freelance-platform


Create and activate a virtual environment:
bash
python -m venv venv
source venv/bin/activate

Install dependencies:

bash
pip install -r requirements.txt

Apply migrations:
bash
python manage.py migrate

Create a superuser:
bash
python manage.py createsuperuser

Run the project:
bash
python manage.py runserver


## Status
Educational project created while learning Django backend development.
