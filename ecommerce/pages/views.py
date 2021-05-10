from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .utils import simpleCostCalculator
from .forms import AddToCartForm, ClearCartForm, ReceiptForm

from cheapStore.models import Product

def index(request):
    """Shows the index page"""

    if('products' not in request.session): # Adds session storage of products if it is not there.
        request.session['products'] = []

    return render(request, "index.html", {})

def products(request):
    """Shows the products page"""

    if('products' not in request.session): # Adds session storage of products if it is not there.
        request.session['products'] = []

    if request.method == 'POST':
        form = AddToCartForm(request.POST) # This is the addToCart form
        if form.is_valid(): # It will add the product to the cart (session storage) if it meets all checks
            addToCart = str(form.cleaned_data['addToCart'])  
            if(len(Product.objects.filter(name=addToCart).values()) != 0): # Checks if product is actually available
                if addToCart in request.session["products"]: # For some reaon dictionaries will not work ;(
                    request.session[addToCart] = request.session[addToCart]+1
                else:
                    request.session["products"].append(addToCart)
                    request.session[addToCart] = 1
    
    allObjects = Product.objects.all()

    context = {
        'allObjects':allObjects
    }
    
    return render(request, "products.html", context)

def cart(request):
    """Shows the cart page"""

    if('products' not in request.session): # Adds session storage of products if it is not there.
        request.session['products'] = []

    if request.method == 'POST':
        form = ClearCartForm(request.POST) 
        if form.is_valid(): # If a user wants to clear the cart this will do so
            for product in request.session['products']: # It will remove everything from session storage
                request.session.pop(product)
            request.session['products'] = []

    context = {
        'wantedProducts': request.session['products'] # Shows all products user wants
    }
    if len(request.session['products']) != 0: # Prepares data like quantities of a product and etc...
        productDict = {}
        for product in request.session['products']: # For some reason dictionaries will not work ;(
            productDict[product] = request.session[product]
        context["quantities"] = productDict
    else:
        context["empty"] = 1

    return render(request, "cart.html", context)

def checkout(request):
    """Shows the checkout page"""

    if('products' not in request.session): # Adds session storage of products if it is not there.
        request.session['products'] = []
    
    context = {}

    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid(): # Creates the reciept
            form.save()
            for product in request.session['products']:
                request.session.pop(product)
            request.session['products'] = []

    if len(request.session['products']) != 0: # Basic checks on how to preview the page
        productDict = {} # Adding neccary data like quantities and prices etc...
        for product in request.session['products']: # For some reason dictionaries will not work ;(
            productDict[product] = request.session[product]
        context["quantities"] = productDict    
        
        prices = {}    
        for product in request.session['products']: # Querying db for price of product and getting the total amount excluding tax
            prices[product] = productDict[product] * Product.objects.filter(name=product).values()[0]['price']
        
        subtotal, taxed, total = simpleCostCalculator(prices)

        context['prices'] = prices # Dictionary for prices of products 
        context['subtotal'] = subtotal
        context['taxed'] = taxed
        context['total'] = total
    else:
        context["empty"] = 1

    context['wantedProducts'] = request.session['products']

    return render(request, "checkout.html", context) 