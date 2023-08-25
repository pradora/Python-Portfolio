#ToniP
#
#

def main():
    months = ["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
    rTotal = [] #empty list for rainfall
    count = 1
    for mon in months:
        rainFall = float(input("Enter rainfal for " + mon + ': '))
        rTotal.append(rainFall)

    #rainfall year total
    total = sum(rTotal)
    avg = total /len(rTotal)
    lo = min(rTotal)
    hi = max(rTotal)
                
    print("The average rainfall in inches is: ",avg)
    print("Total amount of rainfall: ",total)
    print("Most amount of rain: ", months[rTotal.index(hi)], '= ',hi)

    print("Least amount of rain: ",months[rTotal.index(lo)], '= ', lo)

main()
