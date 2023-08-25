#ToniP
#INF103
#romanNumerals

#promts user to enter a numver within the range 1-10
num = int(input('Please enter a number 1 to 10: '))

#display the roman numeral version of that number
if num == 1:
    print('I')
    
elif num == 2:
    print('II')

elif num == 3:
    print('III')

elif num == 4:
    print('IX')

elif num == 5:
    print('V')

elif num == 6:
    print('VI')

elif num == 7:
    print('VII')

elif num == 8:
    print('VIII')

elif num == 9:
    print('IX')

elif num == 10:
    print('X')

else:
    print('Number not recognized')

#if number is ouside the range of 1-10,the program should display error message
