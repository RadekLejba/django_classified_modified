from decimal import Decimal as D
from decimal import InvalidOperation

from babel.numbers import format_currency
from django import template

register = template.Library()


@register.filter(name='currency')
def currency(value, currency=None):
    """
    Format decimal value as currency
    """
    try:
        value = D(value)
    except (TypeError, InvalidOperation):
        return ""

    # Using Babel's currency formatting
    # http://babel.pocoo.org/en/latest/api/numbers.html#babel.numbers.format_currency

    kwargs = {
        'currency': 'PLN',
        'locale': 'pl'
    }

    return format_currency(value, **kwargs)
