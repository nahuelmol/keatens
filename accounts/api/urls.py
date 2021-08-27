from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from accounts.api.views import LoginView, RegisterView

app_name = 'api-name'

router = routers.SimpleRouter(trailing_slash=False)

login_view		= LoginView
register_view	= RegisterView
#unique_user 	= UserView.as_view({'get':'retrieve'})

router.register(r'register',	register_view, basename='register')
router.register(r'login',		login_view,basename='login-view')


urlpatterns = router.urls