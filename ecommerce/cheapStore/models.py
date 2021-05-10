from django.db import models
from django.utils.datetime_safe import datetime


class Receipt(models.Model):
    """
        This is a receipt model for when someone buys something from the store.

        Attributes:
            user
                The name of the person who bought something.
            time
                The time when the transaction took place.
            cost
                The total cost including tax of the transaction.
            products
                All the products that were bought.

    """
    user = models.CharField(max_length=200)
    time = models.TimeField(default=datetime.now)
    cost = models.DecimalField(max_digits=999,decimal_places=2)
    products = models.TextField(null=True)

    def __str__(self):
         return str(self.user) + " reciept at " + str(self.time)
         
class Product(models.Model):
    """
        This is a product model for when an admin wants to add buyable products.

        Attributes:
            name
                The title of the product.
            description
                The description of the product.
            price
                The price of one of those products without tax.

    """
    name = models.CharField(max_length=200)
    description = models.TextField(default="This is a terrible product.")
    price = models.DecimalField(max_digits=999,decimal_places=2) #Image fields are too annoyig to work with

    def __str__(self):
        return str(self.name)
