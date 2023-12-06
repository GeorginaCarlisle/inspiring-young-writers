"""
The following Tutorial was followed when creating the NewUserForm
Custom User Registration Django (AbstractBaseUser and UserCreationForm) by
CodingWithMitch
https://www.youtube.com/watch?v=oZUb372g6Do
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class NewUserForm(UserCreationForm):

    pen_name = forms.CharField(max_length=20)
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'style': 'width: 40px'}))
    first_name = forms.CharField(max_length=12)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(
        widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}))
    consent = forms.BooleanField()
    username = pen_name

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",
                                                 "first_name", "last_name",
                                                 "email", "consent")
