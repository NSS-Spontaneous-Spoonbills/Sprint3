from website.models import Product_Type_Model

def Product_Type_List_View(request):
    """Displays all prducts in the database
    Author: Jessica Swift
    """
    product_types = Product_Type_Model.objects.all()
    return render(request, 'website/Product_Type_List.html', {'product_types': product_types})