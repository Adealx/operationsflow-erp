from django.shortcuts import render
from accounts.models import Employee
from tasks.models import Task
from inventory.models import Product
from delivery.models import Delivery


def dashboard_home(request):
    context = {
        'employee_count': Employee.objects.count(),
        'pending_tasks': Task.objects.filter(status='pending').count(),
        'completed_tasks': Task.objects.filter(status='completed').count(),
        'overdue_tasks': 99,
        'low_stock': Product.objects.filter(quantity__lte=20).count(),
        'delayed_deliveries': Delivery.objects.filter(status='delayed').count(),
        'delivered': Delivery.objects.filter(status='delivered').count(),
    }

    return render(request, 'dashboard/home.html', context)
