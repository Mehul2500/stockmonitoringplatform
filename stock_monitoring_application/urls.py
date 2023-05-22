"""
URL configuration for stock_monitoring_application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from stock_monitoring import views

# from django.urls import include, path

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('accounts/login/', views.login_view, name='login'),
#     path('accounts/logout/', views.logout_view, name='logout'),
#     path('', include('stock_monitoring.urls'))


# ]
from django.contrib import admin
from django.urls import path
# from stock_monitoring.views import dashboard, login_view, logout_view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/login/', login_view, name='login'),
#     path('accounts/logout/', logout_view, name='logout'),
#     path('', dashboard, name='dashboard'),
# ]

# from django.contrib import admin
# from django.urls import path
from stock_monitoring.views import dashboard, login_view, logout_view, add_stock, remove_stock

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_stock/', add_stock, name='add_stock'),
    path('remove_stock/<str:stock_id>/', remove_stock, name='remove_stock'),
    
]
