from django import template

register=template.Library()

@register.filter(name='currency')
def currency(number):
    return "Rs"+str(number)

@register.filter(name='mul')
def mul(value,arg):
    return value * arg
