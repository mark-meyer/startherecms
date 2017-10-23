==================
Setting up Algolia
==================

You can use `Algolia <https://www.algolia.com>`_ to power a free search box on your website.
Algolia will let you index all your Step pages so your users can easily search through the body text and find what they are looking for.
Once you add the following keys to your application, you should see a search box appear in the header.

1. Sign up for a Community account (it's free!)
2. Login and go to `your dashboard <https://www.algolia.com/dashboard>`_
3. Click on "API Keys" in the left nav to find your app's API keys
4. You should see **three** keys:

.. image:: ../_static/images/algolia_keys.png
   :alt: The three keys listed on Algolia API

**Application ID:** used in your Heroku configuration as ALGOLIA_APP_ID

**Admin API Key:** used in your Heroku configuration as ALGOLIA_API_KEY

**Search Only API Key:** used in your :doc:`Site Settings <../tutorial/site_settings>` as ALGOLIA PUBLIC KEY

Once you have your application properly configured, go to your Heroku application dashboard and run the following commands in the Heroku console:

.. code::

    python manage.py algolia_reindex


.. code::

    python manage.py algolia_applysettings


Run these commands every time you update or add a new :ref:`Step <step>` page so the search is up-to-date!