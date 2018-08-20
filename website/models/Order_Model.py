from django.db import models
from django.db.models import *


class Order(models.Model):
    customer_id = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE
    )
    payment_id = models.ForeignKey(
        "Payment_Option",
        on_delete=models.CASCADE
    )
    is_complete = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    order_date = models.CharField(max_length=15, default='2018-07-16')
    total_amount = models.IntegerField()

    def __str__(self):
        return f"Order Date: {self.order_date} | Total: {self.total_amount}"
