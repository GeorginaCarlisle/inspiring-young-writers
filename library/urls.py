from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_view, name='library'),
    path('read/<int:writing_id>', views.read_view, name='read'),
]