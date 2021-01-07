from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    
    if request.method == 'POST':

        form = UserSignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username):
                messages.error(request, 'Username already exists. Please choose another.')
                return redirect(reverse('signup:index'))
            elif User.objects.filter(email=email):
                messages.error(request, 'Email already exists. Please choose another.')
                return redirect(reverse('signup:index'))
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                messages.success(request, 'Successfully registered! Time to log in.')
                return redirect(reverse('index:index'))
    else:
        form = UserSignupForm()

    return render(request, 'signup/signup.html', {'form': form})