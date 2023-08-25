#ToniP
#INF103
#randomNumberGuessingGame

#generates a random number in the range of 1-100
import random
def rando(number):
    num = random.randint(1,3)
    return num
randomNum = random.randint(1,5)
def main(): 
    
    #asks the user to guess the number
    print("I'm thinking of a number from 1 to 100...")
    guess = int(input('Guess a number from 1 - 100: '))
    
    
#if the users guess is high display the number is too high guess again
#if guess is to low, print number is to low
    
    while guess == randomNum:
        rando(guess)
        guess = int(input('Guess a number from 1 - 100: '))
        while guess != randomNum:
            
            if randomNum < guess:
                print('Guess is to high, please guess again')
                guess = int(input('Guess a number from 1 - 100: '))
            elif randomNum > guess:
                print( 'Guess is to low, please guess again')
                guess = int(input('Guess a number from 1 - 100: '))
        if randomNum == guess:
            print( 'got it')
    
        
        

#congradulate user and generate a new random number

#return main

main()
