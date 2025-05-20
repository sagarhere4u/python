#functiondecorator.py

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(f, x):
    r = f(x)
    return r

print(operate(inc,5))
print(operate(dec,99))
