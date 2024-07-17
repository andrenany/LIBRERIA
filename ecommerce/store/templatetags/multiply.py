from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def sum_total(cart_items):
    return sum(item.book.price * item.quantity for item in cart_items)
