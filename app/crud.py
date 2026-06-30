from decimal import Decimal

from sqlalchemy.orm import Session
from sqlalchemy import select

from app import models, schemas

def create_client(
    db: Session,
    client: schemas.ClientCreate
) -> models.Client:
    db_client = models.Client(
        name=client.name,
        email=client.email
    )

    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client

def create_product(
    db: Session,
    product: schemas.ProductCreate
) -> models.Product:
    db_product = models.Product(
        name=product.name,
        price=product.price
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

def create_order(
    db: Session,
    client_id: int,
    total_price: Decimal
) -> models.Order:
    db_order = models.Order(
        client_id=client_id,
        total_price=total_price
    )

    db.add(db_order)
    db.flush()
    
    return db_order

def get_orders_by_client(
    db: Session,
    client_id: int
) -> list[models.Order]:
    statement = select(models.Order).where(
        models.Order.client_id == client_id
    )

    return db.scalars(statement).all()
