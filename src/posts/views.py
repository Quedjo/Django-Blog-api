from django.shortcuts import render
from rest_framework import generics,permissions
from .models import post
from .serializers import postserializer
from .permissions import IsAuthorOrReadonly

# Create your views here.
class postslist(generics.ListCreateAPIView):
    permission_classes= (IsAuthorOrReadonly,)
    queryset=post.objects.all()
    serializer_class=postserializer
    


class postsdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes= (IsAuthorOrReadonly,)
    queryset=post.objects.all()
    serializer_class=postserializer
    