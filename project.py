"""
Project Name: Inventory Management System

Name: Samet

GitHub Username: ceSamet

edX Username: sametaydin

City: İstanbul, Türkiye

Date: 2024-03-19

"""


from json import load, dump
from os import system, execl
import sys


### JSON File Links ###

# Function to Read Products
def read_products():
    try:
        with open("products.json", "r") as f:
            products = load(f)
    except FileNotFoundError:
        products = [
            {"product code": "0001", "name": "rice", "price": "60", "tax": "8", "stock": "84", "alert": "40"}
        ]
    return products

# Function to Update Products


def update_products(products):
    with open('products.json', 'w') as f:
        dump(products, f, indent=4)

# Function to Read Info


def read_info():
    try:
        with open("info.json", "r") as f:
            info = load(f)
    except FileNotFoundError:
        info = [
            {"receipt_code": 1}, {"currency_type": "$"}, {"company_name": "duck duck"}, {
                "current_role": "a"}, {"current_cashier": "admin"}
        ]
    return info

# Function to Update Info


def update_info(info):
    with open('info.json', 'w') as f:
        dump(info, f)

# Function to Read Users


def read_users():
    try:
        with open("users.json", "r") as f:
            users = load(f)
    except FileNotFoundError:
        users = [{"name": "admin", "key": "admin", "role": "a"}]
    return users

# Function to Update Users


def update_users(info):
    with open('users.json', 'w') as f:
        dump(info, f)

# Terminal Clearing Function


def clearterminal():
    system("clear")


# Validation Function


def validate():
    clearterminal()
    users = read_users()
    valid_user = False
    for i in range(3):  # Maximum 3 login attempts
        user_name = input("Username: ")
        for user in users:
            if user_name == user["name"]:
                key = input("Password: ")
                if key == user["key"]:
                    print("Validation successful")
                    info = read_info()
                    info[3]["current_role"] = user["role"]
                    info[4]["current_cashier"] = user["name"]
                    with open("info.json", "w") as f:
                        dump(info, f)
                    valid_user = True
                    break
        if valid_user:
            break
        else:
            clearterminal()
            print("Invalid username or password. Please try again.")
    if not valid_user:
        clearterminal()
        print("You have exceeded the maximum number of login attempts. Program closed.")
    return valid_user


# Integer Input Validation Function


def contint(text):
    while True:
        try:
            answer = int(input(text))
            clearterminal()
            return answer
        except ValueError:
            print("Please enter a valid integer.")

# Function to Return to Main Menu


def goback():
    main()

# Function for Post-Process Decisions


def finish():
    while True:
        answer = input("Back: Return to main menu\nExit: Exit the program\nProcess: ")
        if answer == "back":
            goback()
            break
        elif answer == "exit":
            clearterminal()
            exit()
        else:
            clearterminal()
            print("Invalid process")


### Main Menu Processes ###

# Stockinfo Menu
def stockinfo():
    while True:
        print("Processes:\nList: Monitor list of products\nAlert: Monitor alerts\nBack: Back to main menu")
        process = input("Process: ")
        clearterminal()

        if process == "list":
            for product in read_products():
                print("Product code:", product["product code"])
                print("Name:", product["name"])
                print("Price:", product["price"], read_info()[1]["currency_type"])
                print("Tax:", product["tax"], "%")
                print("Stock:", product["stock"])
                print("Alert:", product["alert"])
                print("-" * 30)
        elif process == "alert":
            alert = "no"
            for product in read_products():
                if int(product["stock"]) <= int(product["alert"]):
                    print("The amount of", product["name"], "is low", "Stock", product["stock"], "Alert", product["alert"])
                    alert = "yes"
            if alert == "no":
                print("No alerts")
        elif process == "back":
            goback()
            break
        else:
            print("Invalid process")

# Function to Update Stock Info


def stock_update():
    while True:
        print("Processes:\nUpdate: Update info of a product\nNew: Enter a new product\nAdd: Add stock to a product\nBack: Back to main menu")
        process = input("Process: ")
        clearterminal()

        if process == "new":
            name = input("Name: ")
            clearterminal()
            for product in read_products():
                if product["name"] == name:
                    print("Product already exists, update in progress.")
                    price = contint("New price: ")
                    tax = contint("New tax: ")
                    stock = contint("New stock: ")
                    alert = contint("Alert level: ")
                    product["price"] = price
                    product["tax"] = tax
                    product["stock"] = stock
                    product["alert"] = alert
                    print("Product updated successfully:", product)
                    break
            else:
                price = contint("New price: ")
                tax = contint("New tax: ")
                stock = contint("New stock: ")
                alert = contint("Alert level: ")
                products = read_products()
                products.append({"product code": str(len(products) + 1).zfill(5), "name": name,
                                "price": price, "tax": tax, "stock": stock, "alert": alert})
                print("Product added successfully:", products[-1])
            update_products(products)
        elif process == "update":
            name = input("Enter the name of the product to update: ")
            clearterminal()
            for product in read_products():
                if product["name"] == name:
                    price = contint("New price: ")
                    tax = contint("New tax: ")
                    stock = contint("New stock: ")
                    alert = contint("Alert level: ")
                    product["price"] = price
                    product["tax"] = tax
                    product["stock"] = stock
                    product["alert"] = alert
                    print("Product updated successfully:", product)
                    update_products(read_products())
                    break
            else:
                while True:
                    answer = input("Product not found. Do you want to add a new product? ")
                    if answer.lower() in ("yes", "y"):
                        price = contint("New price: ")
                        tax = contint("New tax: ")
                        stock = contint("New stock: ")
                        alert = contint("Alert level: ")
                        products = read_products()
                        products.append({"product code": str(len(products) + 1).zfill(5), "name": name,
                                        "price": price, "tax": tax, "stock": stock, "alert": alert})
                        update_products(products)
                        finish()
                    elif answer.lower() in ("no", "n"):
                        finish()
                    else:
                        print("Invalid answer")
        elif process == "add":
            name = input("Enter the name of the product to add stock: ")
            clearterminal()
            product_found = False
            for product in read_products():
                if product["name"] == name:
                    stock = contint("Amount: ")
                    product["stock"] = str(int(product["stock"]) + int(stock))
                    product_found = True
                    print("Stock added successfully")
                    update_products(read_products())
            if not product_found:
                print("Product not found.")
        elif process == "back":
            goback()
        else:
            print("Invalid process")

# Checkout Process


def checkout():
    currency = read_info()
    products = read_products()
    receipt = []
    z = 1

    print("Processes:\nSale: Sell products\nReturn: Get product return\nBack: Back to main menu")
    process = input("Process: ")
    clearterminal()

    if process == "sale":
        total = 0
        tax = 0
        total_tax = 0
        while True:
            code = input("Enter product amount and name, 'finish' or 'cancel': ")
            clearterminal()
            if code == "finish":
                if z == 1:
                    print("Cancelled")
                    break
                while True:
                    payment_method = input("Cash or card: ")
                    clearterminal()
                    if payment_method.lower() in ("cash", "card"):
                        break
                    else:
                        print("Invalid answer")
                for item in receipt:
                    for product in products:
                        if item["name"] == product["name"]:
                            product["stock"] = str(int(product["stock"]) - int(item["amount"]))
                update_products(products)
                print("Receipt")
                print("Company:", currency[2]["company_name"], "Cashier:", currency[4]["current_cashier"])
                for product in receipt:
                    print(product["line"], "Name:", product["name"], "Amount:", product["amount"], "Price:",
                          str(int(product["amount"]) * int(product["price"])), currency[1]["currency_type"], "Tax", "%", product["tax"])
                    total += int(product["amount"]) * int(product["price"])
                    tax += int(product["amount"]) * int(product["price"]) * int(product["tax"]) / 100
                    total_tax += tax
                print("Total:", total, currency[1]["currency_type"])
                print("Total Tax:", "{:.2f}".format(total_tax), currency[1]["currency_type"])
                if payment_method == "card":
                    print("Paid by card")
                else:
                    while True:
                        cash = contint("Cash: ")
                        clearterminal()
                        if total > cash:
                            print("Insufficient")
                        else:
                            print(f"Cash: {cash}")
                            print(f"Change: {cash-total}")
                            break
                code = read_info()
                with open(f"receipt_record/receipt_{code[0]['receipt_code']}.json", "w") as f:
                    dump(receipt, f, indent=4)
                code[0]["receipt_code"] = int(code[0]["receipt_code"]) + 1
                update_info(code)
                print("\n")
                finish()
            elif code == "cancel":
                finish()
            else:
                parts = code.split()
                if len(parts) == 2 and parts[0].isdigit():
                    amount = int(parts[0])
                    name = parts[1]
                else:
                    amount = 1
                    name = code
                for item in receipt:
                    if item["name"] == name:
                        item["amount"] += amount
                        break
                else:
                    for product in products:
                        if product["name"] == name:
                            if int(product["stock"]) >= 0:
                                receipt.append({"line": str(z), "amount": amount, "name": name, "price": product["price"],
                                                "tax": product["tax"]})
                                z += 1
                                break
                            else:
                                print("No stock")
                                break
                    else:
                        print("Product not found")
    elif process == "return":
        name = input("Enter the name of the product to return: ")
        clearterminal()
        for product in products:
            if product["name"] == name:
                stock = contint("Amount: ")
                product["stock"] = str(int(product["stock"]) + int(stock))
                print("Returned successfully")
                update_products(products)
        else:
            print("Product not found.")
    elif process == "back":
        goback()
    else:
        print("Invalid process")

# Function to Change Settings


def settings():
    info = read_info()
    while True:
        print("Processes:\nCurrency: Change currency\nName: Change company name\nBack: Back to main menu")
        process = input("Process: ")
        clearterminal()
        if process == "currency":
            info[1]["currency_type"] = input("Type currency: ")
            update_info(info)
            print("Currency type changed successfully")
        elif process == "name":
            info[2]["company_name"] = input("Company name: ")
            update_info(info)
            print("Company name changed successfully")
        elif process == "back":
            goback()
        else:
            print("Invalid process")

### Functions for User Management ###

# Function to Monitor Users


def monitor():
    users = read_users()
    for user in users:
        print("Name:", user["name"], "Role:", user["role"])

# Function to Register Users


def register():
    users = read_users()
    while True:
        name = input("Name: ")
        clearterminal()
        if any(user["name"] == name for user in users):
            print("User with this name already exists. Please enter a different name.")
        else:
            break
    key = input("Password: ")
    clearterminal()
    print("Admin (a)\nCashier (c)")
    while True:
        role = input("Role: ")
        clearterminal()
        if role.lower() in ("a", "c"):
            users.append({"name": name, "key": key, "role": role})
            with open("users.json", "w") as f:
                dump(users, f, indent=3)
            print("User added successfully")
            break
        else:
            print("Invalid role")

# Function to Delete Users


def delete_user():
    users = read_users()
    name = input("Enter the name of the user you want to delete: ")
    # Check if the user wants to delete themselves
    current_user = read_info()[4]["current_cashier"]
    if name == current_user:
        print("You cannot delete yourself.")
        return
    user_found = False
    for user in users:
        if user["name"] == name:
            users.remove(user)
            user_found = True
            break
    if user_found:
        with open("users.json", "w") as f:
            dump(users, f, indent=3)
        print("User deleted successfully")
    else:
        print("User not found")

# Function to Check Current User


def check():
    role = read_info()
    if role[3]["current_role"] == "a":
        return "a"
    else:
        return "c"

def restart_program():
    python = sys.executable
    execl(python, python, *sys.argv)

# Function to Manage Users


def manageusers():
    while True:
        print("processes: \n list: monitor list of users \n delete: delete a user \n register: register a user \n change: change the current user \n back: back to main menu")
        process = input("process: ")
        clearterminal()
        if process == "list":
            monitor()
        elif process == "delete":
            delete_user()
        elif process == "register":
            register()
        elif process == "change":
            restart_program()
        elif process == "back":
            goback()
        else:
            print("invalid process")


# Main Menu Processes


def main():
    if check() == "a":
        while True:
            print("Welcome to the marketing system \n Processes: \n stockinfo : access the info of list of products \n stockupdate : update the info in list \n checkout : sale and return \n settings: change currency and company name \n manageusers : register, delete or monitor users \n exit: exit the program")
            process = input("Process: ")
            clearterminal()
            if process == "stockinfo":
                stockinfo()
            elif process == "stockupdate":
                stock_update()
            elif process == "checkout":
                checkout()
            elif process == "exit":
                exit()
            elif process == "settings":
                settings()
            elif process == "manageusers":
                manageusers()
            clearterminal()
            print("Invalid process!")
    else:
        while True:
            print("Welcome to the marketing system \n Processes: \n stockinfo : access the info of list of products \n checkout : sale and return \n exit: exit the program")
            process = input("Process: ")
            clearterminal()
            if process == "stockinfo":
                stockinfo()
            elif process == "checkout":
                checkout()
            elif process == "exit":
                exit()
            clearterminal()
            print("Invalid process!")

# Main Function
if __name__ == '__main__':
    while True:
        try:
            if validate():
                main()
            else:
                exit()
        except (EOFError, KeyboardInterrupt):
            clearterminal()
            print("Changes saved. Program closed.")
            break
