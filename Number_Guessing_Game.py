import random

number_to_guess = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100!")

for attempt in range(1, 8):  # sirf 7 chances
    guess = int(input(f"Attempt {attempt}: Guess the number: "))
    if guess == number_to_guess:
        print("Correct!")
        break
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Out of attempts! The number was {number_to_guess}")