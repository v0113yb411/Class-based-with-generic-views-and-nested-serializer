from rest_framework import serializers
from .models import Category
from .models import Products


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= '__all__'


# Nested serializer.

class GetCatagory(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=[
            'id',
            'title'
        ]

class ProductSerializer(serializers.ModelSerializer):
    category=GetCatagory()
    class Meta:
        model=Products
        fields=['title','category']