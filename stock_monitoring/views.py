
# # from django.shortcuts import render
# # from django.views.generic import ListView
# # stock_monitoring/views.py

# from django.shortcuts import render
# from .models import Watchlist
# # from django.contrib.auth.decorators import login_required
# import requests

# # def index(request):
# # 	return render(request, "stock_monitoring/stock_list.html" )




# def dashboard(request):
#     watchlist = Watchlist.objects.filter(user=request.user)
#     stock_data = []

#     for item in watchlist:
#         symbol = item.symbol
#         url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey=WFMPQ9B9RO7GVHTS"
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             latest_price = data["Time Series (1min)"]["2023-05-18 16:00:00"]["4. close"]
#             stock_data.append({"symbol": symbol, "price": latest_price})

#     context = {
#         "watchlist": stock_data
#     }
#     return render(request, 'dashboard.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import Watchlist, Stock, Symbol
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, get_object_or_404



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
				Watchlist.objects.get_or_create(user=user)
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
    try:
        watchlist = Watchlist.objects.get(user=user)
        symbols = watchlist.symbols.all()

        stock_data = []

        for symbol in symbols:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey=WFMPQ9B9RO7GVHTS"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                time_series = data.get("Time Series (1min)")
                if time_series:
                    latest_timestamp = max(time_series.keys())
                    latest_price = time_series[latest_timestamp]["4. close"]
                    stock_data.append({"symbol": symbol, "price": latest_price})

        context = {
            "watchlist": stock_data
        }
    except Watchlist.DoesNotExist:
        watchlist = None
        context = {
            "watchlist": []
        }

    return render(request, 'stock_monitoring/dashboard.html', context)


@csrf_exempt
@login_required(login_url='login')
def add_stock(request):
    if request.method == 'POST':
        symbol_name = request.POST.get('symbol')
        
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol_name}&apikey=WFMPQ9B9RO7GVHTS"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            quote_data = data.get("Global Quote")
            if quote_data:
                latest_price = quote_data["05. price"]
                symbol_obj, _ = Symbol.objects.get_or_create(name=symbol_name)
                
                user = request.user
                watchlist, _ = Watchlist.objects.get_or_create(user=user)
                
                # Check if the symbol already exists in the watchlist
                if symbol_obj in watchlist.symbols.all():
                    messages.warning(request, f"{symbol_name} already exists in your watchlist.")
                else:
                    watchlist.symbols.add(symbol_obj)
                    watchlist.save()

                # Fetch the complete watchlist again
                watchlist_symbols = watchlist.symbols.all()
                stock_data = []

                for symbol in watchlist_symbols:
                    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey=WFMPQ9B9RO7GVHTS"
                    response = requests.get(url)
                    if response.status_code == 200:
                        data = response.json()
                        time_series = data.get("Time Series (1min)")
                        if time_series:
                            latest_timestamp = max(time_series.keys())
                            latest_price = time_series[latest_timestamp]["4. close"]
                            stock_data.append({"symbol": symbol, "price": latest_price})

                messages.success(request, f"{symbol_name} added to watchlist successfully.")
                context = {
                    "watchlist": stock_data
                }
                return render(request, 'stock_monitoring/dashboard.html', context)
            else:
                messages.error(request, f"Invalid stock symbol: {symbol_name}. Please enter a valid symbol.")
        else:
            messages.error(request, f"Failed to fetch stock data. Please try again.")
    
    return redirect('dashboard')

# @csrf_exempt
# @login_required(login_url='login')
# def add_stock(request):
# 	if request.method == 'POST':
# 		symbol_name = request.POST.get('symbol')
# 		symbol_obj, created = Symbol.objects.get_or_create(name=symbol_name)
		
# 		if created:
# 			# Do any additional processing or validation if needed
# 			pass
		
# 		user = request.user
# 		watchlist, _ = Watchlist.objects.get_or_create(user=user)
# 		watchlist.symbols.add(symbol_obj)
# 		# Save the watchlist to ensure the added stock is persisted
# 		watchlist.save()

# 		return redirect('dashboard')
 
		
# 		# return redirect('dashboard')
# 	# if request.method == 'POST':
# 	# 	symbol = request.POST.get('symbol')

# 	# 	try:
# 	# 		stock = Stock.objects.get(symbol=symbol)
# 	# 		watchlist = Watchlist.objects.get(user=request.user)
# 	# 		watchlist.stocks.add(stock)
# 	# 		messages.success(request, f"{symbol} added to watchlist successfully.")
# 	# 	except Stock.DoesNotExist:
# 	# 		messages.error(request, f"Invalid stock symbol: {symbol}. Please enter a valid symbol.")
# 	# 	except Watchlist.DoesNotExist:
# 	# 		messages.error(request, "Watchlist does not exist.")

# 	# 	return redirect('dashboard')
	
	
# 	return render(request, 'stock_monitoring/add_stock.html')

@csrf_exempt
@login_required(login_url='login')
def remove_stock(request, stock_id=None):
	if stock_id:
		watchlist = get_object_or_404(Watchlist, user=request.user)
		stock = get_object_or_404(Stock, id=stock_id)
		watchlist.stocks.remove(stock)
	return redirect('dashboard')
