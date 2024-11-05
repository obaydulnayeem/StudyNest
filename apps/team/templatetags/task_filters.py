from django import template

register = template.Library()

@register.filter
def modulo(value, arg):
    """Returns the modulo of value by arg."""
    return value % arg
