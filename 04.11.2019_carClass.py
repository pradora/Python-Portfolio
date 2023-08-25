#ToniP
#INF103
#classExample

class Car:
    #constructor
    def __init__(self,color,make,model):
        self.__color = color
        self.__make = make
        self.__model = model
        self.__speed = 0

    ##ACCESSOR METHOD##
    #getMake -- get make of car
    def getMake(self):
        return self.__make

    #getSpeed -- current speed of car
    def getSpeed(self):
        return self.__speed
    
    ##MUTATOR METHOD##

    #accelerate -- increase speed by 5
    def accelerate(self):
        self.__speed += 5

    #decel -- decrease speed by 2
    def decel(self):
        self.__speed -= 2

    #setMake -- change make of car
    def setMake(self,make):
        self.__make = make
        
