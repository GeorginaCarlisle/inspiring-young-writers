from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm, LoginForm


def sign_up_view(request):
    """
    View for the sign-up page that handles the sign-up form data
    and saves the form (if valid) thus creating a new instance of user
    and then logs the new user in.
    It also checks that there is not already a logged in user.
    The following Tutorial was followed and adapted:
    Register New Users with Django Custom User by CodingWithMitch
    https://www.youtube.com/watch?v=sbCd52JiCU4
    """
    user = request.user
    if user.is_authenticated:
        return HttpResponse(
            f"You are already authenticated as {user.username}")

    context = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully signed up")
            return redirect('account_home')
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
    """
    View to handle clicking of the log out button
    The following Tutorial was followed and adapted:
    Login and Logout with Django by CodingWithMitch
    https://www.youtube.com/watch?v=5qhlDC_bQsA
    """
    logout(request)
    messages.success(request, "You were successfully logged out")
    return redirect('home')


def login_view(request):
    """
    View for the login page that handles the login form data and
    if valid logs in the user taking them to account_home.
    It also checks that there is not already a logged in user.
    The following Tutorial was followed and adapted:
    Login and Logout with Django by CodingWithMitch
    https://www.youtube.com/watch?v=5qhlDC_bQsA
    """
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
            login(request, user)
            messages.success(request, "You were successfully logged in")
            return redirect('account_home')
        else:
            messages.error(
                request,
                'Details given do not match a registered user')
            form = LoginForm()
            context['login_form'] = form
    else:
        form = LoginForm()
        context['login_form'] = form

    return render(request, 'login.html', context)
