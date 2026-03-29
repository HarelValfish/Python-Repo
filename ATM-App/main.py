accounts = [
    {"account_id": 100, "name": "Liron", "pin": "1234", "balance": 500},
    {"account_id": 101, "name": "Daniel", "pin": "5678", "balance": 900},
]
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123456"

def find_account(account_id):
    for account in accounts: # Check if the ID in the current dictionary matches the one we are looking for
        if account["account_id"] == account_id:
            return account  # Found it! Return the whole dictionary
    return None  # If the loop ends without finding a match

def verify_pin(account, user_pin_input):
    is_pin_correct = account["pin"] == user_pin_input
    return is_pin_correct
    
def deposit():
    account_id = int(input("Account ID: "))
    pin = input("PIN: ")
    amount = float(input("Amount: "))

    account = find_account(account_id)

    if not account:
        print("Account not found")
        return

    if not verify_pin(account, pin):
        print("Wrong PIN")
        return

    if amount <= 0:
        print("Invalid amount")
        return

    account["balance"] += amount

def withdraw():
    account_id = int(input("Account ID: "))
    pin = input("PIN: ")
    amount = float(input("Amount: "))

    account = find_account(account_id)

    if not account:
        print("Account not found")
        return

    if not verify_pin(account, pin):
        print("Wrong PIN")
        return

    if account["balance"] < amount:
        print("Insufficient funds")
        return

    account["balance"] -= amount

def show_account():
    account_id = int(input("Account ID: "))
    pin = input("PIN: ")

    account = find_account(account_id)

    if not account:
        print("Account not found")
        return

    if not verify_pin(account, pin):
        print("Wrong PIN")
        return

    print(account)

def create_account():
    if not admin_login():
        return

    name = input("Enter name: ")
    pin = input("Set PIN: ")

    account = {
        "account_id": len(accounts) + 100,
        "name": name,
        "pin": pin,
        "balance": 0
    }
    accounts.append(account)

def show_all_accounts():
    if not admin_login():
        return

    for acc in accounts:
        print(acc)

def admin_login():
    username = input("Admin username: ")
    password = input("Password: ")
    if (username == ADMIN_USERNAME) and (password == ADMIN_PASSWORD):
        return True
    else:
        print("Access Denied.")
        return False

while True:
    print("1.Create 2.Deposit 3.Withdraw 4.Show 5.Admin View 6.Exit")

    choice = input("Choose: ")
    print()

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        show_account()

    elif choice == "5":
        show_all_accounts()

    elif choice == "6":
        break