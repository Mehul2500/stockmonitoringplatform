
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

@csrf_exempt


def login_view(request):
    # Login view logic here
    if request.method == 'POST':
        # Process login form data
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Invalid credentials, show error message
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Render login form
        return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    watchlist = ['MSFT', 'GOOG']  
    stock_data = []

    for symbol in watchlist:
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
    return render(request, 'stock_monitoring/dashboard.html', context)

