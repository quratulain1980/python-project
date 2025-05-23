#static variables and static methods
#assignment:
#create a class mathutils with astatic method add(a,b) that returns the sum .No  class or instance variables
#should be used.


#solution

class MathUtils:
    @staticmethod
    def add(a,b):
       return a + b
   
result = MathUtils.add(10,5)
print("Sum of my 2 numbers are:",result)












