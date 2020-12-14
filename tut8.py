
# & Property Decorators, Setters & Deleters

class Employee:
    inc = 1.5

    def __init__(self, fname, lname, salary):

        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.inc = 1.3
        # self.email = fname + lname + '@gmail.com'   #@Adding an object will adds the fname and lname as gives the email, but for accessing the changed value we must create a separeate function

    def increase(self):
        self.salary = self.salary*Employee.inc

    # % It enable us to treat the function as an Attribute with which we can easily change the email as we want. {But still It can't set the email}
    @property
    def email(self):  # ^ Defining the function to print the email with changed values also
        # @ The . will help us to distinguish between lastname and firstname
        return (f"{self.fname.lower()}.{self.lname.lower()}@gmail.com")

    @email.setter  # $ We use setter to set the email
    def email(self, give_email):  # ! Giving an Argument (give_email)
        self.email = give_email

    @classmethod
    def cng_inc(cls, amount):
        cls.inc = amount


if __name__ == "__main__":
    deep = Employee('Deepraj', 'Baidya', 200000000)
    raj = Employee('Raj', 'Singhania', 200000)

    print(deep.email, raj.email)
    # % as changing the lname here doesnot change the email so we have to create a specific func for this purpose
    raj.lname = 'Mukherjee'
    print(raj.email)
    # raj.email()="mukherjeeraj@gmail.com"   #@ We still can't change the email the way we want, and to avoid this situation by using Poperty Decorators
