from django.db import models
from accounts.models import Employee
from inventory.models import Product


class Delivery(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('delayed', 'Delayed'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    assigned_driver = models.ForeignKey(Employee, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    dispatch_date = models.DateTimeField()
    expected_delivery = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )

    def __str__(self):
        return f"{self.product.name} to {self.destination}"
