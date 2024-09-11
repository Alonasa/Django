from datetime import datetime

from django import template

register = template.Library()


@register.filter
def startswith(value, prefix):
    """
    Checks if a string starts with a given prefix.
    """
    return value.startswith(prefix)


@register.filter(name='format_date')
def format_date(value):
    date = datetime.strptime(str(value), "%Y-%m-%d")
    if isinstance(date, datetime):
        return date.strftime("%d %b")
    return value
