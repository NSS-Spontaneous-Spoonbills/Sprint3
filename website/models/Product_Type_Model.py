from django.db import models


class Product_Type(models.Model):
    type_name = models.CharField(max_length=20)
