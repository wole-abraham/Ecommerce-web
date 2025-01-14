from django.shortcuts import render
from rest_framework import viewsets, filters
from products.models import Product, Category
from orders.models import Order, OrderItem
from .serializer import *
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name']
