from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from products.models import Product, Category
from orders.models import Order, OrderItem
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  

    def get_paginated_response(self, data):
        return Response(data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoySerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    # Enable search
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name', 'id']

    @action(detail=True, methods=['post', 'delete'])
    def customizer(self, request, pk=None):
        """Marks the product as customizable or not."""
        try:
            product = self.get_object()
            if request.method == 'POST':
                product.customizable = True
                product.save()
                return Response({'message': f'Product {product.name} is now customizable.'}, status=200)
            elif request.method == 'DELETE':
                product.customizable = False
                product.save()
                return Response({'message': f'Product {product.name} is no longer customizable.'}, status=200)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)

    @action(detail=True, methods=['post', 'get'])
    def options(self, request, pk=None):
        """ Returns an empty list for product options. """
        return Response([{'code': pk, 'name':'hoodie', 'values': []}])

        