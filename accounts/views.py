from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import SignUpForm, SignInForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

User = get_user_model()

# Create your views here.

def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Sucessful!')
            return redirect('signin')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):

    if request.method == "POST":
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()

            login(request, user)
            messages.success(request, 'Login Sucessful!')
            return redirect('home')

    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('home')