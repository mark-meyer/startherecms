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

Once you sign up for these services you need the following keys to launch your application:

.. csv-table:: Required keys to create the website
   :header: "Name of key", "How to find it", "Example value"
   :widths: 15, 30, 10

   "AWS_ACCESS_KEY_ID", :ref:`Find your access key <aws_existing_user>`, KUDFHGJKHRUFDBF
   "AWS_SECRET_ACCESS_KEY", :ref:`Create a secret key <aws_existing_user>`, 2IUGFD/8vD9/k7s6
   "AWS_STORAGE_BUCKET_NAME", :ref:`Create your bucket <aws_bucket>`, start-here-dog-files

Additionally there are some optional (free!) services you can use for added functionality:

* Google Analytics -- used to track how people use your website
* Google Maps -- used to let you set locations of community organizations on a map
* Algolia -- used to power a search box on your website so people can easily find pages

.. csv-table:: Optional keys for additional services
   :header: "Name of key", "How to find it", "Example value"
   :widths: 15, 30, 10

   "GOOGLE_MAPS_API_KEY", `Get an API key here <https://developers.google.com/maps/documentation/javascript/get-api-key>`_, AIv80f_8tueriogjURGYE
   "GOOGLE_WIDGET_DEFAULT_LAT", `Find your latitude <http://www.worldatlas.com/aatlas/findlatlong.htm>`_ , 37.773972
   "GOOGLE_WIDGET_DEFAULT_LONG", `Find your longitude <http://www.worldatlas.com/aatlas/findlatlong.htm>`_ , -122.431297
   "GOOGLE_WIDGET_DEFAULT_LONG", `Find your longitude <http://www.worldatlas.com/aatlas/findlatlong.htm>`_ , -122.431297
   "GOOGLE_ANALYTICS_ID", Guide coming soon, fkugsh
   "ALGOLIA_APP_ID", Guide coming soon, Q87VFIUEH
   "ALGOLIA_PUBLIC_KEY", Guide coming soon, ce0896nbfsHUGfdgrz9b

.. _deploy_heroku:

Once you have a Heroku account and an AWS bucket set up, you can start! Click the deploy button to create your project in Heroku:

.. image:: https://www.herokucdn.com/deploy/button.svg
    :alt: Deploy to Heroku button
    :align: center
    :target: https://heroku.com/deploy?template=https://github.com/adrind/startherecms

This will prompt you to create an admin username + password. Remember what you type! We will use this account information
to login later. Viewing your app after Heroku builds it should show a simple "Hello World" website like this:

.. image:: _static/tutorial/basic_wagtail_app.png
    :alt: The basic Hello World Wagtail app

Want a full guide on how to structure and setup your website? Follow our :doc:`Tutorial <tutorial>`!

=======================
Run the project locally
=======================

Coming soon!