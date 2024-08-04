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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from crystal_admin import views
from crystal_manager import em_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('user_show/', views.User_show),
    path('manager_show/', views.Manager_show),
    path('event_show/', views.Event_show),
    path('food_show/', views.Food_show),
    path('decoration_show/', views.Decoration_show),
    path('addServices_show/', views.AddServices_show),
    path('bankdetails_show/', views.BankDetails_show),
    path('eventdetails_show/', views.EventDetails_show),
    path('foodimages_show/', views.food_images_show),
    path('order_show/', views.order_show),
    path('orderitems_show/', views.OrderItems_show),
    path('payment_show/', views.Payment_show),
    path('feedback_show/', views.Feedback_show),

    path('delete_user/<int:id>', views.delete_user),
    path('delete_manager/<int:id>', views.delete_manager),
    path('delete_event/<int:id>', views.delete_event),
    path('delete_food/<int:id>', views.delete_food),
    path('delete_decoration/<int:id>', views.delete_decoration),
    path('delete_addservices/<int:id>', views.delete_addservices),
    path('delete_bankdetails/<int:id>', views.delete_bankdetails),
    path('delete_eventdetails/<int:id>', views.delete_eventdetails),
    path('delete_foodimage/<int:id>', views.delete_foodimage),
    path('delete_order/<int:id>', views.delete_order),
    path('delete_orderitems/<int:id>', views.delete_orderitems),
    path('delete_payment/<int:id>', views.delete_payment),
    path('delete_feedback/<int:id>', views.delete_feedback),

    path('insert_user/',views.insert_user),
    path('insert_manager/',views.insert_manager),
    path('insert_event/', views.insert_event),
    path('insert_food/', views.insert_food),
    path('insert_decoration/', views.insert_decoration),
    path('insert_addon_services/', views.insert_addon_services),
    path('insert_bank_details/', views.insert_bank_details),
    path('insert_event_details/', views.insert_event_details),
    path('insert_food_images/', views.insert_food_images),
    path('insert_order/', views.insert_order),
    path('insert_order_items/', views.insert_order_items),
    path('insert_payment/', views.insert_payment),
    path('insert_feedback/', views.insert_feedback),

    path('update_user/<int:id>', views.update_user),
    path('update_manager/<int:id>', views.update_manager),
    path('update_event/<int:id>', views.update_event),
    path('update_food/<int:id>', views.update_food),
    path('update_decoration/<int:id>', views.update_decoration),
    path('update_addon_services/<int:id>', views.update_addon_services),
    path('update_bank_details/<int:id>', views.update_bank_details),
    path('update_event_details/<int:id>', views.update_event_details),
    path('update_food_images/<int:id>', views.update_food_images),
    path('update_order/<int:id>', views.update_order),
    path('update_order_items/<int:id>', views.update_order_items),
    path('update_payment/<int:id>', views.update_payment),
    path('update_feedback/<int:id>', views.update_feedback),

    path('dashboard/',views.dashboard),

   # path('em/',include('crystal_manager.em_urls')),
    # path('Manager_Event_show/', em_views.Event_show),
]
