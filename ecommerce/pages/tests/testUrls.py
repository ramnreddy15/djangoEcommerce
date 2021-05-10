from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import index, products, cart, checkout

class TestUrls(SimpleTestCase):
    """Testing if the url endpoints are correct"""
    
    def testIndexUrlIsResolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index) 

    def testProductsUrlIsResolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, products) 

    def testCartUrlIsResolved(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func, cart) 

    def testCheckoutUrlIsResolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout) 