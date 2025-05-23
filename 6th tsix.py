#assigment: create a class logger that prints a message when an object is created (constructor)and another messagewhen it is 
#destroyed (destructor).

#solution
class Logger:
   def __init__(self):
        print("Message Before: Logger object created.") #constructor message
   def __del__(self):
            print("Message After: Logger object destructor.")
            
            
log = Logger()
del log