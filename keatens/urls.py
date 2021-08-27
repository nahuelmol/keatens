from django.contrib import admin
from django.urls import path, include

from accounts.views import LoginPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('accounts.urls')),
    path('login/', LoginPage, name='login')
]
