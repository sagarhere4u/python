#calc4.py
import calcmodule

a, b = calcmodule.getNumbers()
var = 1
while ( var == 1 ):
    choice = calcmodule.getChoice()
    if choice == 1:
        print("Addition: ", calcmodule.add(a,b))
    elif choice == 2:
        print ("Subtraction: ", calcmodule.subtract(a,b))
    elif choice == 3:
        print ("Multiplication: ", calcmodule.multiply(a,b))
    elif choice == 4:
        print ("Division: ", calcmodule.divide(a,b))
    elif choice == 0:
        var = 0
    else:
        print("Invalid Choice!")
print("Goodbye!")