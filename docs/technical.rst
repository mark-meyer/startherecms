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

-------------------
Creating a template
-------------------

Did you use this CMS in a cool way and have a template you'd like to share with us? Share your work!

First, create a template of your website locally. We suggest filling out the Home page and Tracks but leaving the
Steps to other users since that's the information that tends to change the most.

When you have your local deploy looking the way you want it to, dump the data into a .json file in the fixtures folder.
Name the .json file something that relates to your template

.. code::

    ./manage.py dumpdata --exclude=wagtailcore.GroupCollectionPermission --exclude=auth.User > fixtures/example-template.json

Now that you have your template exported, update the list of templates here and then make a pull request against
this `repo <https://github.com/adrind/startherecms>`_.

Thanks for sharing!