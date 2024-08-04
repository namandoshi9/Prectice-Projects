import sys
from multiprocessing import connection

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
# from mysqlx import View
# from rest_framework.response import Response
# from rest_framework.views import APIView

from crystal_admin.forms import userForm, managerForm, eventForm, foodForm, decorationForm, addon_servicesForm, \
    bank_detailsForm, event_detailsForm, food_imagesForm, orderForm, order_itemsForm, paymentForm, decoration_mediaForm, \
    feedbackForm
from crystal_admin.models import user, manager, event, food, decoration, addon_services, bank_details, event_details, \
    food_images, order, order_items, payment, feedback


def User_show(request):
    use = user.objects.all()
    return render(request, "user_table.html", {'use': use})


def Manager_show(request):
    man = manager.objects.all()
    return render(request, "manager_table.html", {'man': man})


def Event_show(request):
    eve = event.objects.all()
    return render(request, "event_table.html", {'eve': eve})


def Food_show(request):
    fod = food.objects.all()
    return render(request, "food_table.html", {'fod': fod})


def Decoration_show(request):
    dec = decoration.objects.all()
    return render(request, "decoration_table.html", {'dec': dec})


def AddServices_show(request):
    add = addon_services.objects.all()
    return render(request, "addservices_table.html", {'add': add})


def BankDetails_show(request):
    ban = bank_details.objects.all()
    return render(request, "bankdetails_table.html", {'ban': ban})


def EventDetails_show(request):
    evd = event_details.objects.all()
    return render(request, "eventdetails_table.html", {'evd': evd})


def food_images_show(request):
    fimg = food_images.objects.all()
    return render(request, "foodimages_table.html", {'fimg': fimg})


def order_show(request):
    ord = order.objects.all()
    return render(request, "order_table.html", {'ord': ord})


def OrderItems_show(request):
    oitem = order_items.objects.all()
    return render(request, "orderitems_table.html", {'oitem': oitem})


def Payment_show(request):
    pay = payment.objects.all()
    return render(request, "payment_table.html", {'pay': pay})


def Feedback_show(request):
    fed = feedback.objects.all()
    return render(request, "feedback_table.html", {'fed': fed})


def delete_user(request, id):
    print("==========", id)
    crystal_admin = user.objects.get(user_id=id)
    crystal_admin.delete()
    return redirect("/admin/user_show")


def delete_manager(request, id):
    print("==========", id)
    crystal_admin = manager.objects.get(manager_id=id)
    crystal_admin.delete()
    return redirect("/admin/manager_show")


def delete_event(request, id):
    print("==========", id)
    crystal_admin = event.objects.get(event_id=id)
    crystal_admin.delete()
    return redirect("/admin/event_show")


def delete_food(request, id):
    print("==========", id)
    crystal_admin = food.objects.get(food_id=id)
    crystal_admin.delete()
    return redirect("/admin/food_show")


def delete_decoration(request, id):
    print("==========", id)
    crystal_admin = decoration.objects.get(decoration_id=id)
    crystal_admin.delete()
    return redirect("/admin/decoration_show")


def delete_addservices(request, id):
    print("==========", id)
    crystal_admin = addon_services.objects.get(addon_services_id=id)
    crystal_admin.delete()
    return redirect("/admin/addServices_show")


def delete_bankdetails(request, id):
    print("==========", id)
    crystal_admin = bank_details.objects.get(bank_details_id=id)
    crystal_admin.delete()
    return redirect("/admin/bankdetails_show")


def delete_eventdetails(request, id):
    print("==========", id)
    crystal_admin = event_details.objects.get(event_details=id)
    crystal_admin.delete()
    return redirect("/admin/eventdetails_show")


def delete_foodimage(request, id):
    print("==========", id)
    crystal_admin = food_images.objects.get(food_images_id=id)
    crystal_admin.delete()
    return redirect("/admin/foodimages_show")


def delete_order(request, id):
    print("==========", id)
    crystal_admin = order.objects.get(order_id=id)
    crystal_admin.delete()
    return redirect("/admin/order_show")


def delete_orderitems(request, id):
    print("==========", id)
    crystal_admin = order_items.objects.get(order_items_id=id)
    crystal_admin.delete()
    return redirect("/admin/orderitems_show")


def delete_payment(request, id):
    print("==========", id)
    crystal_admin = payment.objects.get(payment_id=id)
    crystal_admin.delete()
    return redirect("/admin/payment")


def delete_feedback(request, id):
    print("==========", id)
    crystal_admin = feedback.objects.get(feedback_id=id)
    crystal_admin.delete()
    return redirect("/admin/feedback_show")


def insert_user(request):
    if request.method == "POST":
        form = userForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/user_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = userForm()

    return render(request, 'user_insert.html', {'form': form})


def insert_manager(request):
    if request.method == "POST":
        form = managerForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                new_manager = form.save()
                # Create a new user object with the manager's email and password
                user = User.objects.create_user(username=new_manager.manager_name,email=new_manager.manager_email,password=new_manager.manager_password)

                # Add the user as an authenticated user
                user.is_staff = True
                user.save()

                # Set the manager's user_id field to the new user object
                new_manager.user_id = user
                new_manager.save()
                return redirect('/admin/manager_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = managerForm()

    return render(request, 'manager_insert.html', {'form': form})


def insert_event(request):
    if request.method == "POST":
        form = eventForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/event_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = eventForm()

    return render(request, 'event_insert.html', {'form': form})


def insert_food(request):
    if request.method == "POST":
        form = foodForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/food_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = foodForm()

    return render(request, 'food_insert.html', {'form': form})


def insert_decoration(request):
    if request.method == "POST":
        form = decorationForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/decoration_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = decorationForm()

    return render(request, 'decoration_insert.html', {'form': form})


def insert_addon_services(request):
    if request.method == "POST":
        form = addon_servicesForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/addServices_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = addon_servicesForm()

    return render(request, 'addon_services_insert.html', {'form': form})


def insert_bank_details(request):
    User = user.objects.all()
    if request.method == "POST":
        form = bank_detailsForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/bankdetails_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = bank_detailsForm()

    return render(request, 'bank_details_insert.html', {'form': form, "User": User})


def insert_event_details(request):
    Event = event.objects.all()
    User = user.objects.all()
    Manager = manager.objects.all()
    if request.method == "POST":
        form = event_detailsForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/eventdetails_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = event_detailsForm()

    return render(request, 'event_details_insert.html',
                  {'form': form, "Event": Event, "User": User, "Manager": Manager})


def insert_food_images(request):
    Food = food.objects.all()
    if request.method == "POST":
        form = food_imagesForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/foodimages_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = food_imagesForm()

    return render(request, 'food_images_insert.html', {'form': form, "Food": Food})


def insert_order(request):
    Decoration = decoration.objects.all()
    Event = event.objects.all()
    User = user.objects.all()
    Manager = manager.objects.all()
    if request.method == "POST":
        form = orderForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/order_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = orderForm()

    return render(request, 'order_insert.html',
                  {'form': form, "Decoration": Decoration, "Event": Event, "User": User, "Manager": Manager})


def insert_order_items(request):
    Order = order.objects.all()
    Food = food.objects.all()
    Event = event.objects.all()
    if request.method == "POST":
        form = order_itemsForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/orderitems_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = order_itemsForm()

    return render(request, 'insert_order_items.html', {'form': form, "Order": Order, "Food": Food, "Event": Event})


def insert_payment(request):
    Order = order.objects.all()

    if request.method == "POST":
        form = paymentForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/payment_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = paymentForm()

    return render(request, 'insert_payment.html', {'form': form, "Order": Order})


# def insert_decoration_media(request):
#     Decoration = decoration.objects.all()
#     if request.method == "POST":
#         form = decoration_mediaForm(request.POST)
#         print("-------------", form.errors)
#
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/decoration_media_show')
#             except:
#                 print("---------------", sys.exc_info())
#     else:
#         form = decoration_mediaForm()
#
#     return render(request, 'decoration_media_insert.html', {'form': form,"Decoration":Decoration})


def insert_feedback(request):
    Order = order.objects.all()
    User = user.objects.all()
    if request.method == "POST":
        form = feedbackForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/feedback_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = feedbackForm()

    return render(request, 'feedback_insert.html', {'form': form, "User": User, "Order": Order})


# -----------------update---------------
# ------------------user---------------------
def select_user(request, id):
    us = user.objects.get(user_id=id)
    return render(request, 'update_user.html', {'user': us})


def update_user(request, id):
    us = user.objects.get(user_id=id)
    form = userForm(request.POST, instance=us)
    if form.is_valid():
        form.save()
        return redirect("/admin/user_show")
    return render(request, 'update_user.html', {'user': us})


# ------------------manager---------------------
def select_manager(request, id):
    mg = manager.objects.get(manager_id=id)
    return render(request, 'update_manager.html', {'manager': mg})


def update_manager(request, id):
    mg = manager.objects.get(manager_id=id)
    form = managerForm(request.POST, instance=mg)
    if form.is_valid():
        form.save()
        return redirect("/admin/manager_show")
    return render(request, 'update_manager.html', {'manager': mg})


# --------------------event-----------------------------
def select_event(request, id):
    ev = event.objects.get(event_id=id)
    return render(request, 'update_manager.html', {'event': ev})


def update_event(request, id):
    ev = event.objects.get(event_id=id)
    form = eventForm(request.POST, instance=ev)
    if form.is_valid():
        form.save()
        return redirect("/admin/event_show")
    return render(request, 'update_event.html', {'event': ev})

# -------------------------food--------------------------
def select_food(request, id):
    fd = food.objects.get(food_id=id)
    return render(request, 'update_food.html', {'food': fd})


def update_food(request, id):
    fd = food.objects.get(food_id=id)
    form = foodForm(request.POST, instance=fd)
    if form.is_valid():
        form.save()
        return redirect("/admin/food_show")
    return render(request, 'update_food.html', {'food': fd})


# ---------------------------decoration-----------------------------

def select_decoration(request, id):
    dc = decoration.objects.get(decoration_id=id)
    return render(request, 'update_decoration.html', {'decoration': dc})


def update_decoration(request, id):
    dc = decoration.objects.get(decoration_id=id)
    form = decorationForm(request.POST, instance=dc)
    if form.is_valid():
        form.save()
        return redirect("/admin/decoration_show")
    return render(request, 'update_decoration.html', {'decoration': dc})


# --------------------------addon_services--------------------------------------

def select_addon_services(request, id):
    aos = addon_services.objects.get(addon_services_id=id)
    return render(request, 'update_addon_services.html', {'addon_services': aos})


def update_addon_services(request, id):
    aos = addon_services.objects.get(addon_services_id=id)
    form = addon_servicesForm(request.POST, instance=aos)
    if form.is_valid():
        form.save()
        return redirect("/admin/addServices_show")
    return render(request, 'update_addon_services.html', {'addon_services': aos})


# ----------------------------bank_details----------------------------------

def select_bank_details(request, id):
    bd = bank_details.objects.get(bank_details_id=id)
    return render(request, 'update_bank_details.html', {'bank_details': bd})


def update_bank_details(request, id):
    User = user.objects.all()
    bd = bank_details.objects.get(bank_details_id=id)
    form = bank_detailsForm(request.POST, instance=bd)
    if form.is_valid():
        form.save()
        return redirect("/admin/bankdetails_show")
    return render(request, 'update_bank_details.html', {'bank_details': bd, 'User': User})


# -------------------------------event_details-----------------------------------
def select_event_details(request, id):
    evd = event_details.objects.get(event_details_id=id)
    return render(request, 'update_eventdetails_details.html', {'bank_details': evd})


def update_event_details(request, id):
    Event = event.objects.all()
    User = user.objects.all()
    Manager = manager.objects.all()
    evd = event_details.objects.get(event_details_id=id)
    form = event_detailsForm(request.POST, instance=evd)
    if form.is_valid():
        form.save()
        return redirect("/admin/eventdetails_show")
    return render(request, 'update_eventdetails_details.html',
                  {'event_details': evd, 'Event': Event, 'User': User, 'Manager': Manager})


# ------------------------food_images--------------------------
def select_food_images(request, id):
    fi = food_images.objects.get(food_images_id=id)
    return render(request, 'update_food_images.html', {'food_images': fi})


def update_food_images(request, id):
    Food = food.objects.all()
    fi = food_images.objects.get(food_images_id=id)
    form = food_imagesForm(request.POST, instance=fi)
    if form.is_valid():
        form.save()
        return redirect("/admin/foodimages_show")
    return render(request, 'update_food_images.html', {'food_images': fi, 'Food': Food})


# -----------------------order--------------------------
def select_order(request, id):
    odr = order.objects.get(order_id=id)
    return render(request, 'update_food_images.html', {'order': odr})


def update_order(request, id):
    Decoration = decoration.objects.all()
    Event = event.objects.all()
    User = user.objects.all()
    Manager = manager.objects.all()
    odr = order.objects.get(order_id=id)
    form = orderForm(request.POST, instance=odr)
    if form.is_valid():
        form.save()
        return redirect("/admin/order_show")
    return render(request, 'update_order.html',
                  {'order': odr, "Decoration": Decoration, "Event": Event, "User": User, "Manager": Manager})


# --------------------------order_items------------------------
def select_order_items(request, id):
    ordi = order_items.objects.get(order_items_id=id)
    return render(request, 'update_order_items.html', {'order_items': ordi})


def update_order_items(request, id):
    Food = food.objects.all()
    Order = order.objects.all()
    Event = event.objects.all()
    ordi = order_items.objects.get(order_items_id=id)
    form = order_itemsForm(request.POST, instance=ordi)
    if form.is_valid():
        form.save()
        return redirect("/admin/orderitems_show")
    return render(request, 'update_order_items.html',
                  {'order_items': ordi, "Event": Event, "Food": Food, "Order": Order})


# -------------------------payment-------------------------
def select_payment(request, id):
    pay = payment.objects.get(payment_id=id)
    return render(request, 'update_payment.html', {'payment': pay})


def update_payment(request, id):
    Order = order.objects.all()
    pay = payment.objects.get(payment_id=id)
    form = paymentForm(request.POST, instance=pay)
    if form.is_valid():
        form.save()
        return redirect("/admin/payment_show")
    return render(request, 'update_payment.html', {'payment': pay, 'Order': Order})


# ---------------------------feedback-----------------------
def select_feedback(request, id):
    fed = payment.objects.get(feedback_id=id)
    return render(request, 'update_feedback.html', {'feedback': fed})


def update_feedback(request, id):
    User = user.objects.all()
    Order = order.objects.all()
    fed = feedback.objects.get(feedback_id=id)
    form = feedbackForm(request.POST, instance=fed)
    if form.is_valid():
        form.save()
        return redirect("/admin/feedback_show")
    return render(request, 'update_feedback.html', {'feedback': fed, 'Order': Order, "User": User})

def dashboard(request):
    d = user.objects.all().count()
    b = manager.objects.all().count()
    r = event.objects.all().count()
    a = order.objects.all().count()

    return render(request, "dashboard.html",{'user':d, 'manager':b, 'event':r, 'order':a })


