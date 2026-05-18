from django.shortcuts import render
from accounts.models import Employee
from tasks.models import Task
from inventory.models import Product
from delivery.models import Delivery
from workflow.models import OrderWorkflow


def home(request):
    context = {
        'employee_count': Employee.objects.count(),
        'overdue_tasks': Task.objects.filter(status='Pending').count(),
        'low_stock': Product.objects.filter(quantity__lt=20).count(),
        'delayed_deliveries': Delivery.objects.filter(status='Delayed').count(),

        'pending_tasks': Task.objects.filter(status='Pending').count(),
        'completed_tasks': Task.objects.filter(status='Completed').count(),

        'delivered': Delivery.objects.filter(status='Delivered').count(),

        'total_orders': OrderWorkflow.objects.count(),
        'delayed_orders': sum(order.is_delayed() for order in OrderWorkflow.objects.all()),
        'dispatched_orders': OrderWorkflow.objects.filter(status='dispatched').count(),
        'pending_orders': OrderWorkflow.objects.exclude(status='dispatched').count(),
    }

    return render(request, 'dashboard/home.html', context)
