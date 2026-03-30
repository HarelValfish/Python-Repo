accounts = [{
    "account_id": 1001,
    "username": "Harel",
    "balance": 50000,
    "pin": 4331
},
{
    "account_id": 1002,
    "username": "Mike",
    "balance": 1000000,
    "pin": 1234
}]

def auth():
    id = int(input("Enter ID:"))
    pin = int(input("Enter PIN: "))
    
    for user in accounts:
        if id == user["account_id"] and user["pin"] == pin:
            print(f"Welcome {user["username"]}")
            return user
        else:
            exit()

def withdraw():
    user_account = auth()
    if user_account:
        amount = int(input("Please type withdrawal amount: "))
        if amount > user_account["balance"]:
            print("insufficient amount.")
            exit()
        else:
            user_account["balance"] -= amount
            balance(user_account["balance"])
    else:
        print("Wrong pin, goodbye")
        exit()

def deposit():
    user_account = auth()
    if user_account:
        amount = float(input("Please type deposit amount: "))
        if amount < 0:
            print("Invalid amount.")
            exit()
        else:
            user_account["balance"] += amount
            balance(user_account["balance"])
            
    else:
        print("Wrong pin, Goodbye")
        exit()
    
def balance(user_balance):
    print(f"Your balance is {user_balance}")
    
while True:
    print("========= Welcome to Python ATM =========")
    x = int(input("""
          Enter your choice
          1. Withdraw
          2. Deposit
          3. Balance
          0. Exit
          User Choice: """))

    
    match x:
        case 1:
            withdraw()
        case 2:
            deposit()
        case 3:
            balance()
        case 0:
            print("")
            exit()

        