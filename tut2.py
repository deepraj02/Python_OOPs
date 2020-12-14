
#!Instance and Class variabele

class Employee:
    inc=1.5  #?Variable to store increased salary % 
    #!Also Known as Instances.
    
    def __init__(self,fname,lname,salary):    

        self.fname= fname
        self.lname= lname      
        self.salary= salary
        self.inc=1.3
    
    def increase(self):
        self.salary=self.salary*Employee.inc

#?self.inc will search for the inc in the constructor
#?Employee.inc will search for the inc in the class


deep=Employee('deepraj','baidya',200000000)
raj=Employee('raj','radhe',200000)

print(deep.salary)
deep.increase()
print(deep.salary)

print(Employee.__dict__) #! TO print all the values of the class Employee
