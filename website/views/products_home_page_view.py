from django.shortcuts import render
from website.models import Product_Model, Product

def Product_Home_List_View(request):
     """Displays the last 20 products in the database on
        the home page.
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

product_list = []
for product_list in Product_Model.objects.all():
    last_twenty_products = product_type.product_set.all()[:20]
    dict_product_list = {
        {'title': product.title, 'id': product.id}
        for product in last_twenty_products
    }
return render(request, 'product/')