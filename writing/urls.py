from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_writing_view, name='create'),
    path('my_work/<int:user_id>', views.my_writing_view, name='my_work'),
]