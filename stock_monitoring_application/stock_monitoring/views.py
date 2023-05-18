
from django.shortcuts import render
from django.views.generic import ListView

def index(request):
	return render(request, "stock_monitoring/stock_list.html" )