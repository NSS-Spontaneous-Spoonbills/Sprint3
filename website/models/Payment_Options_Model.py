from django.db import models
from django.db.models import *

# Create your models here.
class Payment_Options(models.Model):
    customer_id = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,
    )
    payment_type_id = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
    )
    account_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.account_number}'
