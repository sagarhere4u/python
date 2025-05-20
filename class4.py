#class4.py

class Dog:
    species = "Canis"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        return f"{self.name} says {sound}."

class JackRussell(Dog):
    pass

class Bulldog(Dog):
    pass

jim = Bulldog("Jim", 9)
miles = JackRussell("Miles", 3)

print(jim)
print(miles)
print(jim.speak("hello"))
print(miles.speak("Bow Bow"))

if isinstance(jim, Dog):
    print("jim object is instance of Dog")

if isinstance(jim, Bulldog):
    print("jim is an object of BullDog")