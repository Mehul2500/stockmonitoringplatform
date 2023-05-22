from django.contrib import admin

# Register your models here.
from .models import Stock, Symbol, Watchlist

admin.site.register(Stock)
admin.site.register(Symbol)
admin.site.register(Watchlist)
