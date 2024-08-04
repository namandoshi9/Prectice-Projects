from django import forms
from crystal_admin.models import user, manager, event, food, decoration, addon_services, bank_details, decoration_media, \
    feedback, order_items, event_details, food_images, order, payment, contact


class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ["f_name", "l_name", "email", "mobile_no", "date_of_birth", "gender", "city", "user_address",
                  "password", "user_type", "mobile_verified", "user_status"]


class managerForm(forms.ModelForm):
    class Meta:
        model = manager
        fields = ["manager_name", "manager_address", "manager_email", "manager_password"]


class eventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ["event_name", "event_status"]


class foodForm(forms.ModelForm):
    class Meta:
        model = food
        fields = ["food_type", "food_name", "is_jain_available", "is_cake", "food_price", "food_qty", "food_images_url"]


class decorationForm(forms.ModelForm):
    class Meta:
        model = decoration
        fields = ["decoration_price", "decoration_theam", "decoration_details", "decoration_images_url"]


class addon_servicesForm(forms.ModelForm):
    class Meta:
        model = addon_services
        fields = ["addon_service_name", "addon_service_price", "addon_images_url"]


class bank_detailsForm(forms.ModelForm):
    class Meta:
        model = bank_details
        fields = ["agent_bank_name", "agent_account_no", "agent_ifcs_no", "user_id"]


class event_detailsForm(forms.ModelForm):
    class Meta:
        model = event_details
        fields = ["event_date", "no_of_guest", "event_city", "event_address", "event_status", "event_timeslot",
                  "food_inclueded", "food_type", "user_id", "event_id", "manager_id"]


class food_imagesForm(forms.ModelForm):
    class Meta:
        model = food_images
        fields = ["food_images_url", "food_id"]


class orderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ["order_status", "customer_suggesion", "price", "decoration_price", "addon_service_charge", "cgst",
                  "sgst", "total_price", "decoration_id", "user_id", "manager_id", "event_id"]


class order_itemsForm(forms.ModelForm):
    class Meta:
        model = order_items
        fields = ["food_item_name", "food_price", "decoration_theam", "decoration_price", "food_type", "suggestion",
                  "addon_name", "addon_price", "food_id", "order_id", "event_id"]


class paymentForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = ["amount", "payment_type", "transaction_id", "order_id"]


class decoration_mediaForm(forms.ModelForm):
    class Meta:
        model = decoration_media
        fields = ["decoration_media_url", "decoration_id"]


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ["name", "email", "msg"]


class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ["rating", "suggestion", "user_id", "order_id"]
