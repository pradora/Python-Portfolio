#ToniP
#INF103
#colorMixer


#get the user to enter the names of two primary colors
c1 = input('Enter 1st primary color(Red, Blue, or Yellow): ')
c2 = input('Enter 2nd primary color(Red, Blue, or Yellow): ')


#r,b = purple
if c1.lower() == 'red' or c1.lower() == 'blue' and \
   c2.lower() == 'blue' or c2.lower() == 'red':
    print('Purple')

#r,y = orange
elif c1.lower() == 'red' or c1.lower() == 'yellow' and \
     c2.lower() == 'yellow' or c2.lower() == 'red':
    print('Orange')
    
#b,y = green
elif c1.lower() == 'yellow' or c1.lower() == 'blue' and \
     c2.lower() == 'blue' or c2.lower() == 'yellow':
    print('Green')

#if user enters anything other than r,b, or y: display error message
else:
    print('Not a valid entery.')

#display the name of the secondary colors






