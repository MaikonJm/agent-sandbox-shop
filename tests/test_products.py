from fastapi.testclient import TestClient

from shop.main import app

client = TestClient(app)


def test_list_products_returns_seed_catalog():
    response = client.get("/products")
    assert response.status_code == 200
    assert [p["id"] for p in response.json()] == [1, 2, 3]


def test_get_unknown_product_returns_404():
    assert client.get("/products/999").status_code == 404
