""" The following project was used as a reference point
when writing the code in this file:
https://github.com/GeorginaCarlisle/brobonds-movember-hackathon"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from writing.models import Writing
import os


class Index(TemplateView):
    """ View for the landing page """
    template_name = 'index.html'

    """ Ensure future functions are called every time this view is """
    def get(self, request, *args, **kwargs):
        print("Index view was called!")
        self.featured_writing(request)
        return super().get(request, *args, **kwargs)

    """ Function to render the featured writing """
    def featured_writing(self, request):
        context = {}
        featured_writing = Writing.objects.filter(approved = True)

         # Print the count of featured writings
        print("Count of Featured Writings:", featured_writing.count())

        context['featured_writing'] = featured_writing
        print("Context:", context)
        return render(request, 'index.html', context)


class Contact(TemplateView):
    """ View for the contact page """
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        """
        This function was created while following
        a YouTube tutorial by Codemy.com:
        'How To Send Email With Django - Python Django Dentist Website #7'
        https://www.youtube.com/watch?v=xNqnHmXIuzU
        """

        # Capture data submitted in conatct us form
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        message = request.POST['message']

        # send contact us data in email to site owner
        owner_email = os.environ.get('SITE_OWNER_EMAIL')
        send_mail(
            'Inspiring Young Writers - User contact',
            f'Email from {first_name} {last_name}\n{email}\n{message}',
            email,
            [owner_email],
        )

        return render(request, 'contact.html', {'name': first_name})
