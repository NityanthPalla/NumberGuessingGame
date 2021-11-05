
import random
print("Guess The Number")
number= random.randint(1,9)
chances = 0
print("Guess a number (between 1 to 9):")

while chances>5:

    guess =  input ("Enter your number which you are guessing:- ")

    if guess==number:
        print("Congratulations! You won")

        break

    if guess>number:
        print("Your guess is higher than the number")

    if guess<number:
        print("Your guess is lower than the number")

    chances += 1

if not chances < 5:
    print("Oops! You lose the game")                

