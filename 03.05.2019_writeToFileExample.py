#ToniP
#INF103
#write to file

outFile = open('output.txt','w')

#data
line1 = 'hello world'
line2 = 1200.31
line2 = 'spam and eggs'
line3 = '#'

#write to file
outFile.write(line1 + '\n')
outFile.write(str(line2)'\n')

#close file-- flush channel
outFile.close()
