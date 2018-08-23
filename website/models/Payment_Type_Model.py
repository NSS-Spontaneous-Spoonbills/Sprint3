from django.db import models


class Payment_Type(models.Model):
    payment_type_name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.payment_type_name}'
