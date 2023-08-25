#ToniP
#INF103
#pateintDriver

from procedureClass import *
from patientClass import *

def main():

#user input
    fName = input('Enter your first name: ')
    mName = input('Enter your middle name: ')
    lName = input('Enter your last name: ')
    street = input('Enter street address: ')
    state = input('Enter state: ')
    city = input('Enter your city name: ')
    zCode = input('Enter your zip code: ')
    pNum = input('Enter phone number: ')
    eName = input('Enter your emergeny contact: ')
    eNum = input('Enter your emergeny contact phone number: ')

#create an instance of patient
    iPatient = Patient(fName, mName, lName, street, city, state, zCode, pNum, eName, eNum)

#display patient info
    print(iPatient.__str__())
    
#create an instance of procedure
    #iProcedure = 

#call to main
main ()
