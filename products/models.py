from django.db import models
from datetime import datetime

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    desciption = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_active = models.BooleanField(default=True)
    pubish_date = models.DateTimeField(default=datetime.now)

    def __str__(self):  # defines how the object should be represented as a string
        return self.name

    class Meta:
        ordering = ['-pubish_date']
