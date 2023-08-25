#ToniP
#INF103
#petDriver

from petClass import *

def main():
    #get input from user

    pName = input("Enter your pet's name: ")
    pType = input("Enter your pet type: ")
    pAge  = input("Enter your pet's age:  ")

    ####user's Pet
    #create an instance of pet
    uPet = Pet(pName,pType,pAge)

    ####display pet information
    print("Pet's name: ", uPet.get_name())
    print ("Pet's tyep:", uPet.get_animal_type())
    print("Pet's age: ", uPet.get_age())
    

main()#call main
