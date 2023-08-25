#ToniP
#INF103
#largher than n

#largerThan -- takes a list (numList)
#              and a number n
#              prints numbers greater than n
def largerThan(numList,n):
    for num in numList:
        if n > num:
            print(num)
        else:

def main():
    numList = [1,43,5,66,12]
    n = int(input('Enter a number n: '))
    largerThan(numList,n)
main()


    
            
