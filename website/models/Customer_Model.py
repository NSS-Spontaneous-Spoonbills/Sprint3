from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Customer(models.Model):
    create_date = models.CharField(max_length=15, auto_now_add=False, default='2018-07-16')
    last_signon = models.CharField(max_length=15, auto_now_add=False, default='2018-07-16')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    street = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.IntegerField(max_length=15)
    phone = models.IntegerField(max_length=15)
    username = models.CharField(max_length=25)


    def __str__(self):
        return f'{self.username}'
