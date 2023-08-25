#Tonip
#INF103
#lineNumbers

def main():
    #counter
    count = 1
    
    #ask user for the name of a file
    fileName = input('Enter file name:')

    #program should dispaly contents of the file wil a line number followed by a colon
    inFile = open(fileName + '.txt')

    #iterate through every line, add numbers
    for line in inFile:
        print(count, ':', line, sep='',end='')
        count += 1
    #unlink file
    inFile.close()
main()


