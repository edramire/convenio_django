from datetime import datetime
from django import template

register = template.Library()

@register.filter
def timeuntil_es(value):
    delta = value - datetime.now().date()

    return '{0} dias'.format(str(delta.days)) if delta.days > 0 else ""
