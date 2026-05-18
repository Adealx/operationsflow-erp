from django.db import models
from accounts.models import Employee
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def save(self, *args, **kwargs):
        if self.deadline < timezone.now() and self.status != 'completed':
            self.status = 'overdue'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
