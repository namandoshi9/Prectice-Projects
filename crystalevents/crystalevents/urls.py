"""crystalevents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from crystal_client import views


urlpatterns = [
    #crystal admin
    path("admin/", include("crystal_admin.urls")),
    #crystal Manager
    path("em/",include("crystal_manager.em_urls")),
    #crystal user
    path("", include("crystal_client.urls")),
    path("welcom/", views.welcompage, name='welcom'),
    path("", views.welcompage, name='welcom'),
    path("birthday/", views.birthdaypage, name='birthday'),
    path("register/", views.register, name='register'),
    path("login/", views.mylogin, name='login'),
    path("logout/", views.mylogout, name='logout'),  
    path("forgetpass/", views.forgetpass, name='forgetpass'),
    path("contactus/", views.contactus, name='contactus'),
  
]
