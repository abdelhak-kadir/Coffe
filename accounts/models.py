from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.


class UserProfile(models.Model):
    # modeling one-to-one relationships between objects
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    product_fav = models.ManyToManyField(Product)
    # represents a many-to-many relationship between two models. It allows you to define a many-to-many relationship without creating an explicit intermediate table.
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
