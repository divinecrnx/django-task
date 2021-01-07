from django.shortcuts import render
from .forms import UserSignupForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    
    if request.method == 'POST':

        form = UserSignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            return HttpResponseRedirect(reverse('index:index'))
    else:
        form = UserSignupForm()

    return render(request, 'signup/signup.html', {'form': form})