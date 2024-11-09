from django import template

register = template.Library()

@register.simple_tag
def convert_price(price):
    price = str(price)
    return " ".join([price[max(i-3, 0):i] for i in range(len(price), 0,-3)][::-1]) + " ₽"
