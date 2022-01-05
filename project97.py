import random
number = random.randint(1,9)
chance = 5

print(' Guess a number between 1-9! ')



while chance > 0:
    guess = int(input(' Enter your guess: '))
    print(guess)
    chance = chance - 1
    if (guess < number):
        print(' your guess is to low...guess a higher number. ')
        
    elif (guess > number):
        print(' you guess is to high...guess a lower number. ')
    else:
        print(' YOU WIN!! ')
        break



if (chance == 0):
    print(' YOU LOSE! The number is ' , number)






