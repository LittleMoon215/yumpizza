from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'welcome.html')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            username = form.data["number"]
            password = form.data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next is not None:
                    return redirect("menu_view")
                else:
                    return redirect("index")
            else:
                return render(request, "welcome.html", {"message": "Неверный номер или пароль"})
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'registration/login.html', context)
    else:
        return redirect("index")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["number"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, 'register.html', context)


@login_required
def menu_view(request):
    pizzas = Pizza.objects.all()
    snacks = Snack.objects.all()
    drinks = Drink.objects.all()
    return render(request, 'menu.html', {"pizzas": pizzas, "drinks": drinks, "snacks": snacks})


@login_required
def confirm_order(request):
    quantities_pizza = request.POST.getlist('qty_pizza')
    quantities_drink = request.POST.getlist('qty_drink')
    quantities_snack = request.POST.getlist('qty_snack')
    pizzas = Pizza.objects.all()
    snacks = Snack.objects.all()
    drinks = Drink.objects.all()
    ordered_pizzas = []
    ordered_drinks = []
    ordered_snacks = []
    ordered_pizzas_quantities = []
    ordered_drinks_quantities = []
    ordered_snacks_quantities = []

    # prices = request.POST.getlist('price')
    pizza_totals = []
    drink_totals = []
    snack_totals = []
    for item, qty in zip(pizzas, quantities_pizza):
        if int(qty) > 0:
            ordered_pizzas.append(item)
            ordered_pizzas_quantities.append(int(qty))
            pizza_totals.append(item.price * int(qty))
    for item, qty in zip(drinks, quantities_drink):
        if int(qty) > 0:
            ordered_drinks.append(item)
            ordered_drinks_quantities.append(int(qty))
            drink_totals.append(item.price * int(qty))
    for item, qty in zip(snacks, quantities_snack):
        if int(qty) > 0:
            ordered_snacks.append(item)
            ordered_snacks_quantities.append(int(qty))
            snack_totals.append(item.price * int(qty))

    return render(request, 'order_confirmation.html', {"pizzas_summary": zip(ordered_pizzas, ordered_pizzas_quantities,
                                                                             pizza_totals),
                                                       "drinks_summary": zip(ordered_drinks,
                                                                             ordered_drinks_quantities, drink_totals),
                                                       "snacks_summary": zip(ordered_snacks, ordered_snacks_quantities,
                                                                             snack_totals),
                                                       "grand_total": sum(pizza_totals) + sum(drink_totals) +
                                                                      sum(snack_totals) + 100})


@login_required
def place_order(request):
    pizza_quantities = request.POST.getlist('pizza_qty')
    drink_quantities = request.POST.getlist('drink_qty')
    snack_quantities = request.POST.getlist('snack_qty')
    pizzas = request.POST.getlist('pizza')
    drinks = request.POST.getlist('drink')
    snacks = request.POST.getlist('snack')
    order = Order(user=request.user)
    order.save()

    for item, qty in zip(pizzas, pizza_quantities):
        pizza = Pizza.objects.filter(name=item)
        order_pizza = OrderPizza(itemId=pizza.first(), orderId=order, Qty=qty)
        order_pizza.save()
    for item, qty in zip(drinks, drink_quantities):
        drink = Drink.objects.filter(name=item)
        order_drink = OrderDrink(itemId=drink.first(), orderId=order, Qty=qty)
        order_drink.save()
    for item, qty in zip(snacks, snack_quantities):
        snack = Snack.objects.filter(name=item)
        order_snack = OrderSnack(itemId=snack.first(), orderId=order, Qty=qty)
        order_snack.save()

    return render(request, 'order.html')


@login_required
def user_orders_view(request):
    orders = Order.objects.filter(user=request.user)
    my_orders = {}
    for item in orders:
        orders_pizza = OrderPizza.objects.filter(orderId=item)
        orders_drinks = OrderDrink.objects.filter(orderId=item)
        orders_snack = OrderSnack.objects.filter(orderId=item)
        my_orders[f"{item}"] = {"date": item.order_timestamp, "pizzas": orders_pizza, "drinks": orders_drinks,
                                "snacks": orders_snack}

    context = {"orders": my_orders}
    return render(request, 'my_orders.html', context)
