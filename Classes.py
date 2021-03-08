

# Parent class 

class User:
    name = ' '
    account_number = 0
    email = ' '
    
# these are a child class and (User) will add the parent attributes

class Ceo(User):
    base_pay = '100k','Salary'
    
class Employee(User):
    Department = 'Store Manager'
    To_do_list = 'Open Store' 
    
