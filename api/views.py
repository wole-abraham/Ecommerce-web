from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from products.models import Product, Category
from orders.models import Order, OrderItem
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from rest_framework import status
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name']


    @action(detail=True, methods=['post', 'delete'])
    def customizer(self, request, pk=None):
        """ Marks the product as customizable """  
        if request.method == 'POST':
            try:
                product = self.get_object()
                product.customizable = True
                product.save()
                return Response({'message': 'Product is now customizable'})
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=404)
        elif request.method == 'DELETE':
            try:
                product = self.get_object()
                product.customizable = False
                product.save()
                return Response({"message": f"Product {product.name} is no longer customizable."}, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
                
        
    @action(detail=True, methods=['post', 'get'])
    def options(self, request, pk=None):
        return Response([])
        