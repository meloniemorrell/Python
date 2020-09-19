class Residence:
    structure = 'brick'
    flooring = 'wood'
    floors = 2
    private = True

    def getresidentType(self):
        entry_structure = input("Enter material: ")
        entry_flooring = input("Enter flooring type: ")
        entry_floors = input("Enter number of floors: ")
        entry_private = input("Enter True or False: ")
        if entry_private == "True":
            print('true')    
        elif entry_private == "False":
            print('false')

class MultiFamily(Residence):
    number_of_units = 100
    parking = 'garage'
    gated = True

    def getresidentType(self):
    entry_structure = input("Enter material: ")
    entry_flooring = input("Enter flooring type: ")
    entry_floors = input("Enter number of floors: ")
    entry_gated = input("Enter True or False: ")
    if entry_gated == "True":
        print('true')    
    elif entry_gated == "False":
        print('false')



class SingleFamily(Residence):
    number_of_homes = 100
    parking = 'garage'
    security = True

    def getresidentType(self):
        entry_structure = input("Enter material: ")
        entry_flooring = input("Enter flooring type: ")
        entry_floors = input("Enter number of floors: ")
        entry_security = input("Enter True or False: ")
        if entry_security == "True":
            print('true')    
        elif entry_security == "False":
            print('false')

structure = Residence()
structure.getresidentType()
        
homeowner = MultiFamily()
homeowner.getresidentType()

homeowner = SingleFamily()
homeowner.getresidentType()


        
