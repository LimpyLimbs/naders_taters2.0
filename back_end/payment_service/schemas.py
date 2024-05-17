from enum import Enum
from pydantic import BaseModel

class CreditCardCompany(Enum):
    american_express = 'american_express'
    discover = 'discover'
    visa = 'visa'
    master_card = 'master_card'

class CreditCardSchema(BaseModel):
    credit_card_company: CreditCardCompany
    credit_card_number: int
    expiration_date: int
    security_code: int