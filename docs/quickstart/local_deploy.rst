=======================
Running the app locally
=======================

Are you a developer interested in running this locally to make code changes or templates? Set-up is super simple.
It assumes a working knowledge of Github and Python 3+ installed.

1. Clone or fork the `github repository <https://github.com/adrind/startherecms>`_.
2. Create a .env file in the root of your project with all the :ref:`config variables you want <config_vars>`. Here's what a basic .env should look like::

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

Create a template
'''''''''''''''''

