def main():
    try:
        #read in file
        file = input("Enter Filename: ")
        inFile = open (file)
        #read every line with for loop
        for line in inFile:
            print(line,end='')

    except FileNotFoundError:
        print ('The file does not exist.')
        print (' please try again.')
        main()
    else:
        inFile.close()
main() #call main
        
