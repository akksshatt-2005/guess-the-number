import random
secret_number = random.randint(1, 100)

attempts = 0 max_attempts = 7

print("Welcome to the Number Guessing Game!") print("I have selected a number between 1 and 100.") print("You have 7 attempts to guess it.\n")

while attempts < max_attempts: guess = int(input("Enter your guess: ")) attempts += 1

if guess == secret_number:
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    break
elif guess < secret_number:
    print("Too low! Try again.\n")
else:
    print("Too high! Try again.\n")
if attempts == max_attempts and guess != secret_number: print(f"Game Over! The correct number was {secret_number}.")
