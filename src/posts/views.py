from django.shortcuts import render
from rest_framework import generics
from .models import post
from .serializers import postserializer

# Create your views here.
class postslist(generics.ListCreateAPIView):
    queryset=post.objects.all()
    serializer_class=postserializer

class postsdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=post.objects.all()
    serializer_class=postserializer