""" The following project was used as a reference point 
when writing the code in this file: 
https://github.com/GeorginaCarlisle/brobonds-movember-hackathon"""

from django.urls import path
from .views import Index

urlpatterns = [
  path('', Index.as_view(), name='home'),
]