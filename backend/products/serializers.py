from rest_framework import serializers
from attr import fields
from django import forms
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True) #this is used to introduce a name that isnt in the model
    class Meta:
        model= Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',

        ]
    def get_my_discount(self, obj):
        if not hasattr(obj , 'id'):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.get_discount()


       

       