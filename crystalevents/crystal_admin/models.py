from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=20, null=False)
    l_name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=True)
    mobile_no = models.CharField(max_length=11, null=False)
    amobile_no = models.CharField(max_length=11, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=6, null=True)
    city = models.CharField(max_length=10, null=True)
    user_address = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=20, null=False)
    user_type = models.IntegerField(default=1)
    mobile_verified = models.CharField(max_length=10, null=True)
    user_status = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"


class manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    manager_name = models.CharField(max_length=20, null=True)
    manager_address = models.CharField(max_length=200, null=True)
    manager_email = models.CharField(max_length=20, null=False)
    manager_password = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = "manager"


class event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=20, null=True)
    event_status = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "event"


class food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_type = models.CharField(max_length=10, null=True)
    food_name = models.CharField(max_length=100, null=True)
    is_jain_available = models.CharField(max_length=20, null=True)
    is_cake = models.CharField(max_length=10, null=True)
    food_price = models.FloatField()
    food_qty = models.IntegerField()
    food_images_url = models.CharField(max_length=200, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "food"


class decoration(models.Model):
    decoration_id = models.AutoField(primary_key=True)
    decoration_price = models.FloatField(null=True)
    decoration_theam = models.CharField(max_length=10, null=True)
    decoration_details = models.CharField(max_length=100, null=True)
    decoration_images_url = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "decoration"


class addon_services(models.Model):
    addon_services_id = models.AutoField(primary_key=True)
    addon_service_name = models.CharField(max_length=100, null=True)
    addon_service_price = models.FloatField(null=True)
    addon_images_url = models.CharField(max_length=200, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "addon_services"


class bank_details(models.Model):
    bank_details_id = models.AutoField(primary_key=True)
    agent_bank_name = models.CharField(max_length=20, null=False)
    agent_account_no = models.IntegerField(null=False)
    agent_ifcs_no = models.CharField(max_length=10, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "bank_details"


class event_details(models.Model):
    event_details_id = models.AutoField(primary_key=True)
    event_date = models.DateTimeField()
    no_of_guest = models.IntegerField(null=False)
    event_city = models.CharField(max_length=10, null=False)
    event_address = models.CharField(max_length=200, null=False)
    event_status = models.CharField(max_length=20)
    event_timeslot = models.CharField(max_length=20, null=True)
    food_inclueded = models.CharField(max_length=100, default="no", null=False)
    food_type = models.CharField(max_length=10, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_id = models.ForeignKey(event, on_delete=models.CASCADE, null=True)
    manager_id = models.ForeignKey(manager, on_delete=models.CASCADE, null=True,blank=True)

    class Meta:
        db_table = "event_details"


class food_images(models.Model):
    food_images_id = models.AutoField(primary_key=True)
    food_images_url = models.CharField(max_length=200, null=True)
    food_id = models.ForeignKey(food, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "food_images"


class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_status = models.CharField(max_length=20)
    customer_suggesion = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    decoration_price = models.FloatField()
    addon_service_charge = models.FloatField()
    subtotal = models.FloatField(null=True)
    cgst = models.FloatField()
    sgst = models.FloatField()
    total_price = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    decoration_id = models.ForeignKey(decoration, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    manager_id = models.ForeignKey(manager, on_delete=models.CASCADE, null=True,blank=True)
    event_id = models.ForeignKey(event, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "order"


class order_items(models.Model):
    order_items_id = models.AutoField(primary_key=True)
    food_item_name = models.CharField(max_length=30, null=True)
    food_price = models.FloatField(null=True)
    decoration_theam = models.CharField(max_length=30, null=True)
    decoration_price = models.FloatField(null=True)
    food_type = models.CharField(max_length=10)
    suggestion = models.CharField(max_length=100, null=True)
    addon_name = models.CharField(max_length=20, null=True)
    addon_price = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    food_id = models.ForeignKey(food, on_delete=models.CASCADE, null=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE, null=True)
    event_id = models.ForeignKey(event, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "order_items"


class payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    payment_type = models.CharField(max_length=10, null=False)
    transaction_id = models.CharField(max_length=50, null=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "payment"


class decoration_media(models.Model):
    decoration_media_id = models.AutoField(primary_key=True)
    decoration_media_url = models.CharField(max_length=200)
    decoration_id = models.ForeignKey(decoration, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "decoration_media"


class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)
    msg = models.CharField(max_length=200, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "contact"


class feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    rating = models.IntegerField(null=True)
    suggestion = models.CharField(max_length=200, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "feedback"


class agent_commission(models.Model):
    agent_commission_id = models.AutoField(primary_key=True)
    bank_details_id = models.ForeignKey(bank_details, on_delete=models.CASCADE, default="", null=True)
    transaction_id = models.CharField(max_length=50, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=3)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "agent_commission"


class order_services(models.Model):
    order_services_id = models.AutoField(primary_key=True)
    order_service_price = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE, null=True)
    addon_services_id = models.ForeignKey(addon_services, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "order_services"
