from typing import List
from ninja import Query, Router
from ninja.pagination import paginate
from ninja_jwt.authentication import JWTAuth

from api.products.models import Category, Product
from api.products.schema import CategorySchema, ProductSchema
from api.products.filters import ProductFilters


router = Router(auth=JWTAuth())


@router.get("/categories", response=List[CategorySchema])
def get_categories(request):
    categories = Category.objects.all()
    return categories


@router.get("/", response=List[ProductSchema])
@paginate
def get_products(request, filters: Query[ProductFilters]):
    print(filters.dict(exclude_none=True))
    products = Product.objects.filter(**filters.dict(exclude_none=True))
    return products
