from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_writing_view, name='create'),
    path('my_work/<int:user_id>', views.my_writing_view, name='my_work'),
    path('edit/<int:writing_id>', views.edit_writing_view, name='edit'),
    path('view/<int:writing_id>', views.view_writing_view, name='view')
]