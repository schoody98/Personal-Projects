#Create a number guessing game that takes a random number between (x, x)
#that a player then has to guess, returning output according to how they guessed
#keep track of how many guesses the player has guessed
#max number of tries?

import random
numofguesses = 0

print("Hello! Welcome to the number guessing game, what is your name, friend?")
name = input()

num = random.randint(1, 20)
print("\n")
print("Okay " +name,  ", lets play! Guess a number between 1 and 20, good luck!")


while numofguesses < 6:
    try:
        print("Take a guess:")
        guess = input()
        guess = int(guess)

        numofguesses = numofguesses + 1
    
        if guess < num:
            print("Too low, try again")
            print("\n")

        if guess > num:
            print("Too high, try again")
            print("\n")

        if guess == num:
            break
    except ValueError:
        print("Type a number")
        
if guess == num:
    numofguesses = str(numofguesses)
    print("You win ", name, "! It took you", numofguesses, "tries to win")

if guess != num:
    number = str(num)
    print("You lose! The correct number was ", number)

input("Press enter to exit")
        
    
