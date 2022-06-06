from rest_framework import serializers
from .models import Clothes, Manufacturer, Category

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ClothesSerializer(serializers.ModelSerializer):
    category_info = CategorySerializer(source='category', many=True, read_only=True)
    manufacturer_info = ManufacturerSerializer(source='manufacturer', read_only=True)
    class Meta:
        model = Clothes
        exclude = ['category', 'manufacturer']
