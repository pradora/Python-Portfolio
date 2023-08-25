#ToniP
#INF103
#ageClassifer

#ask the user to enter a person's age
age = int(input('How old are you?:'))

#display a message indicating wherher the person is an infant, child, teenager, or adult

#1 less than or equal to= infant
if age <= 1 and age > 0:
    print('You are an infant.')
    
#Older than 1 but younger than 13 = child
elif age > 1 and age < 13:
    print('You are a child.')

#13 - 20 = teenager
elif age >= 13 and age < 20:
    print('You are a teenager.')

#20 or older = adult
elif age >= 20:
    print('You are an adult.')

else:
    print('you dont exist')
