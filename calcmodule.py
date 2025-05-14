#calcmodule.py
def getNumbers():    
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    return a, b

def getChoice():
    print("-" * 30)
    print ('''            Enter 1 for Addition(+)
            Enter 2 for Subtraction(-)
            Enter 3 for Multiplication(x)
            Enter 4 for Division(/)
            Enter 0 for Exit ''')
    choice = int(input("Enter your choice: "))
    print("-" * 30)
    return choice

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b