from django.shortcuts import render, get_object_or_404
from website.models import Customer, Payment_Option, Payment_Type
from website.forms import Payment_Option_Form


def payment_list_view(request):
    """Displays all payments for customer in the database
    Author: Jacob Smith
    """

    payments = Payment_Option.objects.filter()
    return render(request, 'account/payment_option_list.html', {'payments': payments})


# def payment_detail_view(request, pk):
#     """Displays details about a specific payment type
#     Author: Jacob Smith
#     """

#     payment = get_object_or_404(Payment_Option, pk=pk)
#     return render(request, 'website/payment_option_detail.html', {'payment': payment})


# def payment_update_view(request, pk):
#     """payment_option wil handle rendering the form view for payment option when the 'My Account page renders'
#         It will require a form that has an affordance for:
#             Card Name: <input field> Ex. 'My Airline Rewards Card' or 'My Ascend Credit Union Card'
#             Payment Type: <dropdown> Ex. Visa, Mastercard, etc.
#             Account #: <input field> Ex. 54310
#         Author: Jacob Smith
#     """

#     if request.method == 'POST':
#         form = Payment_Option_Form(requst.POST)
#         new_payment = form.save(commit=False)
#         new_payment.save()
#         return redirect('payment_option', pk=new_payment.pk)
#     else:
#         form = Payment_Option_Form()
#     return render(request, 'website/payment_option_update.html', {'form': form})



