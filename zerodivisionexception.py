#zerodivisionexception.py

var = 1
while ( var == 1 ):
    a = float(input("Enter First No: "))
    b = float(input("Enter Second No: "))

    try:
        print("Division Result is: ", a / b)
        var = 0
    except ZeroDivisionError:
        print("Second Number is ZERO. Retry !!")

print("GoodBye!")