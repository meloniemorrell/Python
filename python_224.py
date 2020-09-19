from abc import ABC, abstractmethod

class touchscreen(ABC):
    def communicate(self):
        return self.communicate
        

    
    @abstractmethod
    def tablet(self):
        pass

class smartphone(touchscreen):
    def touchscreen(self):
        return self.touchscreen
    
obj1 = smartphone()
obj2 = touchscreen()

print(obj1.smartphone())
print(obj2.touchscreen())
