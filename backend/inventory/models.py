from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Part(models.Model):
    sku = models.CharField("SKU", max_length=64, unique=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="parts")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"


class StockItem(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="stock_items")
    quantity = models.DecimalField(max_digits=12, decimal_places=3)
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.part} @ {self.location} ({self.quantity})"
