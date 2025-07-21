from django.contrib import admin

from api.products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")
    ordering = ("code",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "barcode",
        "category",
        "price",
        "quantity_unit",
    )
    list_filter = ("is_active", "unit")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = [
        (None, {"fields": ["name", "description"]}),
        (
            "Product",
            {
                "fields": [
                    "barcode",
                    "category",
                    "price",
                    "quantity",
                    "unit",
                    "is_active",
                ]
            },
        ),
        ("Time", {"classes": ["wide"], "fields": ["created_at", "updated_at"]}),
    ]
