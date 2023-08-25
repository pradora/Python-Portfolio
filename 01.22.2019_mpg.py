#ToniP
#INF103
#milesPerGallon

#miles per gallon = miles driven / gallons of gas used
#ask the user for the number of miles driven
MILES = int(input('How many miles have you driven?: '))

#ask for galllons of gas used
GAS = int(input('How many Gallons of gas have you used?: '))

#display miles per gallon
MPG = MILES / GAS
print('Your miles per gallon is: ', format(MPG, '.0f'))
