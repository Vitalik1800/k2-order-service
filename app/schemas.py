from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, EmailStr, Field

class ClientCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Client name"
    )

    email: EmailStr = Field(
        ...,
        description="Client email"
    )

class ClientResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class ProductCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Product name"
    )

    price: Decimal = Field(
        ...,
        gt=0,
        description="Product price"
    )

class ProductResponse(BaseModel):
    id: int
    name: str
    price: Decimal

    model_config = ConfigDict(from_attributes=True)

class OrderItemCreate(BaseModel):
    product_id: int = Field(
        ...,
        gt=0,
        description="Product ID"
    )

    quantity: int = Field(
        ...,
        gt=0,
        description="Product quantity"
    )

class OrderCreate(BaseModel):
    client_id: int = Field(
        ...,
        gt=0,
        description="Client ID"
    )

    items: list[OrderItemCreate] = Field(
        ...,
        min_length=1,
        description="List of products in the order"
    )

class OrderItemResponse(BaseModel):
    product_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)

class OrderResponse(BaseModel):
    id: int
    client_id: int
    total_price: Decimal
    created_at: datetime
    items: list[OrderItemResponse]

    model_config = ConfigDict(from_attributes=True)
