from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from products.models import Product
from django.db.models import Case, When

# Create your views here.
from products.models import Category

def cart(request):
    cart = request.session.get('cart', {})
    items = Product.objects.filter(id__in=cart.keys()).order_by(
        Case(*[When(id=id, then=pos) for pos, id in enumerate(cart)])
    )
    items = zip(cart.values(), items)

    return render(request, 'cart/shopping-cart.html',  {'cart': cart, 'items': items})



def add_to_cart(request):
    if request.method == 'POST':
        # Get the product ID from the request body
        data = json.loads(request.body)
        product_id = data.get('product_id')
    

        # Retrieve the product from the database
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

        # Add the product to the cart in the session
        cart = request.session.get('cart', {})

        
    
        if str(product_id) in cart:
            cart[str(product_id)] += 1
        else:
            cart[str(product_id)] = 1
        request.session['cart'] = cart

        # Calculate the new cart count
        print(cart)
        

        cart_count = sum(cart.values())
        print(cart_count)

        # Return the updated cart count in the response
        return JsonResponse({'count': cart_count})
    cart = request.session.get('cart', {})
    return JsonResponse({'count': sum(cart.values())})

def remove_from_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        del request.session['cart'][str(product_id)]


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart_view')
