#class variables and class methods
#Assigment:
#create a class bank with a class variable bank _name.Add a class method change_bank_name(cls,name)that allows changeing the
#bank name. show that it affects all instances.


#solution
class Bank:
    bank_name = "Default Bank"
    
    def __init__ (self,account_holder):
        self. account_holder = account_holder
        
        @classmethod
        def change_bank_name(cls,name):
            cls.bank_name = name
            
            def display(self):
                print(f"Account Holder:{self.account_holder},Bank:{self.bank_name}")
                Account1 = Bank("MOHIB")
                Account2 = Bank("MUNEEB")
                
                Account1 = display()
                Account1 = display()
                
                Bank.change_bank_name("AL HABAB Bank")
                
                Account1.dispaly{}
                Account2.display{}
                