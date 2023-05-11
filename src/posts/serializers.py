from rest_framework import serializers
from .models import post

class postserializer(serializers.ModelSerializer):
    class Meta:
        model= post
        fields=[
            "id",
            "author", 
            "title", 
            "body", 
            "created_at", 
            #"updated_at",

        ]