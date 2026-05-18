from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField(default=20)

    def stock_status(self):
        if self.quantity == 0:
            return "Out of Stock"
        elif self.quantity <= self.reorder_level:
            return "Low Stock"
        return "Healthy"

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_changed = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity_changed})"
