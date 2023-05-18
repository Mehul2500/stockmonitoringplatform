# stock/urls.py

# from django.urls import path
from . import views
# stock_monitoring/urls.py

from django.urls import path



app_name = 'stock_monitoring'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
