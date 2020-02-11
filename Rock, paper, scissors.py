#Rock, Paper, Scissors!!! 
#Random answer from the computer (Rock, paper, or scissors)
#Best 2/3?

import random
numoflives = 3
numofpoints = 0

weapons = ["Rock", "Paper", "Scissors"]

print("I challenge you, to the death!")
print("\n")
print("Choose your weapon, type 'weapons' to see what you can use")

while numoflives <= 3:
    choice = input(str())
    
    if choice == ("weapons"):
        print(weapons)
        print("\n")
        continue
        
    if choice == random.choice(weapons):
        numofpoints = numofpoints + 1
        print("Ah! That's a point for you!")
        
    elif choice != random.choice(weapons):
        numoflives = numoflives - 1
        print("Ba hah! That's a point for me!")
        
    if numoflives == 0:
        break

    if numofpoints ==  3:
        break

if numofpoints == 3:
    print("Bah! You have bested me!")

elif numoflives == 0:
    print("You lose! I am the better man!")

input("Press enter to exit")


        
        
    



