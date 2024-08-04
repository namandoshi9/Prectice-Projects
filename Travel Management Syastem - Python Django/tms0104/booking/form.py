from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control p-4', 'placeholder': 'Password', 'required': 'required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control p-4', 'placeholder': 'Confirm Password', 'required': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'Username', 'required': 'required'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'First name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'Last name', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control p-4', 'placeholder': 'Email', 'required': 'required'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'Username', 'required': 'required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control p-4', 'placeholder': 'Password', 'required': 'required'}))
    

