"""Tests for the products API."""

import pytest
from fastapi.testclient import TestClient

from inventory_api.main import app
from inventory_api.routers.products import service


@pytest.fixture(autouse=True)
def reset_service() -> None:
    """Reset the in-memory product service before each test."""
    service.clear()


client = TestClient(app)


def test_create_product_returns_created_product() -> None:
    """Creating a valid product should return HTTP 201 and the product data."""
    response = client.post(
        "/products",
        json={"name": "Sauce Labs Backpack", "price": 29.99},
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "Sauce Labs Backpack",
        "price": 29.99,
    }


def test_get_unknown_product_returns_404() -> None:
    """Requesting an unknown product should return HTTP 404."""
    response = client.get("/products/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Product 999 not found"}


def test_list_products_returns_created_products() -> None:
    """Listing products should return previously created products."""
    client.post("/products", json={"name": "Bike Light", "price": 9.99})
    client.post("/products", json={"name": "Bolt T-Shirt", "price": 15.99})

    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Bike Light", "price": 9.99},
        {"id": 2, "name": "Bolt T-Shirt", "price": 15.99},
    ]