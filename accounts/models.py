from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    ROLE_CHOICES = [
        ('sales_rep', 'Sales Rep'),
        ('accounts_manager', 'Accounts Manager'),
        ('management', 'Management'),
        ('warehouse_officer', 'Warehouse Officer'),
        ('logistics_officer', 'Logistics Officer'),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
