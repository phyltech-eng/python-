#ask the user to input a number of dice to roll
#if the user enters y
#generate a random number between 1 and 6
#print them
#if the user enters n
#print thankyou message
#terminate the program
#else #print an error message and ask again
import random

print("Welcome to the Dice Roller!")

while True:
    choice = input("Do you want to roll a dice? (y/n): ").strip().lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled a {die1} and a {die2}.")
    elif choice == 'n':
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' to roll the dice or 'n' to exit.")
