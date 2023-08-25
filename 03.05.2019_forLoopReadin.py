#ToniP
#INF103
#for loop readline

# read in file
inFile = open('names.txt','r')

#read every line with for loop
for line in inFile:
    print(line, end='')

#close link
inFile.close()
