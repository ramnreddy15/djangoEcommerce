from django.test import SimpleTestCase
from pages.forms import AddToCartForm, ClearCartForm, ReceiptForm

class TestForms(SimpleTestCase):
    """Testing to see if the forms work properly"""

    def testAddToCartFormValidData(self):
        """Checking the add to cart form with valid data"""
        form = AddToCartForm(data={
            'addToCart': 'meme'
        })

        self.assertTrue(form.is_valid())

    def testAddToCartFormNoData(self):
        """Checking the add to cart form with no data"""
        form = AddToCartForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def testClearCartFormValidData(self):
        """Checking the clear cart form with valid data"""
        form = ClearCartForm(data={
            'clearCart': 'Clear'
        })

        self.assertTrue(form.is_valid())

    def testClearFormNoData(self):
        """Checking the clear cart form with no data"""
        form = ClearCartForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def testReceiptFormValidData(self):
        """Checking the receipt form with valid data"""
        form = ReceiptForm(data={
            'user': 'User',
            'cost': 10000,
            'products': '{ meme : 1 }'
        })

        self.assertTrue(form.is_valid())

    def testReceiptFormNoData(self):
        """Checking the receipt form with no data"""
        form = ReceiptForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)