from .views import AccountHome
from django.urls import path


urlpatterns = [
    path('account_home/', AccountHome.as_view(), name='account_home'),
]
