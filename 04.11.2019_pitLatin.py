# ToniP
# inf103
# Pig Lating

#remove extra space at the end of ouput
def main():
    sentence = input('Enter a sentence: ').upper()
    words = sentence.split()
    result = ''

    for word in words:
        if word.isalnum():
            if len(word) > 1:
               result = result + word[1:] + word[0] + 'ay' + ''
            else:
                result = result + word[1:] + word[0] + 'ay' + ''
        else:
            print ('Use alphanumeric data only...')
            main()
            
    print(result)




#train of thought:
    #result = result + word[1:] + word[0] + 'ay'
        #example: word = SLEPT
            # word[1:] = LEPT
            # word [0] = s
            # AY
