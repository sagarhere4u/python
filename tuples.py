#tuples.py

t = ("sam", 786, 2.34, "john", 70)
tinytuple = (123, "hello")

print(t)             #prints ("sam", 786, 2.34, "john", 70)
print(t[0])          #prints sam
print(t[1:3])        #prints (786,2.34)
print(t[2:])         #prints (2.34,"john",70)

print(tinytuple * 3)     #prints (123, "hello", 123, "hello", 123, "hello")
print(t + tinytuple)  #prints ("sam", 786, 2.34, "john", 70, 123, "hello")

t.append("sixth")    #error
print(t)             #error
t[5] = "sixth"        #error
print(t)              #error
