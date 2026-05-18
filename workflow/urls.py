from django.urls import path
from .views import create_order, order_list, approve_order

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('orders/', order_list, name='order_list'),
    path('approve/<int:order_id>/', approve_order, name='approve_order'),
]