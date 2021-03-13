from abc import ABC, abstractmethod

# this is a parent class
class Credit(ABC):
    def AmountToPay(self, amount):
        print("Your amount to pay: ",amount)

    @abstractmethod
    def amountLeft(self, amount):
        pass

# here is the implement amountLeft function from its parent AmountToPay class
class Paynow(Credit):
    def amountLeft(self, amount):
        print('Your amount paid of {} and your amount left to pay is $53.00 '.format(amount))

obj = Paynow()
obj.AmountToPay("$500.00")
obj.amountLeft("$500.00")
    
    
