"""
URL configuration for tms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from booking import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.register, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.user_logout, name='logout'),

    path('tripDetails/',views.tripDetails, name='tripDetails'),
    path('abouUs/',views.abouUs, name='abouUs'),
    path('ServiceView/',views.ServiceView, name='ServiceView'),
    path('ContectUs/',views.ContectUs, name='ContectUs'),
    path('Packges_view/',views.Packges_view, name='Packges_view'),
    path('destination_view/',views.destination_view, name='destination_view'),
    


    path('booking_detail_view', views.booking_detail_view, name='booking_detail_view'),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
