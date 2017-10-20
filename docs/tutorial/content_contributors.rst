====================
Content Contributors
====================

There are many ways to manage who can contribute content to your website.

**Admin:** Admins have access to everything in your application. Provision admin accounts only to individuals
you trust!

**Users:** You can control what pages you want Users to be able to add, edit, and delete.

**Groups:** You can set access to certain pages at a “Group” level. Any User you add to that Group gets the
permissions for that Group.

.. _create_new_admin:


Create new admin
~~~~~~~~~~~~~~~~

Creating an admin can be done one of two ways -- either programmatically using your terminal, or with an admin account
through the Wagtail admin interface.

If you already have an admin account created
''''''''''''''''''''''''''''''''''''''''''''

You can login to Wagtail and provision a new account through the Admin interface.

.. image:: ../_static/tutorial/youtube_icon.png
    :align: left
    :alt: An icon of a movie playing

`How to add a new admin account through the Wagtail admin <https://www.youtube.com/watch?v=k9rj1x2QJNs&feature=youtu.be>`_

If you are setting up the website for the first time
''''''''''''''''''''''''''''''''''''''''''''''''''''

If you are a developer working on it locally and didn't provision an admin account through
the :ref:`Heroku quickstart <deploy_heroku>` you can follow these easy steps.

Run `python manage.py` createsuperuser to locally create a new admin account for your local website deploy.

If provisioning an account for a website hosted on heroku run `heroku run python manage.py createsuperuser` from
the repository that’s hosted.


Create new group
~~~~~~~~~~~~~~~~

Use groups to control who can update certain parts of your website. This makes it easy when you create a new user
because you can simply add them to the group(s) to manage permissions.

All Wagtail apps come with “Editors” and “Moderators” as defined group. You can use these or delete them and
make your own!

.. image:: ../_static/tutorial/youtube_icon.png
    :align: left
    :alt: An icon of a movie playing

`How to add a new group through the Wagtail admin <https://www.youtube.com/watch?v=sBQDtKQhXEg&feature=youtu.be>`_


Add a new user to a group
~~~~~~~~~~~~~~~~~~~~~~~~~

Now when you add a new user (the same way you :ref:`created a new Admin <create_new_admin>`) you can assign them to
groups using the “Role” section.


More about Permissions
~~~~~~~~~~~~~~~~~~~~~~

To learn more about how to structure your Permissions,
read `Wagtail's very own guide <http://docs.wagtail.io/en/v1.12.2/topics/permissions.html>`_


