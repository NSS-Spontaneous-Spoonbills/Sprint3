from django.shortcuts import render, get_object_or_404
from website.models import Product, Customer, Product_Type


def Product_Detail_View(request, pk):
    """Displays details about a specific product
    Author: Erin Meaker
    """

    product = get_object_or_404(Product, pk=pk)
    sellers = Customer.objects.all()
    product_types = Product_Type.objects.all()

    return render(request, 'product/detail.html', {'product': product, 'sellers': sellers, 'product_types': product_types})

# seller_id should return the name
# type id should return the product type
