from django import forms
from .models import OrderWorkflow


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderWorkflow
        fields = [
            'customer_name',
            'product',
            'quantity',
            'priority',
            'created_by'
        ]