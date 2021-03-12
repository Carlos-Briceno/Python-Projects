
# This is protected 

class Secret:

    def __init__(self):
        self._protectedVar = 0


    def __init__(self):
        self.__privateVar = 0

    def getPrivate(self):
        print(self.__privateVar)  # this is a new value "privateVar

    def setPrivate(self, private):
        self.__privateVar = private


obj = Secret()
obj._protectedVar = ('Protected')
print(obj._protectedVar)
obj.getPrivate()
obj.setPrivate('Private') # this will print out self.privateVar
obj.getPrivate()
