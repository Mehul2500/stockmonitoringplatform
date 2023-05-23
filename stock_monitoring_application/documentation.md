## Backend Documentation

#### Stock Model
The `Stock` model represents a stock entry in the user's watchlist. It has the following fields:

- `user`: This field is a foreign key to the `User` model provided by Django's authentication framework. It establishes a one-to-many relationship between users and their stocks, indicating that a user can have multiple stocks in their watchlist.
- `symbol`: This field is a character field with a maximum length of 50. It stores the symbol of the stock.

The `__str__` method is overridden to provide a human-readable representation of the stock object, which, in this case, is the stock symbol.

### Schema

The schema for the stock monitoring application includes the following table:

#### Stock Table
| Field   | Type       | Description                                      |
|---------|------------|--------------------------------------------------|
| user    | ForeignKey | The user associated with the stock entry          |
| symbol  | CharField  | The symbol of the stock                           |

The `Stock` table is used to store the user's stock watchlist. Each row in the table represents a stock entry associated with a specific user. The `user` field establishes a foreign key relationship with the `User` model, linking each stock entry to the corresponding user.

The schema design ensures the association between users and their stocks, allowing for efficient management of user-specific watchlists.

These schema choices facilitate the storage and retrieval of stock data for each user, enabling the application to manage personalized watchlists effectively.


#### Registration View
The `registration` view handles the registration process for new users. It validates the registration form data, creates a new user, logs in the user, and redirects to the dashboard upon successful registration.

#### Login View
The `login_view` view handles user authentication. It verifies the user's credentials, logs the user in, and redirects to the dashboard upon successful login.

#### Logout View
The `logout_view` view handles user logout. It logs the user out and redirects to the login page.

#### Dashboard View
The `dashboard` view displays the user's stock watchlist on the dashboard page. It retrieves the user's stocks from the database and fetches the latest stock prices using the Alpha Vantage API. The retrieved stock data is passed to the template for rendering.

#### Add Stock View
The `add_stock` view handles the process of adding a stock to the user's watchlist. It validates the stock symbol entered by the user, creates a new stock object associated with the user, and saves it to the database.

#### Remove Stock View
The `remove_stock` view handles the process of removing a stock from the user's watchlist. It receives the stock symbol as a parameter, retrieves the corresponding stock object from the database, and deletes it.

### Implementation Details

- The stock monitoring application utilizes Django's built-in authentication framework for user registration, login, and logout functionalities.
- User registration is handled using the `RegistrationForm` form, and the registered user is automatically logged in upon successful registration.
- User authentication is performed using the `AuthenticationForm` form, and the user is logged in upon successful login.
- User logout is achieved by invoking the `logout` function provided by Django.
- The `dashboard` view fetches the latest stock prices using the Alpha Vantage API. It constructs the API URL based on the stock symbols in the user's watchlist and retrieves the corresponding data.
- The `add_stock` view checks if the stock already exists in the user's watchlist before adding it. If the stock already exists, it redirects the user to the dashboard without duplicating the entry.
- The `remove_stock` view retrieves the stock object based on the stock symbol and the logged-in user. If the stock exists, it deletes the object from the database.
- The application leverages Django's model-view-template (MVT) architecture. Views handle the business logic, interact with the models to perform database operations, and pass data to the templates for rendering.
- The application uses the `requests` library to make HTTP requests to the Alpha Vantage API and retrieve stock data in JSON format.
- Error handling is implemented to handle cases such as invalid user credentials, duplicate stock entries, and API request failures.
- The application utilizes Django's built-in messaging framework to display success and error messages to the user.

These design choices and implementation details ensure a robust and functional backend for the stock monitoring application.