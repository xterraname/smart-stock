from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from api.stock.models import Werehouse


@admin.register(Werehouse)
class WerehouseAdmin(GISModelAdmin):
    list_display = ['name', 'location']
