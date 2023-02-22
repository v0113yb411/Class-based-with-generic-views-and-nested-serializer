from django.shortcuts import render
from .models import Category,Products
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class CategoryGetApi(APIView):
    def get(self,request,pk=None):
        id=pk
        if id is not None:
            data=Category.obejects.all()
            serializer=CategorySerializer(data)
            return Response(serializer.data)
        data=Category.objects.all()
        serializer=CategorySerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data is created'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class CategoryUpdateApi(APIView):

    def put(self,request,pk=None,format=None):
        id=pk
        data=Category.objects.get(id=pk)
        serializer=CategorySerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data is updated'})
        return Response (serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request,pk=None,format=None):
        id=pk
        data=Category.objects.get(pk=id)
        serializer=CategorySerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data is updated'})
        return Response(serializer.errors)
    
    def delete(self,request,pk=None,format=None):
        id=pk
        data=Category.objects.get(pk=id)
        data.delete()
        return Response({'msg':'Data is deleted'})
    
#Generic Views for products.

class ProductGetApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class ProductUpdateApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

    

    
    
