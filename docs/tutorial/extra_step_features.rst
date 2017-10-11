=============================
Extra features for Step pages
=============================

The beauty of a Step page is in its simplicity but sometimes you want to highlight key details.
This Wagtail application lets you define locations and people to contact that can become associated with each Step page.
Let’s walk through how to create them.

----------------
Create a Contact
----------------

.. image:: ../_static/tutorial/definition_icon.png
    :align: left
    :alt: A magnifying glass

**Contact** - Contacts are reusable pieces of information that can be connected to certain Step pages.
Use Contacts to direct your users to useful people and organizations who can provide further help.
They must be created before being selected in the Contact field.

Creating a Contact is as simple as navigating to the “Snippets” link on the left hand navigation bar.

.. image:: ../_static/tutorial/youtube_icon.png
    :align: left
    :alt: An icon of a movie playing

`How to create a Contact for a Step page <https://www.youtube.com/watch?v=eyZZsSH_3Zw&feature=youtu.be>`_

Once you create the Contact, navigate to the Step page and add it as the Contact field:

.. image:: ../_static/tutorial/youtube_icon.png
    :align: left
    :alt: An icon of a movie playing

`How to save a Contact to a Step page <https://www.youtube.com/watch?v=nrOiMjQEk_U&feature=youtu.be>`_

Creating Contacts in Snippets allows you to reuse Contacts across multiple Step pages without having to add the same
information over and over again. This also means that there’s only one place you need to update information in case something
changes about that contact.

After adding a Contact you should see it in the right hand side:

.. image:: ../_static/tutorial/contact_example.png
    :align: center
    :alt: A Step page with a contact on it

--------------
Add a location
--------------
.. image:: ../_static/tutorial/definition_icon.png
    :align: left
    :alt: A magnifying glass

**Location of the Step** - Sometimes a Step will have a specific location a user can go to. By using Google Maps,
we can highlight that location in the right column under Contacts.

.. NOTE::
    You can only use this field if you have a Google Maps API key defined in your Heroku settings.

This widget uses the GOOGLE_MAPS_API_KEY, GOOGLE_WIDGET_DEFAULT_LAT, and GOOGLE_WIDGET_DEFAULT_LONG
you defined in your Heroku settings earlier.

.. image:: ../_static/tutorial/youtube_icon.png
    :align: left
    :alt: An icon of a movie playing

`How to add a Location to a Step page <https://www.youtube.com/watch?v=epXkZc9vrRA&feature=youtu.be>`_

After you add a location to the page it should look something like this

.. image:: ../_static/tutorial/location_example.png
    :align: center
    :alt: A Step page with a location on it


