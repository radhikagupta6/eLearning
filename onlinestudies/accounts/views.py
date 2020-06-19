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
