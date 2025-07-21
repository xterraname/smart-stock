from typing import List
from django.contrib import admin
from django.urls import path
from ninja import Router
from ninja_jwt.authentication import JWTAuth

from api.stock.models import Werehouse
from api.stock.schema import WerehouseOut


router = Router(auth=JWTAuth())


@router.get("/", response=List[WerehouseOut])
def add(request):
    werehouses = Werehouse.objects.all()
    return werehouses
