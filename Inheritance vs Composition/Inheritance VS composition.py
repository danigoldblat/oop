class Vehicles:
    def __init__(self,max_speed):
        self.max_speed=max_speed
    def drive(self):
        print(f"The can travel up to{self.max_speed}")
        
    class Car(Vehicles):
       pass
        
class Motrcycle(Vehicles):
    pass
    
# car1=Car(120)
# car1.drive()

# motrcycle1=Motrcycle(100)
# motrcycle1.drive()

class Employee_Types:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee_Types):
    def manager(self):
        print(f"The worker {self.name}earning {self.salary}")
class Developer(Employee_Types):
    def developer(self):
         print(f"The worker {self.name}earning {self.salary}")     
         