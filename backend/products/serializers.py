import email
from turtle import title
from requests import request
from rest_framework import serializers
from attr import fields
from django import forms
from .models import Product
from rest_framework.reverse import reverse
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True) #this is used to introduce a name that isnt in the model
    
    title = serializers.CharField(validators=[ validators.unique_product_title, validators.validate_title_no_hello])
    name = serializers.CharField(source='title', read_only=True)
    class Meta:
        model= Product
        fields = [
            'url',
            'id',
            # 'email',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount',

        ]
    # #validating field of my choice. This will make sure two products do not have ths same title
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact= value) #iexact looks for exact name and case sensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value




    def get_url(self, obj):
        # return f"/api/products/{obj.pk}"
        request = self.context.get('request')
        if request is None:
            return None

        return reverse("product-detail", kwargs= {"pk": obj.pk}, request=request)

    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     return obj


        
    def get_my_discount(self, obj):
        if not hasattr(obj , 'id'):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.get_discount()


       

       