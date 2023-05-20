
from django.db import models
from django.contrib.auth.models import User
# from .symbol import Symbol


class Stock(models.Model):
    symbol = models.CharField(max_length=50)
    # Add any other fields related to stock information

class Symbol(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # Add other fields as needed

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbols = models.ManyToManyField(Symbol)

# class Watchlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     symbol = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.user.username}'s Watchlist - {self.symbol}"
