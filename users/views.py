"""
The following Tutorial was followed when creating the sign_up_view
Custom User Registration Django (AbstractBaseUser and UserCreationForm) by 
CodingWithMitch
https://www.youtube.com/watch?v=oZUb372g6Do
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewUserForm


def sign_up_view(request):
    context = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            pen_name = form.cleaned_data['pen_name']
            raw_password = form.cleaned_data['password1']
            account = authenticate(pen_name=pen_name, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['new_user_form'] = form
    else:
        form = NewUserForm()
        context['new_user_form'] = form

    return render(request, 'signup.html', context)
