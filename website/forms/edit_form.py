from django import forms
from django.contrib.auth.models import User
from website.models import Customer

class EditFormCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('street', 'city', 'state', 'zip', 'phone')


class EditFormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')