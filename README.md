# Start Here CMS #

A flexible [Wagtail](https://wagtail.io/) app to make it easy to build simple guides.
Developed after research from the [Anchorage Code for America](https://cfa-muni.tumblr.com) fellowship team.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?env[DJANGO_SETTINGS_MODULE]=startherecms.settings.production&env[SECRET_KEY]=I_AM_A_DUMMY_KEY_CHANGE_ME)


## Requirements ##
1. A [Heroku](https://heroku.com) account to host the website
2. An AWS Storage bucket to hold images and documents


## Optional features ##
1. An [Algolia](https://algolia.com) account to power a search box (Free!)
2. Google Analytics to track what pages your user goes to (Free!)
3. Google Maps API Key to let a user easily pick locations using the [Wagtail Geo Widget](https://github.com/Frojd/wagtail-geo-widget)


## Quickstart ##

First sign up for any or all of the above services

Add an .env file with

Next clone the repository:

    git clone https://github.com/adrind/startherecms.git

cd to your project and install the dependencies:

    pip install -r requirements.txt

Create the migrations for the project:

    python manage.py makemigrations

Apply the migrations:

    python manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver

## How to use it ##

This CMS is designed to be as simple and reusable as possible.

### Track ###
A track has a singular focus that might require multiple steps to complete.
Example: a task list for "Identification" that outlines steps to getting IDs for I-9 eligibility

### Step ###
Steps pages are the "leaves" of this Wagtail app tree -- each task list has multiple steps with information.
Example: a step page for how to obtain your Birth certificate