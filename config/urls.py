from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from api.stock.api import router as stock_router
from core.views import index_view


api = NinjaExtraAPI(
    title="SmartStock API",
    version="1.0.0",
    description="REST API backend of the service that allows for efficient warehouse product management, inventory control, order processing, delivery, and analytics.",
    docs_url="/docs/",
)

api.register_controllers(NinjaJWTDefaultController)
api.add_router('stock', stock_router)

urlpatterns = [
    path("", index_view, name="home"),
    path('supersmart/', admin.site.urls),
    path('api/', api.urls)
]
