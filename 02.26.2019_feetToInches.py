#ToniP
#INF103
#feetToInches

#Define Function
def feetToInches(feet):
    inches = feet * 12
    return inches
######################

#get input from user
feet = int(input("Please enter how many feet: "))

#call back to function
inches = feetToInches(feet)

#display output
print (inches)
