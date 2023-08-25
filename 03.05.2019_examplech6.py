#ToniP
#INF103
#File I/O -- reading

inFile = open('names.txt','r')

#read method
#data = inFile.read()

#readline method
line1 = inFile.readline()
line2 = inFile.readline()

#display
print(line1,line2)
print(line2)

#close -- disconnect file from program

inFile.close()
