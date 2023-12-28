from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.utils import timezone
from django.core.validators import (
    MinValueValidator, MaxValueValidator, RegexValidator
)


"""
The following Tutorial was followed and adapted when creating:
the user model and manager
Custom User Model with email login (DJANGO) by CodingWithMitch
https://www.youtube.com/watch?v=SFarxlTzVX4
"""


class CustomAccountManager(BaseUserManager):

    def create_user(self, username, age, first_name, last_name,
                    email, consent, password=None):

        # Add validation
        if not username:
            raise ValueError("You must have a pen name")
        if not age:
            raise ValueError("You must include your age")
        if not first_name:
            raise ValueError("Parent/Guardian first name must be included")
        if not last_name:
            raise ValueError("Parent/Guardian last name must be included")
        if not email:
            raise ValueError("Parent/Guardian email must be included")
        if not consent:
            raise ValueError("Parent/Guardian must give consent")
        if age < 8:
            raise ValueError(
                'You must be 8 or older to use this platform'
            )
        if age > 12:
            raise ValueError(
                'You must be 12 or younger to use this platform'
            )
        user = self.model(
            username=username,
            age=age,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            consent=consent,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, first_name, last_name,
                         password):

        super_user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
            age=12,
            consent=True,
        )
        super_user.is_admin = True
        super_user.is_staff = True
        super_user.is_superuser = True
        super_user.save(using=self.db)
        return super_user


class User(AbstractBaseUser, PermissionsMixin):

    __name__ = 'CustomUser'

    # Specifc validators for username, first_name and last_name
    validUsername = RegexValidator(
        r'^[a-zA-Z ]+$',
        'Only letters and spaces are allowed in your Pen name')
    validFirstName = RegexValidator(
        r'^[a-zA-Z ]+$',
        'Only letters and spaces are allowed in your First name')
    validSecondName = RegexValidator(
        r'^[a-zA-Z ]+$',
        'Only letters and spaces are allowed in your Second name')

    username = models.CharField(
        max_length=20, unique=True, validators=[validUsername])
    age = models.IntegerField(
        validators=[MinValueValidator(8), MaxValueValidator(12)], )
    first_name = models.CharField(max_length=12, validators=[validFirstName])
    last_name = models.CharField(max_length=20, validators=[validSecondName])
    email = models.EmailField(max_length=320)
    consent = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # Link to CustomAccountManager class
    objects = CustomAccountManager()

    # Sets field to be used to user login
    USERNAME_FIELD = 'username'

    # Sets fields that will be required for super user creation
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def has_perm(self, per, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True
