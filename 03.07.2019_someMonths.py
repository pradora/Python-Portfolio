#ToniP
#INF103
#someMonths -- remove r

#retracror -- extracts months with 'r' in it
def rExtractor(lMonths):
    rMonths = '' #empty string
    for month in lMonths:
        if 'r' in month:
            #month with r in it
            rMonths += month
    return rMonths


def main():
    
    #read in file
    months = open('months.txt')
    rMonths = rExtractor(months)                        
    months.close()

    #output data
    outFile = open('rMonths.txt', 'w')
    outFile.write(rMonths)
    outFile.close()







main()#call main
