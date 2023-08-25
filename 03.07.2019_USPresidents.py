#ToniP
#INF103
#USPres

#pRange -- prinnts a range of presidents
def pRange(pList,lower,upper):
    pCounter = 1
    for pres in pList:
        if pCounter >= lower and pCounter <= upper:
            print(pCounter, pres.rstrip('\n'))
        pCounter += 1

def main():
    #read in USPres
    pList = open('UsPres.txt')
    
    # ask the user of ranges
    lo = int(input('Enter the lower number of the range: '))
    up = int(input('Enter the upper number of the range: '))

    #call pRange
    pRange(pList,lo,up)
    pList.close()


main()
