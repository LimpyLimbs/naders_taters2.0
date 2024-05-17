from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class Address(BaseModel):
    address_1: str
    address_2: str
    city: str
    state: str
    zip_code: int

class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    address: Address
    phone_number: int
    email: str

class GetUserSchema(CreateUserSchema):
    user_id: int
    orders: List[Optional[UUID]]

class AppendOrdersSchema(BaseModel):
    orders: List[UUID]