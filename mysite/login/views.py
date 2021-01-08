from django.shortcuts import render, redirect
from django.contrib.auth import views
from .forms import LoginForm

# Create your views here.

class LoginView(views.LoginView):
    template_name = 'login/login.html'
    authentication_form = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:index')
        return super(LoginView, self).get(request, *args, **kwargs)
