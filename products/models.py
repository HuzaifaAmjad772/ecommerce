from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,  blank=True, null=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

