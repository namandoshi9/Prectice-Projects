# accounts/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the home page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # Get the value of Remember Me checkbox
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember_me:  # If Remember Me is checked, set session expiry accordingly
                request.session.set_expiry(604800)  # Set session expiry to 7 days
            return redirect('product-list')  # Redirect to the product list page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')
