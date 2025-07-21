import uuid
from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    RegexValidator,
    MaxLengthValidator,
    MinLengthValidator,
)


category_code_validator = RegexValidator(r"^\d{3}[a-z]{1}")
barcode_validators = [
    MinLengthValidator(13),
    MaxLengthValidator(16),
    RegexValidator(r"^\d+"),
]


class Category(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(
        max_length=4,
        unique=True,
        validators=[category_code_validator],
        help_text="The category code consists of 3 numbers "
        "and one English letter. Example: 526f, 392b",
    )
    
    def __str__(self):
        return f"{self.name} [{self.code}]"


class Product(models.Model):
    class Units(models.TextChoices):
        PCS = "PCS", _("Piece(s)")
        KG = "KG", _("Kilogram")
        G = "G", _("Gram")
        L = "L", _("Liter")
        ML = "ML", _("Milliliter")
        BOX = "BOX", _("Box")
        M = "M", _("Meter")
        CM = "CM", _("Centimeter")
        SET = "SET", _("Set")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    barcode = models.CharField(
        max_length=16,
        validators=barcode_validators,
        unique=True,
        db_index=True,
        help_text="A barcode consists of 13-16 digits.",
    )
    name = models.CharField(max_length=128)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )

    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=8, choices=Units.choices)
    quantity = models.PositiveIntegerField(default=0)
    
    is_active = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description="Quantity")
    def quantity_unit(self):
        return f"{self.quantity} {self.unit}"
    
    def __str__(self):
        return f"{self.name} ({self.unit.title()}) [{self.barcode}]"
