#ToniP
#INF103
#procedureClass

class Procedure:
    #constructor
    def __init__(self, proName, proDate, drName, proCharge):
        self.__proName = proName
        self.__proDate = proDate
        self.__drName = drName
        self.__proCharge = proCharge

##MUTATOR METHODS##

    #setproName -- set prodcedure name
    def setproName (self, proName):
        self.__proName = proName

    #setproDate -- set procedure date
    def setproDate(self, setproDate):
        self.__proDate = proDate

    #setdrName -- set doctors name
    def setdrName(self,drName):
        self.__drName = drName

    #setproCharge -- set procedure charge
    def setproCharge(self,proCharge):
        self.__proCharge = proCharge

##ACCESSOR METHOD##

    #getproName -- update prodcedure name
    def getproName(self):
        return self.__proName

    #getproDate -- update procedure date
    def getproDate(self):
        return self.__proDate

    #getdrName -- update doctor name
    def getdrName(self):
        return self.__drName

    #getproCharge -- update procedure charge
    def getproCharge(self):
        return self.__proCharge
        
