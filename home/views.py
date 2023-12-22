""" The following project was used as a reference point
when writing the code in this file:
https://github.com/GeorginaCarlisle/brobonds-movember-hackathon"""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from writing.models import Writing
import os


class Index(TemplateView):
    # View for the landing page
    template_name = 'index.html'

    # Ensure future functions are called every time this view is
    def get(self, request, *args, **kwargs):
        # If a logged in user ends up in this view redirect to account_home
        if request.user.is_authenticated:
            return redirect('account_home')
        return super().get(request, *args, **kwargs)

    # Function to pass the featured writing through
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        featured_writing = Writing.objects.filter(featured = True)

        context['featured_writing'] = featured_writing
        return context


class Contact(TemplateView):
    # View for the contact page
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
    # Check if the user is logged in
        if request.user.is_authenticated:
            # Redirect to a different view for logged-in users
            return redirect('account_contact')

        return super().get(request, *args, **kwargs)


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
