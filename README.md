Grocery Management System
This project is a Grocery Management System that allows users to manage grocery items, create carts, and handle orders efficiently. The system supports both user and admin functionalities and provides features such as user registration, login, adding items to a cart, checking out, and viewing order history. Admins can manage groceries and view the order history of all users.

Features
User Functionality
User Registration:

Users can register with a username, password, and mobile number.
Ensures that usernames are unique.
User Login:

Secure login with username and password.
Cart Management:

Add items from the grocery list to the cart.
Edit or clear items in the cart.
View the total price and proceed to checkout.
Order History:

View past orders with details including item name, quantity, and total price.
Checkout:

Deducts the ordered quantity from the available stock.
Stores purchase details in the orders.json file.
Admin Functionality
Admin Login:

Secure login with username and password.
Manage Groceries:

Add new grocery items by specifying their name, quantity, price, and type.
Update the available quantity and price of existing items.
View Order History:

View order history for specific users or all users.
Files and Data
users.json: Stores user data (username, password, and mobile number).
admin.json: Stores admin login credentials.
grocery.json: Stores grocery items categorized by type.
cart.json: Stores user cart data, including items added by users.
orders.json: Stores completed orders with details about the user, items purchased, and total cost.
Requirements
Python 3.7+
No additional libraries are required as it uses Python's built-in json module for data handling.
How to Use
Run the Script:

bash
Copy code
python grocery_management.py
Choose Your Role:

Login/Register as a user or login as an admin.
User Operations:

Add items to your cart, view/edit the cart, and proceed to checkout.
View your order history anytime.
Admin Operations:

Update grocery lists or add new items.
View the order history of any user.
Example Workflow
For Users:
Register or log in as a user.
View the list of groceries and add desired items to your cart.
Edit or clear the cart as needed.
Proceed to checkout to confirm your order.
View your order history for past purchases.
For Admins:
Log in as an admin.
Add or update grocery items in the inventory.
View order history for any user to track purchases.
Customization
Update grocery.json to pre-load groceries into the system.
Modify admin credentials in admin.json for new admin accounts.
Folder Structure
bash
Copy code
|-- grocery_management.py  # Main script
|-- users.json             # Stores user information
|-- admin.json             # Stores admin credentials
|-- grocery.json           # Stores grocery inventory
|-- cart.json              # Stores user cart data
|-- orders.json            # Stores order history
Future Enhancements
Integrate a database for better scalability.
Implement a graphical user interface (GUI).
Add payment gateway integration for real-world usage.
Include discount codes and promotional offers.
