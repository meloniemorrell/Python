class soccer_player:
    def __init__(self):
        self._name= "Dave"  # protected attribute 
        self.__score= 5 # private attribute


object = soccer_player() #protected object
print(object._name)

object = soccer_player() #protected object
print(object.__score)

