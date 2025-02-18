from django.shortcuts import render, redirect
from django.http import JsonResponse



# Create your views here.


#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os

from cart.cart import Cart
import stripe
# This test secret API key is a placeholder. Don't include personal details in requests with this key.
# To see your test secret API key embedded in code samples, sign in to your Stripe account.
# You can also find your test secret API key at https://dashboard.stripe.com/test/apikeys.
stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'


YOUR_DOMAIN = 'http://localhost:8000'

def create_checkout_session(request):
    cart = Cart(request)
    cart_list = cart.list()
    try:
        checkout_session = stripe.checkout.Session.create(
           line_items=[
        {
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': x.name},
                'unit_amount': int(x.price)*100,  # $50.00 (Stripe uses cents)
            },
            'quantity': cart.cart[str(x.id)],
        } for x in cart_list
    ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        
        return redirect(checkout_session.url)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    

