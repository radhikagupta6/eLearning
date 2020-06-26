from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import StudentProfile
# Create your views here.
from .forms import LoginForm

users = {'email': 'a@gmail.com', 'pass': '1234', 'username': 'Ram'}


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.INFO, f'Your :{username} or password  Invalid !')

    context = {
        "form": form,
    }
    return render(request, 'accounts/login.html', context)


def dashboard(request):
    context = dict()
    if not request.user.is_authenticated:
        return redirect('login')
    print(request.user)
    student = StudentProfile.objects.get(user= request.user)
    context['student'] = student
    return render(request, 'accounts/dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')
    form = SignupForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        print(username, email, password)

        user = User.objects.create_user(username=username, email=email, password=password)
        if user:
            # user.first_name="Your_First_Name"
            # user.last_name="Your_Last_Name"
            # user.save()
            login(request, user)
            messages.add_message(request, messages.INFO, f' {username} Created Successfully')
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.INFO, f' {username} Not Created !')

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
