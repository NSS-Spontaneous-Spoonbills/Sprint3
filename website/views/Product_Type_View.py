from django.shortcuts import render
from website.models import Product_Type

def Product_Type_List_View(request):
    """Displays all prducts in the database
    Author: Jessica Swift
    """
    product_types = Product_Type.objects.all()
    return render(request, 'Product_Type_List.html', {'product_types': product_types})