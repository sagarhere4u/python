#class3.py
#define a class called Dog
class Dog:
    species = "Canis"
    #constructor of the class or intilization method 
    #two attributes name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def description(self):
        return self.name + " is " + str(self.age) + " years old"
    
    #instance method
    def speak(self, sound):
        return self.name + " says " + sound
    
#creating object/instance called jack
miles = Dog("Miles", 5)
print(miles.description())
print(miles.speak("Woof Woof"))
