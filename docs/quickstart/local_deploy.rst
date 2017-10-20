=======================
Running the app locally
=======================

Are you a developer interested in running this locally to make code changes or templates? Set-up is super simple.
It assumes a working knowledge of Github and Python 3+ installed.

1. Clone or fork the `github repository <https://github.com/adrind/startherecms>`_.
2. Create a .env file in the root of your project with all the :ref:`config variables you want <config_vars>`. Here's what a basic .env should look like::

    DJANGO_SETTINGS_MODULE=startherecms.settings.local
    AWS_ACCESS_KEY_ID=something-something
    AWS_SECRET_ACCESS_KEY=irutsgkjniuref
    AWS_STORAGE_BUCKET_NAME=your-bucket-name


3. In the root of the project run::

    pip install -r requirements.txt
4. Create the database migrations for the project::

    python manage.py makemigrations
5. Apply the migrations::

    python manage.py migrate
6. Finally, run the server::

    python manage.py runserver


.. _create_template:

Create a template
'''''''''''''''''

Did you use this CMS in a cool way and have a template you'd like to share with us? Share your work!

First, create an exact template of your website locally. We suggest filling out the :doc:`Home page <../wagtail/home_page>` and :doc:`Tracks <../wagtail/track_page>` but leaving the
:doc:`Steps <../wagtail/step_page>` for other users to fill out since that's the information that tends to change the most.

When you have your local deploy looking the way you want it to, dump the data into a .json file in the fixtures folder.
Name the .json file something that relates to your template. For example:

.. code::

    ./manage.py dumpdata --exclude=wagtailcore.GroupCollectionPermission --exclude=auth.User > fixtures/example-template.json

Also update the Procfile with a command users can use to apply the fixture. It needs a name (example-template) followed
by a loaddata command that loads the fixture you just created. Here's an example for example-template.json:

.. code::

    example-template: python manage.py loaddata fixtures/example-template.json

Now that you have your template exported, update the list of templates :doc:`in the documentation <templates>` and then make a pull request against
this `repo <https://github.com/adrind/startherecms>`_.

Thanks for sharing!
