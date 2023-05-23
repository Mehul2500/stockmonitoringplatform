# Stock Monitoring Application

This is a web application built with Django for monitoring stocks. It allows users to create an account, add stocks to their watchlist, and remove stocks from the watchlist.

## Installation

Follow these steps to set up the application locally:

1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd stock_monitoring_application
   ```

3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - For macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - For Windows:
     ```
     venv\Scripts\activate
     ```

5. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Set up the database:
   ```
   python manage.py migrate
   ```

7. Create a superuser (admin) account:
   ```
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```
   python manage.py runserver
   ```

9. Open your web browser and go to [http://localhost:8000](http://localhost:8000) to access the application.

## Getting Started

To use the stock monitoring platform, follow these steps:

1. **Create an Account**: Start by clicking on the "Create an Account" link on the login page. Fill out the registration form with your desired username and password. Click "Register" to create your account.

2. **Login**: Once you have registered, you can log in with your credentials on the login page.

3. **Dashboard**: After logging in, you will be redirected to the dashboard. Here, you can view and manage your stock watchlist.

4. **Add Stocks**: To add a stock to your watchlist, locate the input field provided on the dashboard. Enter the stock symbol (e.g., MSFT for Microsoft, GOOG for Google) and click the "Add Stocks" button. The stock will be added to your watchlist.

5. **Remove Stocks**: If you want to remove a stock from your watchlist, navigate to the watchlist section on the dashboard. Next to each stock, you will find a "Remove" button. Click on it to remove the corresponding stock from your watchlist.

6. **Log Out**: When you are done using the platform, you can log out by clicking the "Log Out" button in the navigation bar. This will securely log you out of your account.

Please note that the stock monitoring platform uses the Alpha Vantage API to retrieve stock information. The latest stock values displayed on the dashboard are fetched from the API's TIME_SERIES_INTRADAY endpoint.
