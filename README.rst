=====================
Django statictemplate
=====================

!!!under develop!!!
-------------------

render static template from one direction

It will by push to https://pypi.org soon. And maybe I write some help for other
people.

Quick start
-----------
Include the statictemplate URLconf in your project urls.py like this::

    path('newsletter/', include('statictemplate.urls')),

Create the folder '/templates/statictemplate/' and add some static templates.
Get the url with

    {% url 'statictemplate' name='help' %}

for the template 'help.html'.
