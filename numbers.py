import random

low = 1
high = 10
answer = random.randint(low, high)
guesses = 0
is_running = True

print("Welcome to python guessing game")
print(f"Guess a number between {low} and {high}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("Not quite.Your guess is out of range")
            print(f"Guess a number between {low} and {high}")

        elif guess < answer:
            print(f"{guess} is too low. Try again")

        elif guess > answer:
            print(f"{guess} is too high. Try again")
        
        else:
            print(f"{guess} is correct. It took you {guesses} guesses to get it right")
            is_running = False
    else:
        print("Invalid number")
        print(f"Guess a number between {low} and {high}")
