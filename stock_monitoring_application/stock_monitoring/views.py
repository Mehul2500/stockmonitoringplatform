
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import Stock
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, get_object_or_404
# accounts/views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



@csrf_exempt
def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				# Create Watchlist if it doesn't exist
				return redirect('dashboard')
			else:
				messages.error(request, 'Invalid username or password')
	else:
		form = AuthenticationForm()

	return render(request, 'registration/login.html', {'form': form})
@csrf_exempt
def logout_view(request):
	logout(request)
	return redirect('login')

@csrf_exempt
@login_required(login_url='login')
def dashboard(request):
	user = request.user
	stocks = Stock.objects.filter(user=user)
	print(stocks)
	stock_data = []
	
	for stock in stocks:
		url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock.symbol}&interval=1min&apikey=WFMPQ9B9RO7GVHTS"
		response = requests.get(url)
		
		if response.status_code == 200:
			data = response.json()
			time_series = data.get("Time Series (1min)")
			print(time_series)
			if time_series:
				latest_timestamp = max(time_series.keys())
				latest_price = time_series[latest_timestamp]["4. close"]
				stock_data.append({"symbol": stock.symbol, "price": latest_price})
	print(stock_data)
	context = {
		"watchlist": stock_data
	}
	return render(request, 'stock_monitoring/dashboard.html', context)


@csrf_exempt
@login_required(login_url='login')
def add_stock(request):
	if request.method == 'POST':
		symbol_name = request.POST.get('symbol')
		user = request.user

		# Check if the stock already exists for the user
		if Stock.objects.filter(symbol=symbol_name, user=user).exists():
			return redirect('dashboard')
		
		symbol_obj = Stock(symbol=symbol_name, user=user)
		symbol_obj.save()
		messages.success(request, f"The stock '{symbol_name}' added to your watchlist successfully.")

	return redirect('dashboard')





@csrf_exempt
@login_required(login_url='login')
def remove_stock(request, stock_symbol=None):
	if stock_symbol:
		stock = get_object_or_404(Stock, symbol=stock_symbol, user=request.user)
		stock.delete()
	return redirect('dashboard')
