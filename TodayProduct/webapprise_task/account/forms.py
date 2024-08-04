# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    fullname = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'address', 'fullname', 'password1', 'password2')
