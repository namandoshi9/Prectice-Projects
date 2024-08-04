from xml.etree.ElementInclude import include

from django.contrib import admin

from django.urls import path

from . import em_views

urlpatterns = [
    path('event_show/', em_views.Event_show),
    path('eventdetails_show/', em_views.EventDetails_show),
    path('food_show/', em_views.Food_show),
    path('decoration_show/', em_views.Decoration_show),
    path('payment_show/', em_views.Payment_show),

    path('delete_eventdetails/<int:id>', em_views.delete_eventdetails),
    path('delete_food/<int:id>', em_views.delete_food),
    path('delete_decoration/<int:id>', em_views.delete_decoration),
    path('delete_payment/<int:id>', em_views.delete_payment),

    path('insert_event_details/', em_views.insert_event_details),
    path('insert_food/', em_views.insert_food),
    path('insert_decoration/', em_views.insert_decoration),
    path('insert_payment/', em_views.insert_payment),

    path('update_food/<int:id>', em_views.update_food),
    path('update_decoration/<int:id>', em_views.update_decoration),
    path('update_event_details/<int:id>', em_views.update_event_details),
    path('update_payment/<int:id>', em_views.update_payment),

    path('dashboard/', em_views.dashboard),
]
