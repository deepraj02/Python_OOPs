
#! Creating Class Methods

class Employee:
    inc=1.5 
    
    def __init__(self,fname,lname,salary):    

        self.fname= fname
        self.lname= lname      
        self.salary= salary
        self.inc=1.3
    
    def increase(self):
        self.salary=self.salary*Employee.inc
    
    @classmethod  #!Its a decorator which denotes that this is a Class MEthod
    def cng_inc(cls,amount):  #? Creating the class Method. (NEcessary to take the whole Class as an Argument)  {Giving a class as cls as an argumrent}
        cls.inc=amount   #!To increase the amount by giving values.
        
        

deep=Employee('deepraj','baidya',200000000)
raj=Employee('raj','radhe',200000)

print(deep.salary)

Employee.cng_inc(2)  #* To change the salary object by using the class method{by entering the value for increment}
deep.increase()       #// Calling the Increase Function

print(deep.salary)
