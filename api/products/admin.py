from django.contrib import admin

from api.products.models import Category, Product, WerehouseProduct


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
                    "unit",
                    "is_active",
                ]
            },
        ),
        ("Time", {"classes": ["wide"], "fields": ["created_at", "updated_at"]}),
    ]


@admin.register(WerehouseProduct)
class WerehouseProduct(admin.ModelAdmin):
    list_display = ("werehouse", "product", "quantity", "updated_at")
    list_filter = ("werehouse__name",)
    list_editable = ("quantity",)
