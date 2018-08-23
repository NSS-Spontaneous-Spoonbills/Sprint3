from django.shortcuts import render, get_object_or_404
from website.models import Order


def order_history(request, pk):
    """ displays history of orders by customer

        Author: David Paul
    """
    orders = Order.objects.filter(customer_id=pk)
    return render(request, 'orders/order_history', {'orders': orders})
