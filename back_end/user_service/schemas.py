from enum import Enum
from pydantic import BaseModel, conint, constr
from typing import List, Optional
from uuid import UUID

class Address(BaseModel):
    address_1: str
    address_2: str
    city: str
    state: constr(min_length=2, max_length=2)
    zip_code: constr(min_length=5, max_length=5)

class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    address: Address
    phone_number: constr(min_length=10, max_length=10)
    email: str

class GetUserSchema(CreateUserSchema):
    user_id: conint(ge=0, le=99999)
    orders: List[Optional[UUID]]

class AppendOrdersSchema(BaseModel):
    orders: List[UUID]