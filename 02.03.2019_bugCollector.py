#ToniP
#INF103
#bugCollector

total = 0 # counter variable
days = 5 #range of days

#ask for the number of bugs collected for each day
#loop should as forfor the number of bugs collected each day
print('Enter number of bugs collected in 5 days.')
for counter in range(days):
    bug = int(input('Enter number of bugs collected: '))
    total = total + bug

#dispaly the total numer of bugs
print('the total is', total)

