#ToniP
#INF103
#employeeClass

class Employee:

    def __init__(self, name, idNum, dept, title):
        self.__name = name
        self.__idNum = idNum
        self.__dept = dept
        self.__title = title
        
    ##ACCESSOR METHOD##

    #getName -- update name
    def getName(self):
        return self.__name

    #getIdnum -- update id
    def getIdnum(self):
        return self.__idNum

    #getDept -- update department
    def getDept(self):
        return self.__dept

    #getTitle -- update job title
    def getTitle(self):
        return self.__title 
    
    ##MUTATOR METHOD##
