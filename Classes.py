

# Parent class 

class User:
    name = 'No name Provided'
    email = ' '
    password = '12345hhyt'
    account_number = 0

# these are a child class and (User) will add the parent attributes

class Employee(User):
    base_pay = 15.50
    department = 'Team Lead'

class Customer(User):
    mailing_address = ' '
    mailing_list = True
