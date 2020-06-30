from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm

from django.contrib.auth.models import User
from django.contrib import messages
from .models import StudentProfile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
from .forms import LoginForm, StudentProfileForm


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
    student = StudentProfile.objects.get(user=request.user)
    context['student'] = student
    return render(request, 'accounts/dashboard.html', context)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
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


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    student = StudentProfile.objects.get(user=request.user)
    context = {
        'student': student
    }
    return render(request, 'accounts/profile.html', context)


def profile_edit(request):
    if not request.user.is_authenticated:
        return redirect('login')
    student = StudentProfile.objects.get(user=request.user)
    form = StudentProfileForm(request.POST or None,  request.FILES or None, instance= student)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, f' Updated Successfully !')
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'accounts/edit_profile.html', context)


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
