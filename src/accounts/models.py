from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class  CustomUser(AbstractUser):
    name=models.CharField(max_length=200, null=True, blank=True)

    

