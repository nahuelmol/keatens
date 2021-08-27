from django.contrib import admin
from django.urls import path, include


from accounts.views import Profile, Events, Teams, LoginPage

urlpatterns = [
    path('profile/', Profile),
    path('events/',Events),
    path('teams/', Teams),
    path('api/',include('accounts.api.urls',namespace='appi'))
]