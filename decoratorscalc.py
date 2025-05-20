#decoratorscalc.py

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

def operate(f,x,y):
    r = f(x,y)
    return r

print("Add: ", operate(add,10,20))
print("Subtract: ", operate(sub,10,20))
print("Multiply: ", operate(mul,10,20))
print("Division: ", operate(div,10,20))
print("GoodBye!")
