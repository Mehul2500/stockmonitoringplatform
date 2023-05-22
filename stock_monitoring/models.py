from django.contrib.auth.models import User
from django.db import models

class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=50)

    def __str__(self):
        return self.symbol
