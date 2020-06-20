from django.shortcuts import render, redirect

# Create your views here.
from .forms import LoginForm

users = {'email': 'a@gmail.com', 'pass': '1234', 'username': 'Ram'}


def login_view(request):
    if request.session.get('uemail'):
        return redirect("dashboard")
    errr = ""
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        print(email, password)
        if users['email'] == email and users['pass'] == password:
            print("Login Successful")
            request.session['uemail'] = email
            return redirect('dashboard')
        else:
            errr = 'Email or Password is Incorrect !'

    context = {
        'form': form,
        'errr': errr
    }
    return render(request, 'accounts/login.html', context)


def dashboard(request):
    if not request.session.get('uemail'):
        return redirect('login')
    context = dict()
    uemail = request.session.get('uemail')
    print(uemail)
    context = {
        'uemail': uemail
    }
    return render(request, 'accounts/dashboard.html', context)


def logout_view(request):
    del request.session['uemail']
    return redirect('login')


from .forms import SignupForm
from django.contrib.auth.models import User


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        print(username, email, password)
        user = User.objects.create_user(username=username, password=password, email=email)
        if user:
            print(user)
            user.first_name = "unknown"
            user.save()
        else:
            print("something error")
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
