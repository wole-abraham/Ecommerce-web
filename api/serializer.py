from rest_framework import serializers
from products.models import Product, Category
from orders.models import Order, OrderItem




class ProductSerializer(serializers.ModelSerializer):
    code = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    values = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['values','code', 'name', 'description', 'price', 'category', 'image', 'stock', 'thumbnail', 'customizable']

    def get_code(self, obj):
        return str(obj.id)
    
    def get_values(self, obj):
        return []
    
    def get_thumbnail(self, obj):
        request = self.context.get('request')
        thumbnail = obj.image.url
        return request.build_absolute_uri(thumbnail)

class CategoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'