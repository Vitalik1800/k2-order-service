from fastapi import FastAPI

from app.database import Base, engine

import app.models

from app.routers.client import router as client_router
from app.routers.product import router as product_router
from app.routers.order import router as order_router

app = FastAPI(
    title="K2 ERP Test Task"
)

Base.metadata.create_all(bind=engine)

app.include_router(client_router)
app.include_router(product_router)
app.include_router(order_router)

@app.get("/")
def root():
    return {"message": "K2 ERP API is running"}
