from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    discription = serializers.CharField(max_length=500)
    discount = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10,decimal_places=2)
    category = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length = 100)

