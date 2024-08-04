from django.db import models
from django.contrib.auth.models import User

# Choices for ID types
ID_TYPES = [
    ('passport', 'Passport'),
    ('driving_license', 'Driving License'),
    ('national_id', 'National ID'),
    ('other', 'Other'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    alternative_phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    id_type = models.CharField(max_length=20, choices=ID_TYPES)
    id_image = models.ImageField(upload_to='user_use')
    health_issue = models.BooleanField(default=False)
    health_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'



class CMSPages(models.Model):
    page_title = models.CharField(max_length=45)
    page_description = models.CharField(max_length=255)

    def __str__(self):
        return self.page_title
    


class Transportation(models.Model):
    t_type = models.CharField(max_length=10)
    t_details = models.CharField(max_length=255)

    def __str__(self):
        return self.t_type



class Package(models.Model):
    p_name = models.CharField(max_length=45)
    p_image = models.ImageField(upload_to='admin_use')
    p_category = models.CharField(max_length=45)
    p_days = models.CharField(max_length=45,default="4 days & 5 Nights")  # Setting default value to 7
    p_description = models.TextField()

    def __str__(self):
        return self.p_name




class SubPackage(models.Model):
    subp_name = models.CharField(max_length=45)
    sub_p_image = models.ImageField(upload_to='admin_use')
    sub_p_description = models.CharField(max_length=255)
    start_from = models.CharField(max_length=45)
    end_place = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration_days = models.IntegerField()
    cost = models.CharField(max_length=100)
    cms_page = models.ForeignKey(CMSPages, on_delete=models.CASCADE)
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='subpackages')

    def __str__(self):
        return self.subp_name





class Member(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=10)
    subpackage = models.ForeignKey(SubPackage, on_delete=models.CASCADE, related_name='members')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.full_name




class CartItem(models.Model):
    no_of_members = models.CharField(max_length=45)
    cost = models.CharField(max_length=20)
    booking_status = models.CharField(max_length=20)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    subpackage = models.ForeignKey(SubPackage, on_delete=models.CASCADE, related_name='cart_items')
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart item for {self.user_profile}"




class Booking(models.Model):
    no_of_members = models.CharField(max_length=45)
    payment_method = models.CharField(max_length=20)
    booking_status = models.CharField(max_length=20)
    cost = models.CharField(max_length=20)
    total_cost = models.CharField(max_length=20)
    additional_booking_details = models.TextField(blank=True, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    subpackage = models.ForeignKey(SubPackage, on_delete=models.CASCADE, related_name='bookings')
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking for {self.user_profile}"
