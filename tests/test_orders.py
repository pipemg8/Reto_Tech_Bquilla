from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/v1/orders/", json={"product_id": "prod-001", "user_id": "user-001"})
    assert response.status_code == 201
    assert "order_id" in response.json()

def test_create_order_invalid_product():
    response = client.post("/v1/orders/", json={"product_id": "invalid-prod", "user_id": "user-001"})
    assert response.status_code == 500
    assert "Producto no disponible" in response.text
