import random
import time

print("Welcome to my guessing game!")
time.sleep(1)
print("Pick a number between 1 and 100.")
time.sleep(1)
print("I'm picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 0

while guess != correct_number:
    guess_count += 1
    time.sleep(1)
    if guess < correct_number: #guess is lower than correct_number
            guess = int(input("Incorrect! Guess higher: "))
    if guess > correct_number: #guess is higher than correct_number
            guess = int(input("Incorrect! Guess lower: "))
time.sleep(1)
print(f"You got it! It took you {guess_count} tries.")
time.sleep(2)
print("Bye now!")

