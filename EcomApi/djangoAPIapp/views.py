from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *




class DetailsCategory(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=CategorySerializer
    queryset=Category.objects.all()
class ListCategory(generics.ListCreateAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class DetailsBook(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=BookSerializer
    queryset=Book.objects.all()
class ListBook(generics.ListCreateAPIView):
    serializer_class=BookSerializer
    queryset=Book.objects.all()
class DetailsProduct(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=ProductSerializer
    queryset=Product.objects.all()
class ListProduct(generics.ListCreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()



