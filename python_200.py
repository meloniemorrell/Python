class soccer_player:
    def __init__(self):
        self._name= "Dave"  # protected attribute 
        self.__score= 5 # private attribute

    def PrintScore(self):
        return self.__score

S = soccer_player()

print(S.score)
print(S.PrintScore())
print(S._score)

object = soccer_player() #protected object
print(object._name)





