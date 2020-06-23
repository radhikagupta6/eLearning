from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from .forms import LoginForm

users = {'email': 'a@gmail.com', 'pass': '1234', 'username': 'Ram'}


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(username, password)
        # if users['email'] == email and users['pass'] == password:
        #     print("Login Successful")
        #     request.session['uemail'] = email
        user = authenticate(request, username= username, password=password)
        if user:
            login(request, user)  # this also creates the session
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.INFO, 'Username or password incorrect')

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = dict()
    return render(request, 'accounts/dashboard.html', context)


def logout_view(request):
    logout(request)
    # del request.session['uemail']
    return redirect('login')


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        print(username, email, password)
        user = User.objects.create_user(username=username, password=password, email=email)
        if user:

            user.first_name = "unknown"
            user.save()
            login(request, user)
            messages.add_message(request, messages.INFO, f'User {username} Created Successfully')
        else:
            print("something error")
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
