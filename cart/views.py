from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from products.models import Product

# Create your views here.
from products.models import Category

def cart(request):


    return render(request, 'cart/shopping-cart.html')



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
        cart = request.session.get('cart', [])
        cart.append({'product_id': product.id, 'quantity': 1})
        request.session['cart'] = cart

        # Calculate the new cart count
        cart_count = len(cart)

        # Return the updated cart count in the response
        return JsonResponse({'count': cart_count})
def remove_from_cart(request):
    pass

def cart_view(request):
    cart = request.session.get('cart', {})

    return render(request, 'cart.html', {'cart': cart})

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart_view')
