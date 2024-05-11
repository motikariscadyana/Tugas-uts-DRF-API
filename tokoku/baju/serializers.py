from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class ProductSreializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSreializer(serializers.ModelSerializer): 
    class Meta:
        model = Order
        fields = '__all__'
