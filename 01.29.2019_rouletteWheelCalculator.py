#ToniP
#INF103
#rouletteWheelColor

#ask user to enter a pocket number
n1 = int(input('Enter a number 0 to 36: '))

#display green, red, or black
#pocket 0 is green
if n1 == 0:
    print('Green')

#1-10, odd is red, even is black
elif n1 >= 1 and n1 <= 10:
    if n1 % 2 == 1: #odd
        print('pocket is black')
    else: print ('pocket is red') #even    

#11-18, odd is black, even is red
elif n1 >= 11 and n1 <= 18:
    if n1 % 2 == 1: #odd
        print('pocket is red')
    else: print ('pocket is black') #even   
    
#19-28, odd is red, even is black
elif n1 >= 19 and n1 <= 28:
    if n1 % 2 == 1: #odd
        print('pocket is red')
    else: print ('pocket is black') #even   

#29-36, odd is black, even is red
elif n1 >= 29 and n1 <= 36:
    if n1 % 2 == 1: #odd
        print('pocket is black')
    else: print ('pocket is red') #even   

#display error message if not 0-36
else:
    print('invalid entery')
