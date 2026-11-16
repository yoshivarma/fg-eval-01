"""Pricing calculations."""


def apply_discount(price, percent):
    """Return the price after a discount of `percent` percent."""
    return price * (1 - percent / 100)
