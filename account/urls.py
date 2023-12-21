from .views import AccountHome, AccountContact
from django.urls import path


urlpatterns = [
    path('account_home/', AccountHome.as_view(), name='account_home'),
    path('account_contact/', AccountContact.as_view(), name='account_contact'),
]
