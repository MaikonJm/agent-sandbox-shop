"""Cart storage and totals."""

from decimal import Decimal

from shop.models import CartItem

CARTS: dict[str, list[CartItem]] = {}


def cart_total(items: list[CartItem]) -> Decimal:
    """Sum of price x quantity for every item in the cart."""
    total = Decimal(0)
    for item in items:
        total += item.product.price * item.quantity
    return total
