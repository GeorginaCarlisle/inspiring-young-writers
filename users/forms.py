from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


"""
The following Tutorial was followed and adapted when creating the NewUserForm
Register New Users with Django Custom User by CodingWithMitch
https://www.youtube.com/watch?v=sbCd52JiCU4
"""


class NewUserForm(UserCreationForm):

    username = forms.CharField(max_length=20)
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'style': 'width: 40px'}))
    first_name = forms.CharField(max_length=12)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    consent = forms.BooleanField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'age', 'first_name', 'last_name', 'email',
                  'consent', 'password1', 'password2')
