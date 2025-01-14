from rest_framework import serializers
from products.models import Product, Category
from orders.models import Order, OrderItem




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'