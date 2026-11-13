from decimal import Decimal

from fastapi.testclient import TestClient

from shop.main import app

client = TestClient(app)


def test_add_item_and_total():
    client.post("/cart/c1/items", json={"product_id": 1, "quantity": 2})  # 2 x 19.90
    client.post("/cart/c1/items", json={"product_id": 3, "quantity": 2})  # 2 x 5.00
    response = client.get("/cart/c1")
    assert response.status_code == 200
    assert Decimal(response.json()["total"]) == Decimal("49.80")


def test_add_unknown_product_returns_404():
    response = client.post("/cart/c2/items", json={"product_id": 999, "quantity": 1})
    assert response.status_code == 404
