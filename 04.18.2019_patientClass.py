#ToniP
#INF103
#patientClass

class Patient:
    #Constructor
    def __init__(self, fName, mName, lName, street, city, state, zCode, pNum, eName, eNum):
        self.__fName = fName
        self.__mName = mName
        self.__lName = lName
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zCode = zCode
        self.__pNum = pNum
        self.__eName = eName
        self.__eNum = eNum
    
##MUTATOR METHODS##
        
    #setFname -- set first name
    def setfName(self,fName):
        self.__fName = fName

    #setmName -- set middle name
    def setmName(self,mName):
        self.__mName = mName

    #setlName -- set last name
    def setmName(self,lName):
        self.__lName = lName

    #setStreet -- set street address
    def setStreet(self,street):
        self.__street = street

    #setCity -- set city name
    def setCity(self,city):
       self.__city = city 

    #setState -- set state
    def setState(self,state):
       self.__state = state

    #setzCode -- set zip code
    def setzCode(self,zCode):
        self.__zCode = zCode

    #setpNum -- set phone number
    def setpNum(self,pNum):
        self.__pNum = pNum

    #seteName -- set emergency name
    def seteName(self,eName):
        self.__eName = eName

    #seteNum -- set emergency phone number
    def seteNum(self,eNum):
        self.__eNum = eNum
    
##ACCESSOR METHOD##

    #getfName -- update name
    def getfName(self):
        return self.__fName

    #getmName -- update middle name
    def getmName(self):
        return self.__mName

    #getlName -- update last name
    def getlName(self):
        return self.__lName

    #getStreet -- update street address
    def getStreet(self):
        return self.__street

    #getCity -- update city
    def getCity(self):
        return self.__city

    #getzCode -- update zip code
    def getzCode(self):
        return self.__zCode

    #getpNum -- update phone number
    def getpNum(self):
        return self.__pNum

    #geteName -- update emergenct name
    def geteName(self):
        return self.__eName

    #geteNum -- update emergency phone number
    def geteNum(self):
        return self.__eName

    def __str__(self):
        result = 'Name: ' +self.__fName + ' ' +self.__nName+ ' ' +self.__lName + '\n' + \
                 'Address: ' + self.__street + ' ' + self.__city + ' ' + self.__state + '\n' +\
                 'Phone Number: ' + self.__pNum + '\n' +\
                 'Emergency Contact' + self.__eName + ' ' + self.__eNum + '\n'
        return result
                 
        





