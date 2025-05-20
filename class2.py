#class2.py

#define a class called Dog
class Dog:
    species = "Canis"
    #constructor of the class or intilization method 
    #two attributes name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

#creating object/instance called jack
jack = Dog("Jack", 4)

#printing attributes of jack
print(jack.name,jack.age, jack.species)
#printing address of jack
print(jack)

buddy = Dog("Buddy", 9)
print(buddy.name, buddy.age, buddy.species)
print(buddy)