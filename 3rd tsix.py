#3 public variables and methods
#Assignment:
#create a class car with a public variable Brand and a public method start(). instantiate the class and access both 
#from out side  the class.
# solution
class Car:
    def __init__(self,brand):
        self.brand = brand
        
    def start(self):
        print(f"{self.brand} is starting...!")
        
my_car = Car("Audi")
print(my_car.brand)
my_car.start()
        