"""Data models for the sandbox shop."""

from decimal import Decimal

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str
    price: Decimal


class AddItem(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class CartItem(BaseModel):
    product: Product
    quantity: int


CATALOG: dict[int, Product] = {
    1: Product(id=1, name="T-shirt", price=Decimal("19.90")),
    2: Product(id=2, name="Hoodie", price=Decimal("89.90")),
    3: Product(id=3, name="Sticker pack", price=Decimal("5.00")),
}
