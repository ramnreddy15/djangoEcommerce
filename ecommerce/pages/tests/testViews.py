
from django.test import TestCase, Client
from django.urls import reverse
from cheapStore.models import Receipt, Product

class TestViews(TestCase):
    """Testing the views in the pages app"""

    def setUp(self):
        """Setting up the basic things we will use in the test"""
        self.client = Client()
        self.indexUrl = reverse('index')
        self.productsUrl = reverse('products')
        self.cartUrl = reverse('cart')
        self.checkoutUrl = reverse('checkout')

        self.product1 = Product.objects.create( # Creating a product model so users can buy things
            name='glass',
            description='A very sharp object.',
            price=250
        )

    def testIndexGET(self):
        """Testing to see if the index page loads in a GET request"""
        response = self.client.get(self.indexUrl)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def testProductsGET(self):
        """Testing to see if the products page loads in a GET request"""
        response = self.client.get(self.productsUrl)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    def testProductsPOSTAddToCart(self):
        """Testing to see if the products page works in a POST request."""
        response = self.client.post(self.productsUrl, { # Giving data to form
            'addToCart': 'glass'
        })

        self.assertEquals(response.status_code, 200)
        session = self.client.session
        self.assertEquals(len(session["products"]), 1) # Checking to see if values are correct in session storage 
        self.assertEquals(session["glass"], 1)

    def testProductsPOSTNoData(self):
        """Testing to see if the products page work in a POST request with no data."""
        response = self.client.post(self.productsUrl)

        self.assertEquals(response.status_code, 200)
        session = self.client.session
        self.assertEquals(len(session["products"]), 0) # No data should be in the session storage
        self.assertEquals(session.get('glass'), None)

    def testCartGET(self):
        """Testing to see if the cart page loads"""
        response = self.client.get(self.cartUrl)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def testCartPOSTClearCart(self):
        """Testing to see if the cart page works in a POST request."""
        response = self.client.post(self.productsUrl, { # Adding stuff to session storage
            'addToCart': 'glass'
        })

        self.assertEquals(response.status_code, 200)
        session = self.client.session
        self.assertEquals(len(session["products"]), 1)
        self.assertEquals(session["glass"], 1)

        reponse = self.client.post(self.cartUrl, { # Clearing cart
            'clearCart': 'Clear'
        })

        self.assertEquals(response.status_code, 200)
        session = self.client.session
        self.assertEquals(len(session["products"]), 0) # Nothing should be in session storage
        self.assertEquals(session.get('glass'), None)

    def testCartPOSTNoData(self):
        """Testing to see if the products page works in a POST request with no data."""
        response = self.client.post(self.productsUrl, { # Adding an item to cart
            'addToCart': 'glass'
        })

        self.assertEquals(response.status_code, 200)
        session = self.client.session
        self.assertEquals(len(session["products"]), 1)
        self.assertEquals(session["glass"], 1)

        response = self.client.post(self.cartUrl) # Nothing in the request

        self.assertEquals(response.status_code, 200) # Nothing should change
        session = self.client.session
        self.assertEqual(len(session["products"]), 1)
        self.assertEquals(session.get('glass'), 1)

    def testCheckoutGET(self):
        """Testing to see if the checkout page loads"""
        response = self.client.get(self.checkoutUrl)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    def testCheckoutPOST(self):
        """Testing to see if the checkout page works in a POST request."""
        response = self.client.post(self.productsUrl, { # Adding an item to cart
            'addToCart': 'glass'
        })

        self.assertEquals(response.status_code, 200)
        session = self.client.session
        self.assertEquals(len(session["products"]), 1)
        self.assertEquals(session["glass"], 1)

        reponse = self.client.post(self.checkoutUrl, { # Submitting a form
            'user': 'User',
            'cost': 10000,
            'products': '{ glass : 1 }'
        })

        self.assertEquals(response.status_code, 200) # Checking to see if cart status and receipt model are correct
        self.assertEquals(len(Receipt.objects.all()), 1)
        session = self.client.session
        self.assertEquals(len(session["products"]), 0)
        self.assertEquals(session.get('glass'), None)

    def testCheckoutPOSTNoData(self):
        """Testing to see if the checkout page works in a POST request without any data."""
        response = self.client.post(self.productsUrl, { # Adding an item to cart
            'addToCart': 'glass'
        })

        self.assertEquals(response.status_code, 200)
        session = self.client.session
        self.assertEquals(len(session["products"]), 1) # Basic checks
        self.assertEquals(session["glass"], 1)

        reponse = self.client.post(self.checkoutUrl)

        self.assertEquals(response.status_code, 200) # Nothing should change in cart and there should be no receipt model
        self.assertEquals(len(Receipt.objects.all()), 0)
        session = self.client.session
        self.assertEquals(len(session["products"]), 1)
        self.assertEquals(session.get('glass'), 1)
