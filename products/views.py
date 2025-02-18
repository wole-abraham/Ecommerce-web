from django.shortcuts import render
from products.models import Product, Category
from django.http import JsonResponse

# Create your views here.


def search(request, product):
    product = Product.objects.filter(name__icontains=product)
    categories = Category.objects.all()

    return render(request, 'shop.html', context={'products': product, 'categories': categories})


def shop(request):
    if request.method == 'POST':
        product = Product.objects.filter(name__icontains=request.POST['search'])
        categories = Category.objects.all()
        return render(request, 'shop.html', context={'products': product, 'categories': categories, 'shop': 'shop'})
    
    product = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop.html', context={'products': product, 'categories': categories, 'shop': 'shop'})

def index(request):
    """
        Main Page View
        product: retrieves all products from the database
    """
    if request.method == 'POST':
        return shop(request)
    
    product = Product.objects.all().order_by('-id')
    return render(request, 'base/base.html', context={'products': product})





def product_detail(request, id):
    """
        Product Detail View -> View information about one product
        product: retrieves a product from the database
        category: retrieves all products from the same category
    """
    product = Product.objects.get(id=id)
    category = Product.objects.filter(category=product.category)
    return render(request, 'shop-details.html', context={'product': product, 'categories': category})


def get_products(request):
    products = Product.objects.all()
    data = [product.to_dict() for product in products]
    return JsonResponse(data, safe=False)


def customizer(request, id):
    """
        Customizer View -> View to customize a product
        product: retrieves a product from the database
    """
    return render(request, 'cart/customizer.html', context={'id':id})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')