from django.db import models
from django.conf  import settings

# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=200)
    body= models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title