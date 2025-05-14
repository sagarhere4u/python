#function2.py

#define a function
def sum(a, b):
    c = a + b
    print("Inside the function: ", c)
    return c

#call the function and take back return value
total = sum(10,20)
print("Outside the function: ", total)
