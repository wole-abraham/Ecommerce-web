from django.shortcuts import render
from products.models import Product, Category



# Create your views here.


def index(request):
    product = Product.objects.all()
    return render(request, 'base/base.html', context={'products': product})


def shop(request):
    product = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'shop.html', context={'products': product, 'categories': categories})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    category = Product.objects.filter(category=product.category)
    return render(request, 'shop-details.html', context={'product': product, 'categories': category})