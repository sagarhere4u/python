#class5.py

from datetime import date
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
    
person1 = Person('john', 21) 
person2 = Person.fromBirthYear('elvis', 1975) 

print (person1.age)
print (person2.age)