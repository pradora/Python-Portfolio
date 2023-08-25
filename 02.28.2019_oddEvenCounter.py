#ToniP
#INF103
#oddEvenCounter

#library for random numbers
import random

#main -- run program
def main():
    odd = 0 # keep count of odd nums
    even = 0 # keep ount of even nums
    
    for x in range(100):
        # store random number in rNum
        rNum = random.randint(0,1000)
        
        #even
        if rNum % 2 == 0:
            even += 1

        else:
            #odd
            odd += 1
    print(odd, even)

        
    






main()
