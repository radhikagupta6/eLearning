from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class SignupForm(UserCreationForm):
    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password')

    username = forms.CharField(max_length=20, help_text="")
    email = forms.EmailField()
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput, max_length=20, min_length=8)

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if len(username) < 5:
    #         print('hhh')
    #         raise ValidationError('There must be at least two valid inline items')
    #     return username

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('image', 'name', 'dob', 'gender', 'about', 'address')
    dob = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'rows': '2'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': '2'}))

    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
