import sys

from django.shortcuts import render, redirect

# Create your views here.
from crystal_admin.forms import event_detailsForm, foodForm, decorationForm, paymentForm
from crystal_admin.models import event, event_details, food, decoration, payment, user, manager, order


def Event_show(request):
    eve = event.objects.all()
    return render(request, "em_event_table.html", {'eve': eve})


def EventDetails_show(request):
    evd = event_details.objects.all()
    return render(request, "em_eventdetails_table.html", {'evd': evd})


def Food_show(request):
    fod = food.objects.all()
    return render(request, "em_food_table.html", {'fod': fod})


def Decoration_show(request):
    dec = decoration.objects.all()
    return render(request, "em_decoration_table.html", {'dec': dec})


def Payment_show(request):
    pay = payment.objects.all()
    return render(request, "em_payment_table.html", {'pay': pay})


def delete_eventdetails(request, id):
    print("==========", id)
    crystal_admin = event_details.objects.get(event_details_id=id)
    crystal_admin.delete()
    return redirect("/em/eventdetails_show")


def delete_food(request, id):
    print("==========", id)
    crystal_admin = food.objects.get(food_id=id)
    crystal_admin.delete()
    return redirect("/em/food_show")


def delete_decoration(request, id):
    print("==========", id)
    crystal_admin = decoration.objects.get(decoration_id=id)
    crystal_admin.delete()
    return redirect("/em/decoration_show")


def delete_payment(request, id):
    print("==========", id)
    crystal_admin = payment.objects.get(payment_id=id)
    crystal_admin.delete()
    return redirect("/em/payment")


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
                return redirect('/em/eventdetails_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = event_detailsForm()

    return render(request, 'em_event_details_insert.html',
                  {'form': form, "Event": Event, "User": User, "Manager": Manager})


def insert_food(request):
    if request.method == "POST":
        form = foodForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/em/food_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = foodForm()

    return render(request, 'em_food_insert.html', {'form': form})


def insert_decoration(request):
    if request.method == "POST":
        form = decorationForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/em/decoration_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = decorationForm()

    return render(request, 'em_decoration_insert.html', {'form': form})


def insert_payment(request):
    Order = order.objects.all()

    if request.method == "POST":
        form = paymentForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/em/payment_show')
            except:
                print("---------------", sys.exc_info())
    else:
        form = paymentForm()

    return render(request, 'em_insert_payment.html', {'form': form, "Order": Order})


def select_food(request, id):
    fd = food.objects.get(food_id=id)
    return render(request, 'em_update_food.html', {'food': fd})


def update_food(request, id):
    fd = food.objects.get(food_id=id)
    form = foodForm(request.POST, instance=fd)
    if form.is_valid():
        form.save()
        return redirect("/em/food_show")
    return render(request, 'em_update_food.html', {'food': fd})


# ---------------------------decoration-----------------------------

def select_decoration(request, id):
    dc = decoration.objects.get(decoration_id=id)
    return render(request, 'em_update_decoration.html', {'decoration': dc})


def update_decoration(request, id):
    dc = decoration.objects.get(decoration_id=id)
    form = decorationForm(request.POST, instance=dc)
    if form.is_valid():
        form.save()
        return redirect("/em/decoration_show")
    return render(request, 'em_update_decoration.html', {'decoration': dc})


def select_event_details(request, id):
    evd = event_details.objects.get(event_details_id=id)
    return render(request, 'em_update_eventdetails_details.html', {'bank_details': evd})


def update_event_details(request, id):
    Event = event.objects.all()
    User = user.objects.all()
    Manager = manager.objects.all()
    evd = event_details.objects.get(event_details_id=id)
    form = event_detailsForm(request.POST, instance=evd)
    if form.is_valid():
        form.save()
        return redirect("/em/eventdetails_show")
    return render(request, 'em_update_eventdetails_details.html',
                  {'event_details': evd, 'Event': Event, 'User': User, 'Manager': Manager})


def select_payment(request, id):
    pay = payment.objects.get(payment_id=id)
    return render(request, 'em_update_payment.html', {'payment': pay})


def update_payment(request, id):
    Order = order.objects.all()
    pay = payment.objects.get(payment_id=id)
    form = paymentForm(request.POST, instance=pay)
    if form.is_valid():
        form.save()
        return redirect("/em/payment_show")
    return render(request, 'em_update_payment.html', {'payment': pay, 'Order': Order})


# def dashboard(request):
#     manager_id = request.session.get('manager_id')  # Use .get() to avoid KeyError if 'manager_id' is not present in session
#     d = user.objects.all().count()
#     b = manager.objects.all().count()
#     r = event.objects.all().count()
#     a = order.objects.all().count()
#
#     return render(request, "dashboard.html", {'user': d, 'manager': b, 'event': r, 'order': a})

# from .models import Event


def dashboard(request):
    manager_id = request.session.get(
        'manager_id')  # Use .get() to avoid KeyError if 'manager_id' is not present in session
    d = user.objects.all().count()
    b = manager.objects.all().count()
    r = event.objects.all().count()
    orders = order.objects.all()  # Get all orders
    pending_orders = orders.filter(order_status='pending').count()
    completed_orders = orders.filter(order_status='completed').count()

    return render(request, "em_dashboard.html", {'user': d, 'manager': b, 'event': r, 'pending_orders': pending_orders,
                                              'completed_orders': completed_orders})
