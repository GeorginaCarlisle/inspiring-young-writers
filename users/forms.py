from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


"""
Code for validation against swear words copied and adapted from an example given by Chatgpt
"""
SWEAR_WORD_LIST = ['fuck', 'shit', 'crap', 'bollocks', 'bitch', 'cock', 'cunt', 'cum', 'fucker', 'dick']

def validate_no_swearing(value):
    for swear_word in SWEAR_WORD_LIST:
        if swear_word.lower() in value.lower():
            raise forms.ValidationError(
                f"Swear word '{swear_word}' is not allowed. Please remove."
            )


"""
Custom validator passing through clear messaging when age requirements are not met
"""
def validate_age(value):
    if value < 8:
        raise forms.ValidationError(
            "Sorry but this platform has been specifically designed for children aged 8 to 12"
        )
    if value > 12:
        raise forms.ValidationError(
            "Sorry but this platform has been specifically designed for children aged 8 to 12"
        )


"""
The following Tutorial was followed and adapted when creating the NewUserForm
Register New Users with Django Custom User by CodingWithMitch
https://www.youtube.com/watch?v=sbCd52JiCU4
"""
class NewUserForm(UserCreationForm):

    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'style': 'border-color: black'}),
        validators=[validate_no_swearing])
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'style': 'width: 40px'}),
        validators=[validate_age])
    first_name = forms.CharField(max_length=12)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    consent = forms.BooleanField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'age', 'first_name', 'last_name', 'email',
                  'consent', 'password1', 'password2')

    # Add borders around input boxes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['age'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['email'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'border border-black'})


"""
The following Tutorial was followed and adapted when creating the LoginForm
Login and Logout with Django by CodingWithMitch
https://www.youtube.com/watch?v=5qhlDC_bQsA
"""


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid Login")

    # Add borders around input boxes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['password'].widget.attrs.update(
            {'class': 'border border-black'})
