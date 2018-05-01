from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import *

# Create your views here.
def index(request):
    return render(request, 'registration/index.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            phone = userObj['phone']
            location = userObj['location']
            state = userObj['state']
            gender = userObj['gender']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()) or UserProfile.objects.filter(phone_number=phone).exists():
                user1 = User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                UserProfile.objects.create(user_id = user1, phone_number = phone, location = location, gender = gender)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password or mobile number already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form' : form})


def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'registration/profile.html'
    return render(request, template, context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'