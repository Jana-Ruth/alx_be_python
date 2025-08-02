class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

S = Student("Ruth", 20)
print (f"My name is {S.name}. I am {S.age} years old")    





class ProductCatalog:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_Value(self):
        return self.price * self.quantity  
        
        
P = ProductCatalog("Bread", 100, 5)    

print(f"The price of {P.quantity} {P.name} is {P.total_Value()}") 


