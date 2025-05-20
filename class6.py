#class6.py

from datetime import date
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
    
    @staticmethod
    def isAdult(age):
        return age > 16

person1 = Person('john', 12) 
person2 = Person.fromBirthYear('elvis', 1975) 

print (person1.age)
print (person2.age)
print(person1.isAdult(person1.age))
print(person2.isAdult(person2.age))
