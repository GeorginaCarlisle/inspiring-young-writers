from django.shortcuts import render
from django.views.generic import TemplateView


class AccountHome(TemplateView):
    """ View for the landing page """
    template_name = 'account_home.html'
