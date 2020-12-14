class Employee:  #! This is class Which acts as a TEmplate to Store contents in it.
    def __init__(self,fname,lname,salary):  #!Also known as (Constructor)
        #? It helps to store the COntents or the data by creating objects.  

        self.fname= fname
        self.lname= lname      #!Assigning the data name as objects
        self.salary= salary
        
deep=Employee('deepraj','baidya',200000000)
raj=Employee('raj','radhe',200000)

#? Giving Data

print(deep.lname, raj.lname)  #* PRinting the Values