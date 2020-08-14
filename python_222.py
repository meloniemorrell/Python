class patient:
    def __init__(self, name, bal):
        self._name=Sally # protected attribute 
        self._balance=5000 # protected attribute

    def __init__(self, name=None, age=None):
        self.__name = 'Pat'  # private attribute 
        self.__age = '50' # private attribute

    def getPrivate(self):
        print(self.__name)

    def setPrivate(self, age):
        print(self.__age)

obj = patient()
obj.getPrivate()
obj.setPrivate(55)
obj.getPrivate()
