from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from crystal_admin.models import user, food, decoration, decoration_media, addon_services, order_items, order,event_details

from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def indexpage(request):
    return render(request, "index.html")


def contactus(request):
    return render(request, "contactus.html")


def details(request):
    return render(request, "details.html")


def welcompage(request):
    return render(request, "welcom.html")


def forgetpass(request):
    return render(request, "forgot-password.html")


def birthdaypage(request):
    cakedata = food.objects.filter(is_cake='yes')
    jainfood = food.objects.filter(is_jain_available='yes')
    nonvegfood = food.objects.filter(food_type='nonveg')
    vegfood = food.objects.filter(food_type='veg')
    themedata = decoration.objects.all()
    imagedata = decoration_media.objects.all()
    addon = addon_services.objects.all()

    context = {
        'cakedata': cakedata,
        'themedata': themedata,
        'imagedata': imagedata,
        'jainfood': jainfood,
        'nonvegfood': nonvegfood,
        'vegfood': vegfood,
        'addon': addon,
    }
    return render(request, "birthday.html", context)


def mylogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exists in database
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return redirect('login')

        if not username or not password:
            messages.error(request, 'Please enter a username and password')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == 1:
                response = render(request, 'user_table.html')
                response.set_cookie('user_type', 'staff_1')
                request.session['user_type'] = 'staff_1'
                return response
            elif user.is_staff == 1:
                response = render(request, 'em_dashboard.html')
                response.set_cookie('user_type', 'staff_2')
                request.session['user_type'] = 'staff_2'
                return response
            else:
                response = render(request, 'welcom.html')
                response.set_cookie('user_type', 'user')
                request.session['user_type'] = 'user'
                return response
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


# def mylogin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if not username or not password:
#             messages.error(request, 'Please enter a username and password')
#             return redirect('login')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request,user)
#             if user.is_staff==1:
#                 return render(request,'user_table.html')
#             elif user.is_staff==2:
#                 return render(request,'manager_table.html')
#             else:

#                 return render(request,'welcom.html')
#         else:
#             messages.error(request, 'Invalid username or password')
#             return redirect('login')
#     else:
#         return render(request, 'login.html')


def mylogout(request):
    logout(request)
    return redirect('welcom')


def register(request):
    if request.method == 'POST':
        username = request.POST['mobile_no']
        # email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassowrd']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']

        # Validate form data
        if not username:
            error_message = 'Please enter a username.'
            return render(request, 'create-account.html', {'error_message': error_message})
        elif not password:
            error_message = 'Please enter a password.'
            return render(request, 'create-account.html', {'error_message': error_message})
        elif password != confirm_password:
            error_message = 'Passwords do not match.'
            return render(request, 'create-account.html', {'error_message': error_message})
        else:
            if User.objects.filter(username=username).exists():
                error_message = 'User is alrady registerd.'
                return render(request, 'create-account.html', {'error_message': error_message})
            # Create new user
            my_user = User.objects.create_user(username=username, password=password)
            my_user.first_name = firstname
            my_user.last_name = lastname
            my_user.save()
            return redirect('login')

    else:
        return render(request, 'create-account.html')


# def orderdata(request):
#     from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from .models import food, decoration, addon_services, order, order_items

# @login_required
def orderdata(request):
    # Get the user who is creating the order
    user = request.user

    # Get the selected food items
    food_items = request.POST.getlist('food')

    # Get the selected decoration
    decoration_id = request.POST.get('theme')
    selected_decoration = decoration.objects.get(decoration_id=decoration_id)

    # Get the selected addon services
    addon_services_ids = request.POST.getlist('addon')
    selected_addon_services = addon_services.objects.filter(addon_services_id__in=addon_services_ids)

    # Calculate the total price
    food_items_prices = [food.objects.get(food_id=food_item_id).food_price for food_item_id in food_items]
    food_price = sum(food_items_prices)
    decoration_price = selected_decoration.decoration_price
    addon_service_charge = sum([addon_service.addon_service_price for addon_service in selected_addon_services])
    subtotal_price = food_price + decoration_price + addon_service_charge
    gst_rate = 0.28
    gst_amount = round(subtotal_price * gst_rate, 2)
    total_price = subtotal_price + gst_amount

    # Create the order object
    new_order = order.objects.create(
        order_status='New',
        customer_suggesion=request.POST.get('customer_suggestion'),
        price=food_price,
        subtotal=subtotal_price,
        decoration_price=decoration_price,
        addon_service_charge=addon_service_charge,
        cgst=gst_amount / 2,
        sgst=gst_amount / 2,
        total_price=total_price,
        decoration_id=selected_decoration,
        user_id=user
    )

    # Save the selected food items as order items
    for food_item_id in food_items:
        food_item = food.objects.get(food_id=food_item_id)
        order_items.objects.create(
            food_item_name=food_item.food_name,
            food_price=food_item.food_price,
            food_type=food_item.food_type,
            food_id=food_item,
            order_id=new_order
        )

    # Save the selected addon services as order items
    for addon_service in selected_addon_services:
        order_items.objects.create(
            addon_name=addon_service.addon_service_name,
            addon_price=addon_service.addon_service_price,
            order_id=new_order
        )

    # Redirect the user to the order details page
    return redirect('invoice', order_id=new_order.order_id)


def invoice(request, order_id):
    # Get the order object from the database
    order_obj = get_object_or_404(order, order_id=order_id)

    # Render the invoice template with the order object
    context = {'order': order_obj}
    return render(request, 'invoice.html', context)


def ddata(request):
    if request.method == 'POST':
        edate = request.POST['date']
        ecity = request.POST['ecity']
        eloc = request.POST['eloc']
        eguests = request.POST['guests']
        ebudget = request.POST['budget']
        ets = request.POST['ts']

        umail = request.POST['email']
        ugen = request.POST['gen']
        ubod = request.POST['udate']
        uno = request.POST['no']
        ucity = request.POST['ucity']
        uadd = request.POST['add']

        edata = event_details.objects.create(event_date=edate, event_city=ecity, event_address=eloc,
                                             no_of_guest=eguests, event_budget=ebudget, event_timeslot=ets)
        pdata = user.objects.create(email=umail, gender=ugen, date_of_birth=ubod, city=ucity, user_address=uadd)
        edata.save()
        pdata.save()

    return render(request, 'bookingdetails.html')


def bdetails(request):
    return render(request, 'bookingdetails.html')