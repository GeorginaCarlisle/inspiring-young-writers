""" The following project was used as a reference point 
when writing the code in this file: 
https://github.com/GeorginaCarlisle/brobonds-movember-hackathon"""

from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    """ View for the landing page """
    template_name = 'index.html'

class Contact(TemplateView):
    """ View for the contact page """
    template_name = 'contact.html'