
#* Inheritance

class Employee:
    inc=1.5 
    def __init__(self,fname,lname,salary): 
        self.fname= fname
        self.lname= lname      #! Assigning the data name as objects
        self.salary= salary
        
    def increase(self):
        self.salary=(self.salary*Employee.inc)
        return self.salary
deep=Employee('deepraj','baidya',200000000)

print(deep.increase())
#? Creating another Class which will have all the Methods and attributes of Class Employee

class Programmer(Employee):  #! Also known  as Super class
    def __init__(self, fname, lname, salary,proglang,exp):   #// To Recall all the values of class Employee
        super().__init__(fname, lname, salary) #? It calls the constructor of the class from which the super class is being inherited.
        self.proglang=proglang
        self.exp=exp
    
    def increase(self):   #// In this way we can use an existing function and change it for any partiucular Inherited Class
        self.salary=int(self.salary*(Employee.inc+0.2))
        return self.salary     #? To return the salary


deep=Programmer('deepraj','baidya',200000000,'Python and C++','Newbie')
raj=Programmer('raj','radhe',200000,'C and C#','2+ yrs')

print(f"{deep.proglang}, {deep.exp}, {deep.salary}")
print(f"{raj.proglang}, {raj.exp}")

# print(help(Employee))  #! it is a built in function that helps...

print(deep.increase())
print(help(Programmer))