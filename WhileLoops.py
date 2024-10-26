### Part Two -- your code goes here. 
import random


secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Hurray! You've guessed the number!")
