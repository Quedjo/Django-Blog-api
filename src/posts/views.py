from django.shortcuts import render
from rest_framework import generics,permissions
from .models import post
from .serializers import postserializer

# Create your views here.
class postslist(generics.ListCreateAPIView):
    queryset=post.objects.all()
    serializer_class=postserializer
    #permission_classes= (permissions.IsAuthenticatedOrReadOnly,)


class postsdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes= (permissions.IsAdminUser,)
    queryset=post.objects.all()
    serializer_class=postserializer
    