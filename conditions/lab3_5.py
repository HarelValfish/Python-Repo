# def hello():
#     print("Hello")
    
# print("start")
# hello()
# print("finish")

def ask():
    user_input = int(input("Enter your age: "))
    secage = user_input * 365 * 24 * 60 * 60
    print(f"Your are {secage} seconds old.")
    
ask()
    