#calc2.py
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("-" * 30)
print ('''          Enter 1 for Addition(+)
          Enter 2 for Subtraction(-)
          Enter 3 for Multiplication(x)
          Enter 4 for Division(/)
          Enter 0 for Exit ''')
choice = int(input("Enter your choice: "))
print("-" * 30)

if choice == 1:
    print ("Addition: ", a + b)
elif choice == 2:
    print ("Subtraction: ", a - b)
elif choice == 3:
    print ("Multiplication: ", a * b)
elif choice == 4:
    print ("Division: ", a / b)
else:
    exit()