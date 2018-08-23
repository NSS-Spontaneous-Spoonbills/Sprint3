from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from website.forms import EditFormCustomer, EditFormUser
from website.models import Customer

@login_required
def edit_account_info(request, pk):
    """This will either redirect the user to the their account home page view or it will redirect them to login page.
    
    Author: Cashew Rose
    """
    customer_instance = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        user_form = EditFormUser(request.POST, instance=request.user)
        customer_form = EditFormCustomer(request.POST, instance=customer_instance)

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save()

            return redirect('website:account_home')

    else: 
        formCustomer= EditFormCustomer(instance=request.user)
        formUser = EditFormUser(instance=request.user)
    return render(request, 'account/account_edit.html', {'formC': formCustomer,
    'formU': formUser})
