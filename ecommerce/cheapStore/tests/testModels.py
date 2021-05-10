from django.test import TestCase
from cheapStore.models import Product, Receipt

class TestModels(TestCase):
    """Test cheapStore models"""

    def setUp(self):
        """Set up a product and receipt model so we can test them"""
        self.product1 = Product.objects.create(
            name='glass',
            description='A very sharp object.',
            price=250
        )

        self.receipt1 = Receipt.objects.create(
            user='User',
            cost=10000,
            products='{ glass : 1 }'
        )

    def testProductModel(self):
        """Test to see if the values in the product models are the same as what we inputted"""
        self.assertEquals(str(self.product1.name), 'glass')
        self.assertEquals(str(self.product1.description), 'A very sharp object.')
        self.assertEquals(self.product1.price, 250)

    def testReceiptModel(self):
        """Test to see if the values in the receipt models are the same as what we inputted"""
        self.assertEquals(str(self.receipt1.user), 'User')
        self.assertEquals(self.receipt1.cost, 10000)
        self.assertEquals(self.receipt1.products, '{ glass : 1 }')
        self.assertNotEquals(self.receipt1.time, -1) # Also making sure the time actually worked
        