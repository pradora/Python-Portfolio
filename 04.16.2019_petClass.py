#ToniP
#INF103
#petClass

class Pet:
    #constructor
    def __init__(self, name, aType, age):
        self.__name = name
        self.__aType = aType
        self.__age = age
        
##MUTATOR METHODS##
    #set_name - update name
    def set_name(self,name):
        self.__name = name

    #set_animal_type - update aType
    def set_animal_type(self,aType):
        #mutator
        self.__aType = aType

    #set_age - update age
    def set_age(self,age):
        self.__age = age

##ACCESSOR METHODS##
    #get_name -- returns name
    def get_name(self):
        return self.__name

    #get_animal_type -- returns animal type
    def get_animal_type(self):
        return self.__aType

    #get_age -- returns pet age
    def get_age(self):
        return self.__age
    
