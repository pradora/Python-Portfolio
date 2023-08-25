#ToniP
#INF103
#caloriesBurned

#dsiplay the number of calories burned after 10,15,20,25, and 30 mins

print ('Minutes\tCalories Burned')
for minutes in range(10,35,5):
    cals = minutes * 4.2
    print(minutes, '\t', cals)
