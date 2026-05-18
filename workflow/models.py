from django.db import models
from accounts.models import Employee
from django.utils import timezone
from datetime import timedelta


class OrderWorkflow(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('accounts_approved', 'Accounts Approved'),
        ('management_approved', 'Management Approved'),
        ('warehouse_processing', 'Warehouse Processing'),
        ('dispatched', 'Dispatched'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    customer_name = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='submitted')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def is_delayed(self):
        return self.status != 'dispatched' and self.created_at < timezone.now() - timedelta(minutes=2)

    def __str__(self):
        return f"{self.customer_name} - {self.product}"
