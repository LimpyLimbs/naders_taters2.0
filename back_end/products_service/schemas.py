from enum import Enum
from typing import List
from pydantic import BaseModel, conint

class Flavor(str, Enum):
    barbeque = 'barbeque'
    sour_cream_and_onion = 'sour_cream_and_onion'
    salt_and_vinegar = 'salt_and_vinegar'
    classic = 'classic'
    cheddar = 'cheddar'
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

class InventorySchema(BaseModel):
    flavor: Flavor
    size: Size
    quantity: int

class UpdateInventorySchema(BaseModel):
    items: List[InventorySchema]