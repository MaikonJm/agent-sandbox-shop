"""A small shop API used as a sandbox for the AI Dev Agent."""

from fastapi import FastAPI, HTTPException

from shop.cart import CARTS, cart_total
from shop.models import CATALOG, AddItem, CartItem, Product

app = FastAPI(title="Agent Sandbox Shop")


@app.get("/products")
def list_products(q: str | None = None) -> list[Product]:
    products = list(CATALOG.values())
    if q:
        products = [p for p in products if q.lower() in p.name.lower()]
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int) -> Product:
    if product_id not in CATALOG:
        raise HTTPException(status_code=404, detail="product not found")
    return CATALOG[product_id]


@app.post("/cart/{cart_id}/items", status_code=201)
def add_item(cart_id: str, item: AddItem) -> dict:
    if item.product_id not in CATALOG:
        raise HTTPException(status_code=404, detail="product not found")
    CARTS.setdefault(cart_id, []).append(CartItem(product=CATALOG[item.product_id], quantity=item.quantity))
    return {"cart_id": cart_id, "items": len(CARTS[cart_id])}


@app.get("/cart/{cart_id}")
def get_cart(cart_id: str) -> dict:
    items = CARTS.get(cart_id, [])
    return {"cart_id": cart_id, "items": [i.model_dump() for i in items], "total": str(cart_total(items))}
