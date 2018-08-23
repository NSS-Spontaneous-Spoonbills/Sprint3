from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def my_account_home(request):
    """This will either redirect the user to the their account home page view or it will redirect them to login page.
    
    Author: Cashew Rose
    """

    return render(request, 'account/my_account_index.html')
