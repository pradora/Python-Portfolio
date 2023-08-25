#ToniP
#INF103
#distance Travled

#distance = speed * time

speed = int(input('What is the speed of the vehicle in mph?: '))
time = int(input('How many hours has it travled?: '))

for hours in range(1,time+1):
    distance = speed * hours
    print(hours, distance)
    
