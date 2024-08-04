from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .form import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def tripDetails(request):
    return render(request, 'trip&packgeDetails.html')


def abouUs(request):
    return render(request,'about.html')


def ServiceView(request):
    return render(request,'service.html')


def ContectUs(request):
    return render(request,'contact.html')


def Packges_view(request):
    packages = Package.objects.all()
    return render(request,'package.html',{'packages':packages})


def destination_view(request):
    # destinations = Destination.objects.all()
    return render(request,'destination.html')



def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            user = User.objects.filter(email=user_email).first()
            if user:
                # Generate a password reset token
                token_generator = default_token_generator
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = token_generator.make_token(user)

                # Build password reset email
                subject = 'Password Reset'
                message = render_to_string('password_reset_email.html', {
                    'user': user,
                    'domain': request.get_host(),
                    'uid': uid,
                    'token': token,
                })
                send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])

                return render(request, 'password_reset_done.html')
            else:
                # User does not exist with the provided email
                messages.error(request, 'User with this email does not exist.')
    else:
        form = PasswordResetForm()
    return render(request, 'forgot_password.html', {'form': form})


@login_required
def booking_detail_view(request):
    # Fetch bookings for the logged-in user
    user = request.user
    bookings_exist = Booking.objects.filter(user_profile__user=user).exists()
    if bookings_exist:
        bookings = Booking.objects.filter(user_profile__user=user)
        return render(request, 'booking.html', {'bookings': bookings})
    else:
        message = "You have no bookings."
        return render(request, 'booking.html', {'message': message})
    



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


@csrf_protect
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            response = redirect('index')
            response.set_cookie('username', user.username)
            return response
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'signin.html')

def user_logout(request):
    logout(request)
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'username' in request.session:
        del request.session['username']
    response = redirect('index')
    response.delete_cookie('username')
    return response

