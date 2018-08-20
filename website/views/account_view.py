from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def my_account_home(request):
    """[summary]
    
    Arguments:
        request {[type]} -- [description]
    """


    return render(request, 'account/my_account_index.html', {})



