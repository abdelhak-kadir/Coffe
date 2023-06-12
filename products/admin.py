from django.contrib import admin
from .models import Product
# Register your models here.

# allows you to register models so they can be managed through the admin interface
admin.site.register(Product)
