#2.Using cls
#Assignment :
#create a class counter that keeps track of how many objects have beencreated . Use a variable and a class
#method with cls to manage and display the count.

#solution:

class Counter:
    count =0
    def __init__(self):
       Counter. count += 1
       
    @classmethod
    def display_counter(cls):
        print(f"My total created objects are:{cls.count}")
        
        
obj1= Counter()
obJ2= Counter()
obj3= Counter()
obj4= Counter()

Counter .display_counter()