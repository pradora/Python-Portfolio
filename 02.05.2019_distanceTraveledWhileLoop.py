#ToniP
#INF103
#distance Travled

#distance = speed * time

speed = int(input('What is the speed of the vehicle in mph?: '))
time = int(input('How many hours has it travled?: '))
hour = 1 #initialize hour

print ('Hour\tDistance Traveled')
while hour <= time:
    #increment by 1
    hour += 1 # augmented assignment operator
    print(hour, '\t\t', speed * hour)
