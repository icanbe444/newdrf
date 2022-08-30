from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    # instance = Product.objects.all().order_by("?").first()
    
    # if instance:
    #     '''
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    #     #this is trying to convert the model into python dictionary and it is re written bellow using model_to_dict
    #     '''
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        # data = serializer.data
        return Response(serializer.data)
    return Response({"invalid data": "not good data"})