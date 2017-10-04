# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django import forms
from django.db import models
from django.conf import settings
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.utils.functional import cached_property
from django.utils.html import format_html_join

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.url_routing import RouteResult
from wagtail.wagtailcore import hooks
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtailgeowidget.edit_handlers import GeoPanel
from wagtailgeowidget.helpers import geosgeometry_str_to_struct


# A contact that someone should reach out to
# Used in the step templates
@register_snippet
class Contact(models.Model):
    name = models.CharField(max_length=255, help_text="The name of someone to contact. Ex: Sharon Smith")
    location = models.CharField(max_length=255, blank=True, help_text="An address for where this person works")
    email = models.EmailField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=16, blank=True) # validators should be a list
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('location'),
        FieldPanel('email'),
        FieldPanel('phone_number'),
        ImageChooserPanel('image'),
    ]

    def __str__(self):
        return self.name


# Allows admins to create logic that directs users to specific steps
# Used in the track templates
class ChoiceRulesBlock(blocks.CharBlock):
    def __init__(self, required=True, help_text=None, max_length=None, min_length=None,
                 **kwargs):
        super(ChoiceRulesBlock, self).__init__(**kwargs)

    def field(self):
        field_kwargs = {}
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)

    def clean(self, value):
        return super(ChoiceRulesBlock, self).clean(value)

    def render_form(self, value, prefix='', errors=None):
        if value:
            choices = value.split(',')
            choicesHtml = ''
            for choice in choices:
                choicesHtml = choicesHtml + '<button class="selected-choice button bicolor icon icon-cross" data-id="'+choice+'" style="margin:0;margin-right:.5rem;margin-top:.5rem;white-space: normal;max-width: 250px;"></button>'
            out = """<div class="new-choice-button-group"></div><h4><strong>When someone selects:</strong></h4> <div class="selected-choice-container">{}</div><h4><strong>Direct them to these pages:</strong></h4>""".format(choicesHtml)
        else:
            value = 'NEW'
            out = """<div class="new-choice-button-group"></div><h4><strong>When someone selects:</strong></h4> <div class="selected-choice-container">{}</div><h4><strong>Direct them to these pages:</strong></h4>""".format('')

        out = '<div class="sequence-container sequence-type-list choice-list-container" id="'+ prefix +'-container"> <div class="field-content"><input type="hidden" class="selected-choice-input" name="rules-NUM-value-name" value="'+value +'" placeholder="Name" id="rules-NUM-value-name">' + out + '</div></div>'

        return mark_safe(out + '<script>(function(){if (document.readyState === "complete") {return initializeChoices("'+prefix+'");}$(window).load(function() {initializeChoices("'+prefix+'");});})();</script>')

    def value_from_form(self, value):
        arr = value.split(',')
        arr.sort()
        val = ','.join(arr)
        return super(ChoiceRulesBlock, self).value_from_form(val)

class TaskChoicesBlock(blocks.StreamBlock):
    question = blocks.CharBlock()
    choices = blocks.ListBlock(blocks.StructBlock([
        ('label', blocks.CharBlock(required=True)),
    ]))

    class Meta:
        label='Add choices to guide a client to services'
        template='roadmap/track/partials/_choice_form.html'

# A Track -- contains a series of steps that a user can do to accomplish a specific goal
class Track(Page):
    page_body = RichTextField(blank=True, help_text="The main content of the page, above the list of steps and form")
    form_submission_message = models.CharField(max_length=255, help_text="The text that is shown to the user after they make a form submissiom", default="Based on your choices we suggest looking at the following:")
    question = models.CharField(max_length=255, blank=True, help_text="The question for the form on the page (optional)")
    choices = StreamField([
        ('label', blocks.CharBlock(required=True)),
    ], blank=True, null=True)

    has_strict_rules = models.BooleanField(default=False, help_text="If the rule definitions are strict it will ONLY display results that match the exact answers (instead of the union of the answers)")

    rules = StreamField([
        ('rule', blocks.StructBlock([
            ('name', ChoiceRulesBlock()),
            ('pages', blocks.ListBlock(blocks.PageChooserBlock())),
            ('override', blocks.BooleanBlock(default=False, required=False))
        ]))], default=[], blank=True)

    default_steps = StreamField([
        ('page', blocks.PageChooserBlock())
    ], blank=True, default=[], help_text="The steps to show if someone submits a form with answers that are not covered by the rules")

    content_panels = Page.content_panels + [
        FieldPanel('page_body', classname='full'),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('question'),
                FieldPanel('form_submission_message'),
                StreamFieldPanel('choices')
            ]),
            FieldPanel('has_strict_rules'),
            StreamFieldPanel('rules'),
            StreamFieldPanel('default_steps'),
        ], heading="Options form for the page to help narrow down choices", classname="collapsible")
    ]

    template = 'roadmap/track/base.html'

    def steps(self):
        # Get list of all step pages that are descendants of this page
        events = Step.objects.live().descendant_of(self)
        return events

    # Directs people to the walk through or self service routes
    # Walk through path uses the choices model to filter steps to take
    def route(self, request, path_components):
        if len(request.GET):
            return RouteResult(self, kwargs={'template': 'roadmap/track/base.html'})
        else:
            return super(Track, self).route(request, path_components)

    def serve(self, request, template=''):
        if template == '':
            template = self.template
        #Kind of hacky but intercept request if it has 'submit-choice' in the slug
        #Serve the rules for the selected choices
        if len(request.GET):
            #Get selected checkbox values from params in request
            selected_choices = list(request.GET.values())

            #Sort the choices so we have them in the same order as the admin defined rules
            selected_choices.sort()

            pages = [] #list of pages that will be presented to the user
            default_pages = [] #default pages if there isn't a rule defined for the choices the user selected
            all_selected_choices = ','.join(selected_choices)

            #loop through each admin defined rule to see if we have a defined rule for the selected choices
            if self.has_strict_rules:
                #Find the one rule that matches the selected choices and only suggest those steps
                for rule in self.rules:
                    if rule.value['override'] and re.search(rule.value['name'], all_selected_choices):
                        pages = rule.value['pages']
                        break
                    if rule.value['name'] == all_selected_choices:
                        pages = rule.value['pages']
            else:
                #Union all the pages that match with a rule
                for rule in self.rules:
                    if rule.value['override'] and re.search(rule.value['name'], all_selected_choices):
                        pages = rule.value['pages']
                        break
                    if rule.value['name'] in selected_choices:
                        for page in rule.value['pages']:
                            if page not in pages:
                                pages.append(page)

            for page in self.default_steps:
                #if the user defines default pages in the admin then create a list of pages
                #otherwise the default default_pages list is all the steps in the track
                default_pages.append(Page.objects.get(id=page.value.id))

            if not pages:
                if not default_pages:
                    default_pages = Step.objects.live().descendant_of(self)
                pages = default_pages

            request.path = '/'.join(request.path.split('/')[:3])

            return render(request, template, {
                'steps': list(map((lambda page: page.specific), pages)),
                'page': self,
                'selected_choices': ','.join(map(str, selected_choices)),
                'default_pages': default_pages,
                'showMessage': True
            })
        #Otherwise just render the track page with the appropriate template
        return render(request, template, {
            'page': self,
            'steps': self.steps()
        })

class Step(Page):
    short_description = models.CharField(max_length=75, help_text="A short preview of what the page is about")
    page_body = RichTextField(blank=True)
    checklist_instructions = RichTextField(blank=True, help_text="Specific instructions provided when a user prints the page. Keep it short!")

    address = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)

    contact = models.ForeignKey(
        'roadmap.Contact',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('short_description', classname='full'),
        FieldPanel('page_body', classname='full'),
        FieldPanel('checklist_instructions', classname='full'),
        SnippetChooserPanel('contact'),
        MultiFieldPanel([
            FieldPanel('address'),
            GeoPanel('location', address_field='address'),
        ], _('Location of the step')),
    ]

    template = 'roadmap/step/base.html'

    @cached_property
    def point(self):
        return geosgeometry_str_to_struct(self.location)

    @property
    def lat(self):
        return self.point['y']

    @property
    def lng(self):
        return self.point['x']

@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'js/choices_panel.js',
    ]
    js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )
    return js_includes

