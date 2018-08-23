from django import forms
from website.models import Payment_Option


class Payment_Option_Form(forms.ModelForm):
    """
    Form to edit a new payment type

    Author: Jacob Smith
    """
    class Meta:
        model = Payment_Option
        fields = ('payment_type_id', 'account_number')

