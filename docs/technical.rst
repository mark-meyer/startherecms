Technical documentation
***********************

So you're interested in knowing what's going on under the hood. Good for you! At its core StartHereCMS is a Django
application that uses `Wagtail <https://www.wagtail.com>`_ to manage the CMS and admin interface.

-----------------
Upgrading Wagtail
-----------------

Let’s say you really want to update Wagtail from version 1.12 to 1.12.1

* Upgrade the line in the project’s requirements.txt file: wagtail==1.12.1
* Run ``pip install -r requirements.txt`` from the root directory
* Run ``python manage.py makemigrations`` and ``python manage.py migrate``
* Commit the new migration file and push it up to heroku
* Run ``heroku run python manage.py migrate``
