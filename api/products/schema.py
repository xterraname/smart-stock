from datetime import datetime
from ninja import Schema
from pydantic.types import UUID4
from pydantic import AnyUrl


class CategorySchema(Schema):
    id: int
    name: str
    code: str


class ProductSchema(Schema):
    id: UUID4
    barcode: str
    name: str
    description: str = None

    category: CategorySchema
    price: float
    unit: str
    image_url: AnyUrl | None

    is_active: bool

    created_at: datetime
    updated_at: datetime
