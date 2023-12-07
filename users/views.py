from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm, LoginForm


"""
The following Tutorial was followed and adapted when creating the sign_up_view
Register New Users with Django Custom User by CodingWithMitch
https://www.youtube.com/watch?v=sbCd52JiCU4
"""


def sign_up_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.username}")

    context = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request,
                'Form not valid. Please correct before clicking to signup')
            context['new_user_form'] = form
    else:
        form = NewUserForm()
        context['new_user_form'] = form

    return render(request, 'signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request, *args, **kwargs):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("account_home")

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return redirect('account_home')
        else:
            messages.error(
                request,
                'Form not valid. Please correct before clicking to signup')
            context['login_form'] = form
    else:
        form = LoginForm()
        context['login_form'] = form

    return render(request, 'login.html', context)
