Quickstart
**********

.. toctree::
    :hidden:

    aws

==========================
How to start a new website
==========================
There are a couple of services you need to sign up for before deploying your website to Heroku:

1. A `Heroku <https://www.heroku.com>`_ account
2. An :doc:`Amazon Web Services <aws>` account

Additionally there are some optional (free!) services you can use for added functionality:

* Google Analytics -- used to track how people use your website
* Google Maps -- used to let you set locations of community organizations on a map
* Algolia -- used to power a search box on your website so people can easily find pages

Once you sign up for these services you need the following keys to launch your application:

.. csv-table:: Required keys to create the website
   :header: "Name of key", "How to find it", "Example value"
   :widths: 15, 30, 10

   "AWS_ACCESS_KEY_ID", :ref:`Find your access key <aws_keys>`, KUDFHGJKHRUFDBF
   "AWS_SECRET_ACCESS_KEY", :ref:`Create your secret key <aws_keys>`, 2IUGFD/8vD9/k7s6
   "AWS_STORAGE_BUCKET_NAME", :ref:`Create your bucket <aws_bucket>`, start-here-dog-files

While not required, these additional services add functionality to the website and we encourage you to sign up:

.. csv-table:: Optional keys for additional services
   :header: "Name of key", "How to find it", "Example value"
   :widths: 15, 30, 10

   "GOOGLE_MAPS_API_KEY", `Get an API key here <https://developers.google.com/maps/documentation/javascript/get-api-key>`_, AIv80f_8tueriogjURGYE
   "GOOGLE_WIDGET_DEFAULT_LAT", `Find your latitude <http://www.worldatlas.com/aatlas/findlatlong.htm>`_ , 37.773972
   "GOOGLE_WIDGET_DEFAULT_LONG", `Find your longitude <http://www.worldatlas.com/aatlas/findlatlong.htm>`_ , -122.431297
   "GOOGLE_WIDGET_DEFAULT_LONG", `Find your longitude <http://www.worldatlas.com/aatlas/findlatlong.htm>`_ , -122.431297




Once you have the above keys ready, you can start! Click the deploy button to create your project in Heroku:

.. image:: https://www.herokucdn.com/deploy/button.svg
    :alt: Deploy to Heroku button
    :target: https://heroku.com/deploy?template=https://github.com/adrind/startherecms

This will prompt you to create an admin username + password. Remember what you type! We will use this account information
to login later.

=======================
Run the project locally
=======================

Coming soon!