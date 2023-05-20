# stockmonitoringplatform
##Steps: 

: Design a stock monitoring platform where a user can login and monitor stock information.
Requirements:
• The platform should allow users to create and manage their own watchlists of stock symbols 
(e.g., MSFT, GOOG).
• The platform should display a dashboard with the latest stock values of the symbols on the 
user’s watchlist.
• The platform should be able to handle multiple users concurrently, each having different 
watchlists.
• The platform should use a DB of your choice (e.g., MySQL/PostgreSQL/MongoDB) to store the 
user and watchlist data.
• The platform should use a secure and simple authentication mechanism for the users.
• The platform should use https://www.alphavantage.co as an API to pull stock information. The 
dashboard should show the latest stock price as returned by the TIME_SERIES_INTRADAY 
endpoint.