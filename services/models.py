from django.db import models
from django.contrib .auth.models import User
# Create your models here.


class Service(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    service_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=False)
