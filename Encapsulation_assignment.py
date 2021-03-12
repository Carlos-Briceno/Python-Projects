
# This is protected 

class Secret:
    def __init__(self):
        self.privateVar = 'Protected'

    def getPrivate(self):
        print(self.privateVar)  # this is a new value "privateVar

    def setPrivate(self, private):
        self.privateVar = private


obj = Secret()
obj.getPrivate()
obj.setPrivate('Private') # this will print out self.privateVar
obj.getPrivate()
