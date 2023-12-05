from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.exceptions import ValidationError

"""
The following Tutorial was followed when creating the models in this file
Learn Django - Build a Custom User Model with Extended Fields by Very Academy
https://www.youtube.com/watch?v=Ae7nc1EGv-A
"""


def validate_age(value):
    if value < 8:
        raise ValidationError(
            _('You are not old enough to register for this platform'),
            params={'value': value},
        )
    elif value > 12:
        raise ValidationError(
            _('You are too old to register for this platform'),
            params={'value': value},
        )


class User(AbstractBaseUser, PermissionsMixin):

    pen_name = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(validators=[validate_age])
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    consent = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=timezone.now)

    # Sets field to be used to user login
    USERNAME_FIELD = 'pen_name'

    # Sets fields that will be required for super user creation
    REQUIRED_FIELDS = ['pen_name', 'email', 'first_name', 'last_name']

    def __str__(self):
        return self.pen_name
