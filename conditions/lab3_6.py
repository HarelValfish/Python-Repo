def add_numbers(x, y):
    result = x + y
    print(result)
    
add_numbers(5, 3)

#=======================

def greet():
    print("Hello")

greet() # cant take argument because the function takes 0 arguments

#=======================

def getname(x):
    print(f"hello, {x}")
    
getname("Bob") # Must recieve arguments because the fucntion take 1 (x)

#=======================

def fullname(first_name, last_name):
    print(first_name,last_name)

fullname(last_name = "Valfish", first_name = "Harel")

#=======================

def subnum(n1, n2):
    
    if n2 == 0:
        print("You Fool.")
    else:
        print(n1 / n2)

subnum(20, 0)