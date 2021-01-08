from django.shortcuts import render
from django.contrib.auth import views

# Create your views here.

class LogoutView(views.LogoutView):
    template_name = 'logout/logout.html'