from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from api.stock.api import router as stock_router


api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router('stock', stock_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
