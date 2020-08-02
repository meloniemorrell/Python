from abc import ABC, abstractmethod
class cooking_chicken(ABC):
    def cook(self, temperature):
        print("What temperature will you cook your chicken? ", temperature)
        #this function tells us to pass in an argument but not how or what kind
        #of data it will be.
    @abstractmethod
    def cook(self,temperature):
        pass

class bakingChicken(cooking_chicken):
        #defining how to implement pmt function from its parent bake class.
    def bake(self, temperature):
        print("It is recommended to bake chicken at 400 degrees".format(temperature))

        obj = bakingChicken()
        obj.cook("400 degrees")
        obj.bake("400 degrees")
