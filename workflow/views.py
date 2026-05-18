from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import OrderWorkflow


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/workflow/orders/')
    else:
        form = OrderForm()

    return render(request, 'workflow/create_order.html', {'form': form})


def order_list(request):
    query = request.GET.get('q')
    status = request.GET.get('status')

    orders = OrderWorkflow.objects.all()

    if query:
        orders = orders.filter(customer_name__icontains=query)

    if status:
        orders = orders.filter(status=status)

    return render(request, 'workflow/order_list.html', {
        'orders': orders
    })


def approve_order(request, order_id):
    order = get_object_or_404(OrderWorkflow, id=order_id)

    if order.status == 'submitted':
        order.status = 'accounts_approved'
    elif order.status == 'accounts_approved':
        order.status = 'management_approved'
    elif order.status == 'management_approved':
        order.status = 'warehouse_processing'
    elif order.status == 'warehouse_processing':
        order.status = 'dispatched'

    order.save()

    return redirect('/workflow/orders/')

    
