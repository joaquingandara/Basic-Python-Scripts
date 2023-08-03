class Person: 
    codeOfCreation = 6
    def __init__(self,name,age,city="Buenos Aires"):
        self.name = name 
        self.age = age 
        self.city = city 

    def __str__(self):
        return f"My name is {self.name}, I'm {self.age} years old and I'm from {self.city}"
    
    @classmethod
    def codeCreation(cls):
        return f"{cls.count}"
    
    def changeCity(self,newCity):
        self.city = newCity

    @staticmethod
    def printAgeWithYears(actualYear, yearBirth):
        print(actualYear - yearBirth)

newP = Person("Joaquin",23,"CABA")
print(newP)
Person.printAgeWithYears(2023,1999)
