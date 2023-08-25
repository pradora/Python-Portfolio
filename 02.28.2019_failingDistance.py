#ToniP
#INF103
#fallingDistance

#distance = 1/2*gt**2

#falling distance
    #returns d - distance object has fallen
        #fallen in time t

def fallingDistance(t):
    g = 9.8 #gravity
    d = 1/2*g*t**2
    return d
    
#main function
def main(): 
    print('Time\t Distance fallen(meters)')
    for t in range(1,10):
        d = fallingDistance(t)
        print(t, '\t',format(d,'.2f'))

main()# call main
    
