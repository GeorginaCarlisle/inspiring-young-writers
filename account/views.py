import os
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail


@method_decorator(login_required, name='dispatch')
class AccountHome(TemplateView):
    """
    View for the account_home page
    """
    template_name = 'account_home.html'


@method_decorator(login_required, name='dispatch')
class AccountContact(TemplateView):
    """
    View for the contact page that handles the contact form data and
    pulls the parent contact details from the user object
    sending these via email to the site owner.
    """
    template_name = 'account_contact.html'

    def post(self, request):
        """
        This function was created while following
        a YouTube tutorial by Codemy.com:
        'How To Send Email With Django - Python Django Dentist Website #7'
        https://www.youtube.com/watch?v=xNqnHmXIuzU
        """

        # Pull data from user
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email

        # Capture data submitted in conatct us form
        message = request.POST['message']

        # send contact us data in email to site owner
        owner_email = os.environ.get('SITE_OWNER_EMAIL')
        send_mail(
            'Inspiring Young Writers - User contact',
            f'Email from {first_name} {last_name}\n{email}\n{message}',
            email,
            [owner_email],
        )

        return render(request, 'account_contact.html', {'success': 'True'})
