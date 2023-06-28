from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect

import authentication

# Create your views here.


def index(request):
    return render(request, 'authentication/index.html', context={
        'User' : User
    })


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
    if user is not None:
        return render(request, 'authentication/welcome.html', context={
        'User' : User
    })
    else:
        return render(request, 'authentication/index.html')

def logout(request):
    auth.logout(request)
    print(dir(auth))
    return redirect('index')