#a class is like a blueprint for creating objects
 ##creating a class
class user:
    #class attributes
    name = ""
    age = 0
    
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #init use objects
        
    
    #method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


#extend class

phylis = user("Phylis", 30)
phylis.greet()
print(f"User's name is {phylis.name} and age is {phylis.age}")
