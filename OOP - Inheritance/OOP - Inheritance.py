class Vehicles:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        return(f"{self.brand},{self.model}The vehicle is moving")   
class Car(Vehicles):
    def move(self):
        return(f"{self.brand},{self.model}The car drives")

class Plane(Vehicles):
    def move(self):
        return(f"{self.brand},{self.model}The plane flies")
         
a =  Vehicles("vehicles","0")
print(a.move())

b = Car("tyote",2025)
print(b.move())

c = Plane("boeing","2015")
print(c.move())






class Animals:
    def __init__(self,name):
        self.name=name
    def sound(self):
        return
class Dog(Animals):    
    def sound(self):
        return f"{self.name}doing Woof"
    
class Cat(Animals):    
    def sound(self):
        return f"{self.name}doing meow"
    

a = Dog("raxi ")
b = Cat("mitzi ")

c=[a.sound(),b.sound()]

for i in c:
    print(i)             
          


          







    



