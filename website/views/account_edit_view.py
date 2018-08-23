from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from website.forms import EditFormCustomer, EditFormUser
from website.models import Customer

@login_required
def edit_account_info(request, pk):
    """This will give the users a form where they can update their account information. On submit it will update their account information and save it to the database. 
    
    Author: Cashew Rose
    """
    customer_instance = get_object_or_404(Customer, pk=pk)

    ##Runs only when form is submitted
    if request.method == "POST":
        user_form = EditFormUser(request.POST, instance=request.user)
        customer_form = EditFormCustomer(request.POST, instance=customer_instance)

        ##Checks everything in both forms is filled out correctly and saves them with the new information. Sends them back to the main account page when finished.
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save()

            return redirect('website:account_home')

    else: 
        formCustomer= EditFormCustomer(instance=customer_instance)
        formUser = EditFormUser(instance=request.user)

    ##Displays the page with the forms    
    return render(request, 'account/account_edit.html', {'customer_form': formCustomer,
    'user_form': formUser})
