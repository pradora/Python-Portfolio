#ToniP
#INF103
#sumOfNumbers

sumNum = 0 #holding running total
num    = 0

#should only enter a negative number when they are finished
print('Enter a series of positive numbers.\n','Enter a negative number when finished',sep='')

#Asks the user to enter a series of positive numbers

while num >= 0:
    sumNum += num

    num = float(input('Please enter numbers: '))
    
#Display the sum of all numbers   
print('this is sum num:',sumNum)



