from typing import List, Optional
from pydantic import Field
from ninja import Schema


class ProductFilters(Schema):
    p_werehouse__werehouse: int = Field(alias="werehouse")
    name__icontains: Optional[str] = Field(None, alias="name")
    barcode__icontains: Optional[str] = Field(None, alias="barcode")
    category__in: Optional[List[str]] = Field(None, alias="category")
