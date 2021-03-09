

# Parent class

class Ceo:
    name = "Jerry"
    email = " JerrySpringer@gmail.com"
    password = "Youarenotthefather1234"

    def getLoginInfo(self):
        entry_name = input("Please enter your name: ")
        entry_email = input("Please enter your email: ")
        entry_password = input("Please enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The email or password is incorrect, please try again.")

#Child Class Customer
class Customer(Ceo):
    mailing_address = " "
    cart = 0

# This is the same method as the one in the parent class "user"
# the difference is entry_mailing_address

    def getLogInfo(self):
        entry_name = input("Please enter your name: ")
        entry_email = input("Please enter your email: ")
        entry_mailing_address = input("Please enter your mailing address: ")
        if (entry_email == self.email and entry_mailing_address == self.mailing_address):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The email or mailing address is incorrect")

# another child class
class Employee(Ceo):
    hourly_pay = 12.50
    department = "Bakery"
    employee_number = "236712"


# This is the same as the parent method


    def getLoginInfo(self):
        entry_name = input("Please enter your name: ")
        entry_email = input("Please enter your email: ")
        entry_employee_number = input("Please enter your employee number: ")
        if (entry_email == self.email and entry_employee_number == self.employee_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The employee number or email is incorrect")



        









    
            
            
        
        
