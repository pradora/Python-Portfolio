import random
def rando(number):
    num = random.randint(1,3)
    return num
randomNum = random.randint(1,5)

print("I'm thinking of a number from 1 to 100...")
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
rando(randomNum)
guess = int(input('Guess a number from 1 - 100: '))

