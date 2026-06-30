from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db

router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)

@router.post(
    "",
    response_model=schemas.ClientResponse,
    status_code=201
)
def create_client(
    client: schemas.ClientCreate,
    db: Session = Depends(get_db)
):
    return crud.create_client(db, client)
