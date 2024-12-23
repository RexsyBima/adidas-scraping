from pydantic import BaseModel
from datetime import datetime

from enum import Enum


class Category(Enum):
    SHOES = "SHOES"
    CLOTHES = "CLOTHES"
    HAT = "HAT"


class Product(BaseModel):
    id: int
    sku: str
    name: str
    price: int
    release_date: datetime
    category: Category
