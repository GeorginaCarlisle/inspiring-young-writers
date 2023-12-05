"""
The following Tutorial was followed when creating the models in this file
Learn Django - Build a Custom User Model with Extended Fields by Very Academy
https://www.youtube.com/watch?v=Ae7nc1EGv-A
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class CustomAccountManager(BaseUserManager):

    def create_user(self, pen_name, age, password, first_name, last_name,
                    email, consent, **other_fields):

        # set and save user
        email = self.normalize_email(email)
        user = self.model(pen_name=pen_name, age=age, first_name=first_name,
                          last_name=last_name, email=email, consent=consent,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, pen_name, email, first_name, last_name,
                         password, ** other_fields):

        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)

        # set and save superuser
        email = self.normalize_email(email)
        # age of all superusers set to 100. Field must be given a value
        age = 100
        super_user = self.model(pen_name=pen_name, first_name=first_name,
                                last_name=last_name, email=email, age=age,
                                **other_fields)
        super_user.set_password(password)
        super_user.save()
        return super_user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    __name__ = 'CustomUser'

    pen_name = models.CharField(max_length=20, unique=True)
    age = models.IntegerField()
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    consent = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)

    # Link to CustomAccountManager class
    objects = CustomAccountManager()

    # Sets field to be used to user login
    USERNAME_FIELD = 'pen_name'

    # Sets fields that will be required for super user creation
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.pen_name
