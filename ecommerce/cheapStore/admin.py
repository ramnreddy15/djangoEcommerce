from django.contrib import admin
from .models import Receipt, Product


admin.site.register(Receipt) # Allowing admins to see the data in the admin page
admin.site.register(Product)
