import random

answer = random.randint(1, 10)
guessed = False

print("I have thought of a number between 1 and 10.")

while not guessed:
  current_guess = int(input("Please guess what it is:"))

  if current_guess == answer:
    print("That's it! You win!")
    guessed = True
  elif current_guess < answer:
    print("That is too low!")
  elif current_guess > answer:
    print("That is too high!")
