import json
import os
data='users.json'
data2='admin.json'
data3='grocery.json'
data4='cart.json'
def loadusers():
    try:
        with open(data,'r') as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
def loadcart():
    try:
        with open(data4,'r') as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
def loadadmin():
    try:
        with open(data2,'r') as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return [] 
def loadgroceries():
    try:
        with open(data3,'r') as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
def savegrocery(grocery):
    with open(data3,'w') as file:
        json.dump(grocery,file,indent=4)
def saveusers(users):
    with open(data,'w') as file:
        json.dump(users,file,indent=4)
def savecart(cart):
    with open(data4,'w') as file:
        json.dump(cart,file,indent=4)
def login():

    users=loadusers()
    error=0
    while True:
        os.system("cls")
        if error==1:
            print("Incorrect Details, Try again!")
        username=input("Enter Username:")
        password=input("Enter Password:")
        flag=0
        for i in users:
            if i['username']==username and i['password']==password:
                flag=1
                break
        if flag==1:
            return username
        else:
            error=1
def register():
    users=loadusers()
    mobile=input("Enter Mobile Number:")
    username=input("Enter Username:")
    password=input("Enter Password:")
    for i in users:
        if i['username']==username:
            print("Username already exists. Please choose a different one.")
            return
        users.append({"username":username,"password":password,"mobile":mobile})
        saveusers(users)
        print("Registration Successful")
        os.system("cls")
        return
def loginadmin():
    error=0
    users=loadadmin()
    while True:
        os.system("cls")
        if error==1:
            print("Incorrect Details enter again:")
        username=input("Enter Username:")
        password=input("Enter Password:")
        flag=0
        for i in users:
            if i['username']==username and i['password']==password:
                flag=1
                break
        if flag==1:
            print("Login Succesful")
            return True
        else:
            error=1
def usermenu(username):
    while True:
        os.system("cls")
        choice=input("1.Checkout Cart\n2.Add items to cart\n3.Order history\n4.logout\nSelect Choice:")
        if choice=='1':
            showcart(username)
        elif choice=='2':
            addtocart(username)
        elif choice=='3':
            orderhistory(username)
        elif choice=='4':
            break
    return 
def orderhistory(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"======== Order History for {username} ========")

    try:
        with open("orders.json", "r") as file:
            orders = json.load(file)
    except FileNotFoundError:
        print("No order history found.")
        input("Press Enter to return...")
        return

    user_orders = [order for order in orders if order["username"] == username]

    if not user_orders:
        print("No orders found for this user.")
        input("Press Enter to return...")
        return

    for i, order in enumerate(user_orders, start=1):
        print(f"Order #{i}:")
        print(f"{'Item ID':<10} {'Item Name':<20} {'Quantity':<10} {'Price (INR)':<10}")
        print("-" * 60)
        for item in order["items"]:
            print(f"{item['item_id']:<10} {item['item_name']:<20} {item['item_quantity']:<10} {item['item_price']:<10}")
        print("-" * 60)
        print(f"{'Total Price:':<30} INR {order['total_price']:.2f}")
        print()

    input("Press Enter to return...")

def adminorderhistory():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======== Admin: View Order History ========")

    try:
        with open("orders.json", "r") as file:
            orders = json.load(file)
    except FileNotFoundError:
        print("No order history found.")
        input("Press Enter to return...")
        return

    usernames = sorted(set(order["username"] for order in orders))

    if not usernames:
        print("No users have placed any orders.")
        input("Press Enter to return...")
        return

    print("Available Users:")
    for idx, username in enumerate(usernames, start=1):
        print(f"{idx}. {username}")

    try:
        choice = int(input("\nSelect a user by number (or 0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(usernames):
            selected_user = usernames[choice - 1]
            orderhistory(selected_user)
        else:
            print("Invalid selection. Please try again.")
            input("Press Enter to return...")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        input("Press Enter to return...")

def adminmenu():
    while True:
        os.system("cls")
        choice=input("1.Update Groceries\n2.Order history\n3.logout\nSelect Choice:")
        if choice=='1':
            addgrocery()
        elif choice=='2':
            adminorderhistory()
        elif choice=='3':
            break
    return
def addtocart(username):
    error = False
    grocery = loadgroceries()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen command compatible with Windows and Linux/Mac
        if error:
            print("Invalid choice, please try again!")
            error = False
        
        print("======== Types of Groceries =======")
        grocerytypes = list(grocery.keys())

        for idx, grocery_type in enumerate(grocerytypes, start=1):
            print(f'{idx}. {grocery_type}')
        print(f'{len(grocerytypes   ) + 1}. Exit')

        try:
            choice = int(input("Select choice: ")) - 1
        except ValueError:
            error = True
            continue

        if choice == len(grocerytypes): 
            break

        if 0 <= choice < len(grocerytypes):
            selected_type = grocerytypes[choice]
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nDetails of {selected_type}:\n")
            print(f"{'ID':<6} {'Name':<15} {'Quantity (kg)':<15} {'Price (INR)':<10}")
            print("-" * 50)

            for item in grocery[selected_type]:
                print(f"{item['id']:<6} {item['name']:<15} {item['quantity']:<15} {item['price']:<10}")
            
            try:
                action = int(input("\n1. Add Items to Cart\n2. Back\nSelect choice: "))
            except ValueError:
                error = True
                continue

            if action == 1:
                try:
                    item_id = int(input("Enter ID: "))
                    quantity = float(input("Enter Quantity (in KG): "))
                except ValueError:
                    print("Invalid input. Please enter numerical values for ID and Quantity.")
                    input("Press Enter to continue...")
                    continue

                selected_item = next((item for item in grocery[selected_type] if item['id'] == item_id), None)

                if selected_item:
                    if selected_item['quantity'] >= quantity:
                        total_price = selected_item['price'] * quantity
                        print(f"\nYour Order Summary:")
                        print(f"Name: {selected_item['name']}")
                        print(f"Quantity: {quantity} KG")
                        print(f"Total Price: INR {total_price:.2f}")
                        
                        confirm = int(input("1. Continue\n2. Cancel\nSelect choice: "))
                        if confirm == 1:
                            cart = loadcart()

                            # Check if the username exists in the cart
                            user_cart = next((user for user in cart if user["username"] == username), None)

                            if user_cart:
                                # Add the new order to the user's cart
                                user_cart["orders"].append({
                                    "type": selected_type,
                                    "name": selected_item["name"],
                                    "quantity": quantity,
                                    "price": total_price
                                })
                            else:
                                # Create a new entry for the user
                                cart.append({
                                    "username": username,
                                    "orders": [{
                                        "type": selected_type,
                                        "name": selected_item["name"],
                                        "quantity": quantity,
                                        "price": total_price
                                    }]
                                })

                            savecart(cart)
                            print("Order added to cart successfully!")
                            input("Press Enter to continue...")
                        else:
                            print("Order cancelled.")
                            input("Press Enter to continue...")
                    else:
                        print("Insufficient quantity available!")
                        input("Press Enter to continue...")
                else:
                    print("Item not found!")
                    input("Press Enter to continue...")
            elif action == 2:
                continue
            else:
                error = True
        else:
            error = True


def showcart(username):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen command compatible with Windows and Linux/Mac

    cart = loadcart()
    grocery = loadgroceries()
    user_cart = next((user for user in cart if user["username"] == username), None)

    if not user_cart:
        print(f"Cart is empty for user '{username}'.")
        input("Press Enter to return...")
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"======== Cart for {username} ========")
        print(f"{'Type':<15} {'Name':<15} {'Quantity (kg)':<15} {'Price (INR)':<10}")
        print("-" * 60)

        total_price = 0
        for order in user_cart["orders"]:
            print(f"{order['type']:<15} {order['name']:<15} {order['quantity']:<15} {order['price']:<10}")
            total_price += order["price"]

        print("-" * 60)
        print(f"{'Total Price:':<30} INR {total_price:.2f}")

        choice = input("\n1. Proceed to Buy\n2. Edit Cart\n3. Exit\nSelect an option: ")

        if choice == '1':
            out_of_stock = []
            for order in user_cart["orders"]:
                for item in grocery[order["type"]]:
                    if item["name"] == order["name"]:
                        if item["quantity"] >= order["quantity"]:
                            item["quantity"] -= order["quantity"]
                        else:
                            out_of_stock.append(order["name"])

            if out_of_stock:
                print("The following items are out of stock or insufficient:")
                for item in out_of_stock:
                    print(f"- {item}")
            else:
                print("Purchase successful!.")

                # Update orders.json with the purchase details
                try:
                    with open("orders.json", "r") as file:
                        orders = json.load(file)
                except FileNotFoundError:
                    orders = []

                # Append purchase details to orders.json
                orders.append({
                    "username": username,
                    "items": [
                        {
                            "item_id": next(item["id"] for item in grocery[order["type"]] if item["name"] == order["name"]),
                            "item_name": order["name"],
                            "item_quantity": order["quantity"],
                            "item_price": order["price"]
                        }
                        for order in user_cart["orders"]
                    ],
                    "total_price": total_price
                })

                with open("orders.json", "w") as file:
                    json.dump(orders, file, indent=4)

                user_cart["orders"] = []  # Clear the cart after purchase

            savegrocery(grocery)
            savecart(cart)
            input("Press Enter to continue...")

        elif choice == '2':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("1. Edit Items in Cart\n2. Clear Cart\n3. Exit")
                edit_choice = input("Select an option: ")

                if edit_choice == '1':
                    print(f"{'ID':<6} {'Type':<15} {'Name':<15} {'Quantity (kg)':<15} {'Price (INR)':<10}")
                    print("-" * 60)
                    for idx, order in enumerate(user_cart["orders"], start=1):
                        print(f"{idx:<6} {order['type']:<15} {order['name']:<15} {order['quantity']:<15} {order['price']:<10}")

                    try:
                        item_id = int(input("Enter the ID of the item to remove (or 0 to cancel): "))
                        if item_id == 0:
                            break
                        if 1 <= item_id <= len(user_cart["orders"]):
                            user_cart["orders"].pop(item_id - 1)
                            savecart(cart)
                            print("Item removed successfully!")
                        else:
                            print("Invalid ID. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                    input("Press Enter to continue...")

                elif edit_choice == '2':
                    user_cart["orders"] = []
                    savecart(cart)
                    print("Cart cleared successfully!")
                    input("Press Enter to continue...")
                    break

                elif edit_choice == '3':
                    break

                else:
                    print("Invalid choice. Please try again.")
                    input("Press Enter to continue...")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


def showlist():
    grocery = loadgroceries()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen command compatible with Windows and Linux/Mac
        
        print("======== Types of Groceries =======")
        grocerytypes = list(grocery.keys())

        for idx, grocery_type in enumerate(grocerytypes, start=1):
            print(f'{idx}. {grocery_type}')
        print(f'{len(grocerytypes) + 1}. Exit')

        try:
            choice = int(input("Select choice: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            input("Press Enter to continue...")
            continue

        if choice == len(grocerytypes):  # Exit condition
            break

        if 0 <= choice < len(grocerytypes):
            selected_type = grocerytypes[choice]
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nDetails of {selected_type}:\n")
            print(f"{'ID':<6} {'Name':<15} {'Quantity (kg)':<15} {'Price (INR)':<10}")
            print("-" * 50)

            for item in grocery[selected_type]:
                print(f"{item['id']:<6} {item['name']:<15} {item['quantity']:<15} {item['price']:<10}")
            
            input("\nPress Enter to go back to the menu...")
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")

def showtypes():
    grocery=loadgroceries()
    while True:
        os.system("cls")
        choice=input("1.Update List\n2.Show List\n3.Exit\nSelect Choice:")
        if choice=='1':
            showtypes()
            os.system('cls')
            print("========Types of Groceries=======")
            grocerytypes=list(grocery.keys())
            max=0
            for i,j in enumerate(grocerytypes):
                if max<i:
                    max=i
                print(f'{i+1}. {j}')
            print(f'{i+2}. Exit')
            a=int(input("Select Choice:"))
            if a==i+2:
                break
def addgrocery():
    grocery=loadgroceries()
    error=0
    while True:
        os.system("cls")
        if error==1:
            print("Invalid Input, Enter again!")
        choice=input("1.Update List\n2.Show List\n3.Exit\nSelect Choice:")
        if choice=='1':
            while True:
                os.system('cls')
                print("========Types of Groceries=======")
                grocerytypes=list(grocery.keys())
                max=0
                for i,j in enumerate(grocerytypes):
                    if max<i:
                        max=i
                    print(f'{i+1}. {j}')
                print(f'{i+2}. Exit')
                a=int(input("Select Choice:"))
                if a==i+2:
                    break
                elif a>0 and a<=i+1:
                    name=input("Name:")
                    quantity=float(input("Quantity"))
                    price=float(input("Price:"))
                    count=sum(len(items) for items in grocery.values())
                    id=count+1001
                    grocery[grocerytypes[a-1]].append({"name":name,"quantity":quantity,"price":price,"id":id})
                    savegrocery(grocery)
                    return
                else:
                    error=1

        elif choice=='2':
            showlist()
        elif choice=='3':
            break
        else:
            print("Invalid Choice!")   
flag=0
while True:
        os.system("cls")
        if flag==1:
            print("Invalid Choice, Enter again")
        choice=input("1.Login\n2.Login as Admin\n3.Register\n4.Exit\nChoose one:")
        if choice=='1':
            username=login()
            os.system("cls")
            print("Login Successful!")
            usermenu(username)
        elif choice=='2':
            if(loginadmin()):
                os.system("cls")
                print("Login Successful!")
                adminmenu()
        elif choice=='3':
            register()
        elif choice=='4':
            break
        else:
            flag=1