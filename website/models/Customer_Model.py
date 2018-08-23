from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    last_signon = models.CharField(blank=True, max_length=15, default='2018-07-16')
    street = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip = models.PositiveSmallIntegerField(blank=True)
    phone = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'
