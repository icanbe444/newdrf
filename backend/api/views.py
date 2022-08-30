from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

@api_view(['POST', 'GET'])
def api_home(request, *args, **kwargs):
   
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        # data = serializer.data
        return Response(serializer.data)
    return Response({"invalid data": "not good data"})