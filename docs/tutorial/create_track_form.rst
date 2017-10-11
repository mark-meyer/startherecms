===================
Create a Track form
===================

Some users might need help deciding which Step or Steps is right for them. You can use the  **Options Form** field in
the Track page to create an easy form (aka a quiz or a survey) that helps a user narrow down their options.

For the dog breed Track, let’s create a simple form to help a user decide what dog breeds might be good for
their family:

.. image:: ../_static/tutorial/youtube_icon.png
    :align: left
    :alt: An icon of a movie playing

`How to create a basic Options Form on the Track page <https://www.youtube.com/watch?v=_lzTPVs6TC0&feature=youtu.be>`_

At the end you should see this survey on your Track page:

.. image:: ../_static/tutorial/basic_track_form.png
    :align: center
    :alt: A Track page with an Options Form to help a user pick a dog breed

There’s a lot going on here. Let’s look at the fields we have to fill out.

.. image:: ../_static/tutorial/definition_icon.png
    :align: left
    :alt: A magnifying glass

**Question** - This is the question for your form. Focus on making it simple and easy for someone to answer.

.. image:: ../_static/tutorial/definition_icon.png
    :align: left
    :alt: A magnifying glass

**Choices** - The choices a user can select from to answer the question. You can have as many as you want, but we
recommend keeping it fewer than eight so a user isn’t overwhelmed by the checkboxes.

.. image:: ../_static/tutorial/definition_icon.png
    :align: left
    :alt: A magnifying glass

**Has strict rules** - If this box is checked then the form will only display steps for a rule that matches the exact
choices selected. If this box is not checked the form will display the steps for the union of all matched choices
(explained more below).

.. image:: ../_static/tutorial/definition_icon.png
    :align: left
    :alt: A magnifying glass

**Rules** - These are the rules you need to define to determine what Steps we show to a user based on the choices
they select.

.. image:: ../_static/tutorial/definition_icon.png
    :align: left
    :alt: A magnifying glass

**Default steps** - (optional) If a user selects a choice or combination of choices that do not have associated rules,
then show this list of pages. If no list of default steps is provided, the form will show all the steps
(aka the default of the default is all of the steps)

Let’s look at an example of a rule:

.. image:: ../_static/tutorial/example_rule_1.png
    :align: center
    :alt: An example of a rule defined in the Wagtail admin
