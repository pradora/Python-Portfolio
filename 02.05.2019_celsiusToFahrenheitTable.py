#ToniP
#INF103
#celciousToFarenheitTable

#display celsius tepms 0-20
#F = (9/5 * C) + 32
C = 0 #counter
#Display a table

for C in range(-1,21):
    C += 1
    degree = (9/5 * C) + 32
    print(C, format(degree, '.2f'))
    
