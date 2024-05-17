from enum import Enum
from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, conint

class Flavor(str, Enum):
    barbeque = 'barbeque'
    sour_cream_and_onion = 'sour_cream_and_onion'
    salt_and_vinegar = 'salt_and_vinegar'
    classic = 'classic'
    cheddar = 'cheddar'
    pizza = 'pizza'
    jalapano = 'jalapano'
    kettle_cooked = 'kettle_cooked'
    dill_pickle = 'dill_pickle'
    salt_and_pepper = 'salt_and_pepper'
    
    def __str__(self):
        return self.value

class Size(str, Enum):
    small = 'small'
    medium = 'medium'
    large = 'large'
    
    def __str__(self):
        return self.value
    
class Status(str, Enum):
    received = 'received'
    processesing = 'processing'
    shipped = 'shipped'
    delivered = 'delivered'
    cancelled = 'cancelled'

    def __str__(self):
        return self.value

class ItemSchema(BaseModel):
    flavor: Flavor
    size: Size
    quantity: Optional[conint(ge=1, strict=True)] = 1

class CreateOrderSchema(BaseModel):
    items: List[ItemSchema]

class UpdateOrderSchema(CreateOrderSchema):
    order_id: UUID
    created: datetime
    status: Status
    
class GetOrderSchema(UpdateOrderSchema):
    price: float

class MessageSchema(BaseModel):
    message: str