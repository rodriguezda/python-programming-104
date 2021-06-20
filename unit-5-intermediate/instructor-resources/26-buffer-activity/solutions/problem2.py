import random

answer = random.randint(1, 10)
guessed = False

print("I have thought of a number between 1 and 10.")

while not guessed:
  current_guess = input("Please guess what it is:")

  try:
    current_guess = int(current_guess)
  except:
    print("D'Oh! That is NOT a number, Bart!")
    continue # This skips the rest of this loop iteration

  if current_guess == answer:
    print("That's it! You win!")
    guessed = True
  elif current_guess < answer:
    print("That is too low!")
  elif current_guess > answer:
    print("That is too high!")
