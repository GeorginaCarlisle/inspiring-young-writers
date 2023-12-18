"""inspiringyw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name=''),
    path('user/', include('users.urls'), name=''),
    path('account/', include('account.urls'), name=''),
    path('writing/', include('writing.urls'), name=''),
    path('library/', include('library.urls'), name=''),

    # Password reset links copied from 'Password Reset and Password Change (Django)' tutorial by CodeWithMitch
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset.html'),
         name='password_reset'),    
    
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_sent.html'),
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_form.html'),
         name='password_reset_confirm'),


    
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
]

# Error Pages
handler404 = handler404
handler500 = handler500

# Admin Site basic costumisation
admin.site.site_header = "Inspiring Young Writers administration"
admin.site.site_title = "Inspiring YW Admin"