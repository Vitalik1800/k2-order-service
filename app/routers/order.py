from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db
from app.services.order_service import create_order_service

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post(
    "",
    response_model=schemas.OrderResponse,
    status_code=201
)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    return create_order_service(db, order)

@router.get(
    "/client/{client_id}",
    response_model=list[schemas.OrderResponse]
)
def get_orders_by_client(
    client_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_orders_by_client(db, client_id)
