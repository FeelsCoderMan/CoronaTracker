from random import randint

def guessingNumber():
    print('I am thinking of a number between 1 and 20')
    myRandomNumber=randint(1,20)
    guess=int(input('Take a guess.'))
    counter=0
    while guess!=myRandomNumber:
        counter+=1
        if guess<myRandomNumber:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')
        guess = int(input('Take a guess.'))
    print('Good job! You guessed my number in {} guesses'.format(counter))
guessingNumber()



