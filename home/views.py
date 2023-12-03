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

    def post(self, request, *args, **kwargs):
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        message = request.POST['message']

        return render(request, 'contact.html', {'name': first_name})