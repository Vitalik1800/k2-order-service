from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas

def validate_client(
    db: Session,
    client_id: int
) -> models.Client:
    client = db.get(models.Client, client_id)

    if client is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client with ID {client_id} not found"
        )

    return client

def validate_order_items(
    items: list[schemas.OrderItemCreate]
) -> None:
    if not items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Order must contain at least one item"
        )

def validate_products(
    db: Session,
    items: list[schemas.OrderItemCreate]
) -> dict[int, models.Product]:
    products = {}

    for item in items:
        product = db.get(models.Product, item.product_id)

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {item.product_id} not found"
            )

        products[item.product_id] = product

    return products

def calculate_total_price(
    items: list[schemas.OrderItemCreate],
    products: dict[int, models.Product]
) -> Decimal:
    total_price = Decimal("0.00")

    for item in items:
        product = products[item.product_id]
        total_price += product.price * item.quantity

    return total_price

def create_order_items(
    db: Session,
    order: models.Order,
    items: list[schemas.OrderItemCreate],
    products: dict[int, models.Product]
) -> None:
    for item in items:
        order_item = models.OrderItem(
            order=order,
            product_id=products[item.product_id].id,
            quantity=item.quantity
        )

        db.add(order_item)

def create_order_service(
    db: Session,
    order_data: schemas.OrderCreate
) -> models.Order:

    # 1. Перевірка, що список товарів не порожній
    validate_order_items(order_data.items)

    # 2. Перевірка клієнта
    validate_client(db, order_data.client_id)

    # 3. Перевірка існування всіх товарів
    products = validate_products(db, order_data.items)

    # 4. Розрахунок загальної суми
    total_price = calculate_total_price(
        order_data.items,
        products
    )

    # 5. Створення замовлення
    order = crud.create_order(
        db=db,
        client_id=order_data.client_id,
        total_price=total_price
    )

    # 6. Створення позицій замовлення
    create_order_items(
        db=db,
        order=order,
        items=order_data.items,
        products=products
    )

    # 7. Збереження всіх змін
    db.commit()
    db.refresh(order)

    return order
