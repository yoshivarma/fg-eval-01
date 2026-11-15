"""Pricing calculations."""


def apply_discount(price, percent):
    """Return the price after a discount of `percent` percent."""
    return price * percent / 100
