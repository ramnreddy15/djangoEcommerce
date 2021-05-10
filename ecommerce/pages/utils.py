"""This file contains useful utility functions that can be used anywhere in the app."""

def simpleCostCalculator(prices):
    """This calculates the subtotal, taxed and total amount from the given dictionary"""
    
    subtotal = 0
    taxed = 0
    total = 0
    for product in prices:
        subtotal+=int(prices[product])

    taxed = subtotal*0.06
    total = taxed + subtotal
    return subtotal, taxed, total