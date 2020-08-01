class soccer_player:
    def __init__(self, name, score):
        self._name= "Dave"  # protected attribute 
        self.__score= 5 # private attribute


        soccer_player_a = sp() #protected object
        print(sp_a.name)

        soccer_player_b = sp() #private object
        print(sp_b.score)
