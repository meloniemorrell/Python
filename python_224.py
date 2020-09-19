from abc import ABC, abstractmethod

class touchscreen(ABC):
    def communicate(self):
        print('Select here:')
        
   
    @abstractmethod
    def tablet(self):
        pass

class smartphone(touchscreen):
    def tablet(self):
        print('Enter pin here:')
    
obj1 = smartphone()
obj1.tablet()
obj1.communicate()
