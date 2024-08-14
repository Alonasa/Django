from django import template

register = template.Library()

@register.filter
def startswith(value, prefix):
    """
    Checks if a string starts with a given prefix.
    """
    return value.startswith(prefix)