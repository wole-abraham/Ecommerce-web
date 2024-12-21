from django.shortcuts import render

# Create your views here.
from products.models import Category

def cart(request):


    return render(request, 'cart/shopping-cart.html')