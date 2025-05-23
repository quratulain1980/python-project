#project 6: Bulide compose and Decorate A complete tradition oop practice quratulain
#1. using self
#Assignment :
# Create a class student with attributes name and marks.Use the selfe kyeword to initialize the values
#via a constructor. Add a method display() t
#that prints student details.

# solution:
class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
            print(f"Student Name:{self.name}")
            print(f"Marks:{self.marks}")
                  
student1= Student("Quratulain",95) 
student1.display()
 

