from django.contrib.auth.models import Customer, Product_Type
from django.db import models

# Create your models here.
class Product(models.Model):
    seller_id = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )
    type_id = models.ForeignKey(
        Product_Type,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.title}'
