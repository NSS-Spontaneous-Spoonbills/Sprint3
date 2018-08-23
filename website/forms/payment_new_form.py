from django import forms
from website.models import Payment_Option, Customer

class Payment_New_Form(forms.ModelForm):
    """
    Form to create a new payment type

    Author: Jacob Smith
    """
    class Meta:
        model = Payment_Option
        fields = ('payment_type_id', 'account_number', 'customer_id')

    def __init__(self, user, *args, **kwargs):
        """
        init method used to help filter foreign key option on fields.
        takes an argument called user that option_view passes via 'request.user'
        customer_id grabs the queryset and filters the user against the logged in user via the .filter method
        Author: Jacob Smith
        """
        super(Payment_New_Form, self).__init__(*args, **kwargs)
        self.fields['customer_id'].queryset = Customer.objects.filter(user=user.id)