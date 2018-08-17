from django.db import models

# Create your models here.
class Ordered_Products(models.Model):
    order_id = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
