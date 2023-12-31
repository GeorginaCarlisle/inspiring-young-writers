from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_view, name='library'),
    path('read/<int:writing_id>', views.read_view, name='read'),
    path('give_feedback/<int:writing_id>',
         views.give_feedback_view,
         name="give_feedback"),
    path('read_feedback/<int:writing_id>',
         views.read_feedback_view,
         name="read_feedback"),
    path('edit_feedback/<int:feedback_id>',
         views.edit_feedback_view,
         name="edit_feedback"),
    path('delete_feedback/<int:feedback_id>',
         views.delete_feedback_view,
         name="delete_feedback"),
]
