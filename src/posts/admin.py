from django.contrib import admin
from .models import post

class postadmin(admin.ModelAdmin):
    model= post
    list_display= (
            "author", 
            "title", 
            "body", 
            "created_at",
            "updated_at",
    )

# Register your models here.

admin.site.register(post,postadmin)