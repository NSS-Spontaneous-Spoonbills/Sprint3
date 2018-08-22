from django.shortcuts import render, get_object_or_404
from website.models import Product_Type, Product

def Product_Type_List_View(request):
    """Displays all products in the database
    Author: Jessica Swift

    [
        {
            'type_name': 'electronics',
            'count': 6,
            'products': [
                {
                    'title': 'laptop'
                },
                {
                    'title': 'apple watch'
                }
            ]
        },
        {
            'type_name': 'sporting goods',
            'count': 18,
            'products': [
                {
                    'title': 'bike'
                },
                {
                    'title': 'air mattress'
                    'title':
                }
            ]
        }

    ]
    """
    # final list that will get passed to template
    product_types = []
    for product_type in Product_Type.objects.all():
        # query the first 3 products for this product type
        first_three_products = product_type.product_set.all()[:3]
        # convert those 3 procuts to a list of dicts
        # inner product list inside each product type dict
        dict_product_list = [
            {'title': product.title, 'id': product.id}
            # get title & id for products in first 3 bc they are data objs to start w/
            for product in first_three_products
        ]
        # outter product list
        product_type_dict = {
            'type_name': product_type.type_name,
            # filter the product by type and count total in each category
            'count': Product.objects.filter(type_id=product_type.id).count(),
            'products': dict_product_list,
            'type_id': product_type.id
        }
        # append product type dict to final product types list
        product_types.append(product_type_dict)
    return render(request, 'product/Product_Type_List.html', {'product_types': product_types})


def product_category_view(request, pk):
    """ displays all products in a single category

        Author: David Paul
    """
    product_category = get_object_or_404(Product_Type, pk=pk)
    products = Product.objects.filter(type_id=pk)
    return render(request, 'product/product_category.html', {'product_category': product_category, 'products': products})
