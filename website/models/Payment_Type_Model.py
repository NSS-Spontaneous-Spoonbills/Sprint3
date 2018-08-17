from django.db import models

# Create your models here.
class Payment_Type(models.Model):
    payment_type_name = models.CharField(max_length=25)
