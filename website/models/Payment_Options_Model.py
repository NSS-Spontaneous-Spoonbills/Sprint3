from django.db import models

# Create your models here.
class Ordered_Products(models.Model):
    customer_id = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
    )
    payment_type_id = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    account_number = models.CharField()

    def __str__(self):
        return f'{self.account_number}'
