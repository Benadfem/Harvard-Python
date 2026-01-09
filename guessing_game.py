#This is a demo game ripped from Bro code tutorial.
#this is done while I write the code my self.

import random
lowest_number = 1
highest_number = 20

#let's give the count of guesses before the match
guesses = 0
is_running = True

#let's prompt for the guess instruction
print("--------THIS IS A GUESSING GAME --------")

print(f"Select a number from {lowest_number} to {highest_number}")
guess_number = random.randint(lowest_number, highest_number)
while is_running:
    guess = input("Enter your guess: ")
    guesses += 1
    if guess.isdigit():
        guess = int(guess)


        if guess < lowest_number or guess > highest_number:
            print("Guess is Out of range")
        elif guess > guess_number:
            print("Your guess is too high")
            print("Try again!")
            print(f"Select a number from {lowest_number} to {highest_number}")

        elif guess < guess_number:
            print("Your guess is too low")
            print("Try again!")
            print(f"Select a number from {lowest_number} to {highest_number}")

        else:
            print("--------- CORRECT  GUESS---------")
            print(f"The correct guess is {guess}")
            print(f"the number of guess is: {guesses}")
            break

    else:
        print("The guess must be a number ")
        print(f"Select a number from {lowest_number} to {highest_number}")



