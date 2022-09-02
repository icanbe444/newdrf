from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator




#validating field of my choice. This will make sure two products do not have ths same title
def validate_title(value):
    qs = Product.objects.filter(title__iexact= value) #iexact looks for exact name and case sensitive
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name")
    return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} is not allowed" )
        
unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')