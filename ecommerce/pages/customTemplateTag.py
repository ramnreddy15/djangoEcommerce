from django import template

register = template.Library()
"""This file contains all the custom tags I am using for django templates"""

@register.filter
def to_str(value):
    """converts int to string"""
    return str(value)

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter
def get_item(dictionary, key):
    """returns value from a key in a dictionary"""
    return dictionary.get(key)