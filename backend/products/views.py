from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins

from .models import Product
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework.response import Response
from api.mixins import StaffEditorPermissionMixin



class ProductListCreateAPIView(
    StaffEditorPermissionMixin, 
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    #lookup_filed = 'pk


    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        # print(serializer.validated_data)
        # serializer.save()
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailAPIView(
    StaffEditorPermissionMixin, 
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    #lookup_filed = 'pk

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance:
            instance.content = instance.title


class ProductUpdateAPIView(
    StaffEditorPermissionMixin, 
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_filed = 'pk'
    


class ProductDestroyAPIView(
    StaffEditorPermissionMixin, 
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_filed = 'pk'
    

    def perform_delete(self, instance):
        super().perform_destroy(instance)

'''
Below is a function view for ProductListCreateView
'''
@api_view(['GET', 'POST'])
def product_alt_vew(request, pk= None, *args, **kwargs):
    methoD = request.method

    if request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)


    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status=400)

