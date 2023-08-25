#ToniP
#INF103
#randomNumberGuessingGame

#generates a random number in the range of 1-100
import random

#congradulate user and generate a new random number



def main():
    rNum = random.randint(1,100)
    
    #asks the user to guess the number
    guess = int(input('Guess a number 1-100: '))

    while True:
        if guess > num:
            print('guess is to high')
        elif guess < num:
            print('guess is to low')
        elif guess == num:
            print('congrats')
            #generate a new random number
            rNum = random.randint(1,100)
        guess = int(input('Guess a number 1-100: '))
        
        

main()
