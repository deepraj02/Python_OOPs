# Static Methods In Python oop
#// JAb class ka bhi kaam na ho aur na hi instance ka kaam ho then we use {@staticmethod}

class Office:
    def __init__(self, place, dept):
        self.place=place
        self.dept=dept
        
        
    @staticmethod          
    def isopen(day):
        if day=='sunday':
            return False      #* TO check if office is closed or open using a staticmethod
        else:
            return True

raj=Office('nagar','PR')   #! Creating the object [Not Necessary though 😝]
print(Office.isopen('sunday'))

#? We can also use 
print(raj.isopen('sunday'))

print(Office.isopen('monday'))

