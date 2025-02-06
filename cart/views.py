from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from products.models import Product
from django.db.models import Case, When

# Create your views here.
from products.models import Category
from .cart import Cart


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('index')

def cart(request):
    cart = Cart(request)
    return render(request, 'cart/shopping-cart.html', {'cart': cart.list()})

def add_to_cart(request, id):
    cart = Cart(request)
    cart.add(id)

    return JsonResponse({'count': cart.cart_item_total()})

def remove_from_cart(request, id):
    cart = Cart(request)
    cart.remove(id)
    print("Removed", cart.cart.get(str(id)))
    print("Total", cart.cart_total())
    return JsonResponse({'Response': 'Sucess'})

def quantity(request, id):
    cart = Cart(request)
    return JsonResponse({'quantity': cart.quantity(id)})

def total(request):
    cart = Cart(request)
    total = cart.cart_total()
    return JsonResponse({"total": total})

def cart_count(request):
    cart = Cart(request)
    return JsonResponse({"count": cart.cart_item_total()})
