#ToniP
#INF103
#maryLittleLamb

#lineNubmbers - add line nums in front of line
def lineNumbers(textFile):
    counter = 1
    newFile = '' #empty string
    for line in textFile:
        newFile += '/*' + str(counter) + '/*' + line
        counter += 1 #increment counter
    return newFile
    


def main():
    
    #ask user for input file name
    fileName = input('Enter File Name: ')
    outfname = input('Enter outpur filename:')
    #open file
    lambText = open(fileName + '.txt', 'r')
    #get modified file from lineNumbers function
    newText = lineNumbers(lambText)
    lambText.close()

    #output text file
    outFile = open(outfname + '.txt', 'w')#write out file
    outFIle.write(newText)
    outfile.close()

main()
