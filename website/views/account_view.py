from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required()
def my_account_home(request):
    """[summary]
    
    Arguments:
        request {[type]} -- [description]
    """

    return render(request, 'account/my_account_index.html', {})


# def wall(request):

#     return HttpResponse("Invalid login details supplied.")

