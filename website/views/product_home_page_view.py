from django.shortcuts import render
from website.models import Product

def Product_Home_List_View(request):
    """Displays the last 20 products in the database on the home page.
     Author: Jessica Swift
     [
         {
             'title': 'abc'
         },
         {
             'title': 'def'
         },
         {
             'title': 'ghi'
         }
     ]
    """
    lastest_twenty_products = Product.objects.order_by('-id')[:20]
    print('lastest_twenty_products')
    return render(request, 'website/index.html', {'latest_products': latest_products})