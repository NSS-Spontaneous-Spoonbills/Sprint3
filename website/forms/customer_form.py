from django import forms
from website.models import Customer

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('street', 'city', 'state', 'zip', 'phone')
