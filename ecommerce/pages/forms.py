from django import forms
from cheapStore.models import Receipt

class AddToCartForm(forms.Form):
    """A form to add something to the users cart"""
    addToCart = forms.CharField(label='addToCart', max_length=100) # Only requires the name of the product


class ClearCartForm(forms.Form):
    """A form to clear the users cart"""
    clearCart = forms.CharField(label='clearCart', max_length=100) # This is a dummy input

class ReceiptForm(forms.ModelForm):
    """
    This is a form that creates a reciept from the users cart. 
    This uses the Receipt model in the cheapStore app.
    """
    class Meta:
        model = Receipt
        fields= [
            'user',
            'cost',
            'products'
        ]