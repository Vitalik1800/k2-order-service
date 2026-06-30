def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "K2 ERP API is running"
    }

def test_create_order_success(client):
    # Створюємо клієнта
    client_response = client.post(
        "/clients",
        json={
            "name": "Igor",
            "email": "igor@example.com"
        }
    )

    assert client_response.status_code == 201

    client_id = client_response.json()["id"]

    # Створюємо товар
    product_response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": 1500.00
        }
    )

    assert product_response.status_code == 201

    product_id = product_response.json()["id"]

    # Створюємо замовлення
    order_response = client.post(
        "/orders",
        json={
            "client_id": client_id,
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 2
                }
            ]
        }
    )

    assert order_response.status_code == 201

    order = order_response.json()

    assert order["client_id"] == client_id
    assert float(order["total_price"]) == 3000.0

def test_create_order_client_not_found(client):
    # Спочатку створюємо товар
    product_response = client.post(
        "/products",
        json={
            "name": "Keyboard",
            "price": 500.00
        }
    )

    assert product_response.status_code == 201

    product_id = product_response.json()["id"]

    # Спроба створити замовлення для неіснуючого клієнта
    order_response = client.post(
        "/orders",
        json={
            "client_id": 9999,
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 1
                }
            ]
        }
    )

    assert order_response.status_code == 404
    assert order_response.json()["detail"] == "Client with ID 9999 not found"

def test_create_order_empty_items(client):
    # Створюємо клієнта
    client_response = client.post(
        "/clients",
        json={
            "name": "Ivan",
            "email": "ivan@example.com"
        }
    )

    assert client_response.status_code == 201

    client_id = client_response.json()["id"]

    # Відправляємо порожній список товарів
    order_response = client.post(
        "/orders",
        json={
            "client_id": client_id,
            "items": []
        }
    )

    assert order_response.status_code == 422
