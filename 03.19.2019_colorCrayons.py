#ToniP
#INF103
#crayonColors

def colorExtractor(cList):
    sColor = '' # empty string
    for colors in cList:
        if len(colors.rstrip('\n')) <= 6:
            #if color name <= 6, store in sColor
            sColor += colors
    return sColor



def main():
    
    #read in crayon list
    cList = open('crayonColors.txt')
    sColor = colorExtractor(cList)
    cList.close ()

    #ouput Data
    outFile = open('colorList.txt', 'w')
    outFile.write(sColor)
    outFile.close()
    

main()
