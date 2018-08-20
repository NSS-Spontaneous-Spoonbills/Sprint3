from django.db import models


class Payment_Type(models.Model):
    payment_type_name = models.CharField(max_length=25)
