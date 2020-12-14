
#* Class Methods As Alternative Constructor 
#// TO only change the Class Methods not the Object


class Employee:
    inc=1.5 
    
    def __init__(self,fname,lname,salary):    

        self.fname= fname
        self.lname= lname      
        self.salary= salary
        self.inc=1.3
    
    def increase(self):
        self.salary=self.salary*Employee.inc
    
    @classmethod  
    def cng_inc(cls,amount):
        cls.inc=amount   
        
        
    @classmethod
    def from_str(cls,emp_string):  #* Creating the Class Method to take input for Employee
        fname, lname,  salary=emp_string.split('-') #//values and how to give Input
        return cls(fname, lname,  salary)    #? How to return the values.(Define the class{which is [cls] here})
    
    
deep=Employee('deepraj','baidya',200000000)
rahul=Employee.from_str("Rahul-Deb-455056")   #!Giving The Input by defining the Class method
raj=Employee('raj','radhe',200000)

print(deep.salary)
# Employee.cng_inc(2)
# deep.increase()
print(rahul.salary)

