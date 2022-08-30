#Import the random module
import random

#passing the input variable to the user
user = int(input('Enter 1 To Roll A Dice'))

#creating a function to roll the dice
def rolldice():
    
    #the shuffle random method is passed to the run variable
    run = random.randint(1,6)
    print ('The number obtained is', run)
        
#a callback function to roll the dice
rolldice()

#deci variable to hold the user input which is a string
deci = str(input('Enter YES To Play Again'))

#setting a while loop to keep the code running depending on the user input
while deci == 'YES':
    user = int(input('Enter 1 To Roll A Dice'))
    rolldice()
    deci = str(input('Enter YES To Play Again'))
    
    #to stop the code running when the user inputs string other than capital YES
    if deci != 'YES':
        break
    
#call back function to roll the dice
rolldice()