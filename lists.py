#lists.py

list = ["sam", 786, 2.34, "john", 70]
tinylist = [123, "hello"]

print(list)             #prints ["sam", 786, 2.34, "john", 70]
print(list[0])          #prints sam
print(list[1:3])        #prints [786,2.34]
print(list[2:])         #prints [2.34,"john",70]

print(tinylist * 3)     #prints [123, "hello", 123, "hello", 123, "hello"]
print(list + tinylist)  #prints ["sam", 786, 2.34, "john", 70, 123, "hello"]

list.append("sixth")  
print(list)             #prints ["sam", 786, 2.34, "john", 70,"sixth"]

