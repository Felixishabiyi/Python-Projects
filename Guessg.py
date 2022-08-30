#Import the random module
import random

#random variable for the random number between 1 and 100
random = random.randint(1, 100)

#guess variable is set for the user input
guess = int(input("Enter an integer from 1 to 100: "))

#Setting the score variable to initialize the score to 100
score = 100

#Setting a while loop
while random != guess:
    
    #To deduct 10 point every time the user get a wrong answer
    score -= 10
    print('Your present score is', score)
    
    #if statment on what the program should run if the guess number is greater or lesser than the random number
    if guess < random:
        sub = random - guess
        print ("Add", sub, 'To your inital guess to get the answer')
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > random:
        sub2 = guess - random
        print ('subtract', sub2, 'To your initial guess to get the answer')
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("you guessed it!")
        break