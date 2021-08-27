from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action

from django.contrib.auth.models import User

from accounts.forms import UserForm
from accounts.api.serializers import UserSerializer
from accounts.decorators import unauthenticated_user

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(unauthenticated_user,name='create')
class RegisterView(viewsets.ViewSet):
	form = UserForm()

	def create(self,request):

		form = UserForm(req.POST)
		
		print(req.POST)

		if form.is_valid():
			user 		= form.save()
			username 	= form.cleaned_data.get('username')
			role		= form.cleaned_data.get('role')

			return redirect('login')


@method_decorator(unauthenticated_user,name='create')
class LoginView(viewsets.ViewSet):
	permission_classes = ()

	def create(self,request):
		username 	= request.data.get("username")
		password	= request.data.get("password")

		user 		= authenticate(username=username, password=password)

		if user:
			return Response({"token":user.auth_token.key})
		else:
			return Response({"error":"Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

