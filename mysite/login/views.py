from django.shortcuts import render
from django.contrib.auth import views
from .forms import LoginForm

# Create your views here.

class LoginView(views.LoginView):
    template_name = 'login/login.html'
    authentication_form = LoginForm
