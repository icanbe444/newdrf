from requests import request
from rest_framework import serializers
from attr import fields
from django import forms
from .models import Product
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True) #this is used to introduce a name that isnt in the model
    class Meta:
        model= Product
        fields = [
            'url',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',

        ]

    def get_url(self, obj):
        # return f"/api/products/{obj.pk}"
        request = self.context.get('request')
        if request is None:
            return None

        return reverse("product-detail", kwargs= {"pk": obj.pk}, request=request)


    def get_my_discount(self, obj):
        if not hasattr(obj , 'id'):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.get_discount()


       

       