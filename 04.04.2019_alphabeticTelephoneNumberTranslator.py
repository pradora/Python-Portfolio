#ToniP
#INF103
#alphabeticTelephoneNumberTranslator

#process
#abc = 2    
#def = 3
#ghi = 4
#jkl = 5
#mno = 6
#pqrs = 7
#tuv = 8
#wxyz = 9

def main():
#input
#ask the user to enter a 10-character number in the format XXX-XXX-XXXX
    pNum = input("Please enter a phone number in the format XXX-XXX-XXXX:").upper()
    numList = ['2','3','4','5','6','7','8','9']
    result = '' #empty string
    for char in pNum:
        if char.isalpha()== 'A' or char.isalpha() == 'B' or char.isalpha() == 'C':
            char = numList[0]
        elif char.isalpha()== 'A' or char.isalpha() == 'B' or char.isalpha() == 'C':
            char = numList[1]
            
        elif char.isalpha()== 'G'or char.isalpha()== 'H' or char.isalpha()== 'I':
            char = numList[2]
            
        elif char.isalpha()== 'J'or char.isalpha()== 'K' or char.isalpha()== 'L':
            char = numList[3]

        elif char.isalpha()== 'M'or char.isalpha()== 'N' or char.isalpha()== 'O':
            char = numList[4]

        elif char.isalpha()== 'P'or char.isalpha()== 'Q' or char.isalpha()== 'R' or char.isapha() == 'S':
            char = numList[5]

        elif char.isalpha()== 'T'or char.isalpha()== 'U' or char.isalpha()== 'V':
            char = numList[6]

       elif char.isalpha()== 'W'or char.isalpha()== 'X' or char.isalpha()== 'Y' or char.isaplpha() == 'Z':
            char = numList[7]
        result += char #concatenate     


#output
#display the telephone number from letters to number

    
main() #call to main
