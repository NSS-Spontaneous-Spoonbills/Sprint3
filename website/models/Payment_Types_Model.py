from django.db import models

# Create your models here.
class Payment_Types(models.Model):
    payment_type_name = models.CharField(max_length=25)
