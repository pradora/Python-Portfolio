#ToniP
#INF103
#oceanLevels

#ocean level rising at 1.6 mm
oLevelRate = float(1.6) 
oLevel = 0 #running total

#display the number of millimetters have risen in 1-25 years
for year in range(1,26):
    #running sum of ocean rising
    oLevel += oLevelRate
    
    print('year:',year,'\t','millimetter:', format(oLevel, '.2f'))
