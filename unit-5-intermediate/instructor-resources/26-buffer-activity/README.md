### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Brandi

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack @brandib
--->

# Intermediate Python: Practice Problems

In this homework, you're going to write code for a few problems. Like before, we'll be practicing new material, but you may need to break out your skills from older material!

You will practice these programming concepts we've covered in class: FIXME
* Using `itertools` and `random` functions
* Type conversion and more advanced variable usage
* Debugging code that doesn't work using print statements
* Scripting and file I/O
* Using list comprehensions to simplify list creation
* Using functions with parameters
* Using dictionaries and sets
* Declaring and using classes to make objects
* Demonstrating inheritance and method overriding
* Using a variable number of keyword arguments

In this homework, you're going to write code for a few problems. We'll be building on older material like lists, loops, and functions, as well as adding in some practice from the new materials.

------------

## Deliverables

For each of the challenges listed below, you will create a new `.py` file and write code to solve the problem. For example, you would create `problem1.py` with your solution code to the first problem. Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following command:*

```python
python problem1.py
```

> **Hint**: Make sure you are printing something out with the print statement! Otherwise, you won't see any output from running your program!


## Requirements:

* By the end of this, you should have 5 different `.py` files (one for each problem).

------------

## Problem 1:

### Skill You're Practicing: Generating random numbers, type conversion

Make your own version of the `Guess A Number` game. Generate a random integer and store it in a variable called `answer`. Print a statement asking the user to guess a number.

If the user's guess is:
* Higher than the `answer`: print `That is too high!`
* Lower than the `answer`: print `That is too low!`
* Exactly the `answer`: print `That's it! You win!`

Your program should keep prompting the user until they get the answer correct.

#### Example Output
```
I have thought of a number between 1 and 10.
Please guess what it is:
> 4
That is too low!
> 8
That is too high!
> 6
That's it! You win!
```

> **HINT**: User input comes to you as a string. How can you make it into an integer so you can properly compare the user's guess with the `answer` (which is an integer)?
> **HINT**: You can set a variable to `False` or `True`.

------------

## Problem 2: D'Oh!

### Skill You're Practicing: Using Try-Except Statements, Error Handling

Bart Simpson has gotten ahold of your program from problem 1 and started entering a bunch of values that are NOT numbers! How do you handle it?

Create a new file with your code from problem 1, and modify it to print `D'Oh! That is NOT a number, Bart!` if the user doesn't enter an integer.

#### Example Output
```
I have thought of a number between 1 and 10.
Please guess what it is:
> Eat My Shorts!
D'Oh! That is NOT a number, Bart!
Please guess what it is:
> Ay Caramba!
D'Oh! That is NOT a number, Bart!
Please guess what it is:
> 5
That is too low!
Please guess what it is:
> 8
That's it! You win!
```

> **HINT**: the `continue` keyword can be called in a loop and means "skip the rest of this loop iteration". It may be useful to call this in an `except` clause.
------------

## Problem 4:

### Skill You're Practicing: Debugging Built-In Errors

Copy the code out of the repl below into your file, and fix the errors in the code. Don't change the `rainbow`'s contents.

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-eod-hw-4?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

#### Expected Output
```
The rainbow's name is Roy G. Biv
I'll be taking that gold!
red
orange
yellow
green
blue
What color is indigo?
violet
102
100.0
```

> **HINT**: You may encounter: NameError, SyntaxError, IndentationError, KeyError, TypeError, etc. Refer to the class notes for common causes of these errors.

## Problem 1: Call Me! (Maybe)

### Skill You're Practicing: Accessing dictionaries, writing functions, and passing parameters

Write a function called `get_contact` that has two paramters. The first will be a dictionary called `contacts` and the second will be a string called `name` that you would like to look up the phone number for.


#### Example Test Code
```python
contacts = {
  "Carly": "333-3333",
  "Blondie": "444-4444",
  "Jenny": "867-5309"
}
name = "Jenny"

phone_number = get_contact(contacts, name)

print("The phone number of", name, "is", phone_number)
```

#### Example Test Output
```
The phone number of Jenny is 867-5309
```

**Hint 1:**

Refer to your class notes for details about how to use dictionaries.

**Hint 2:**

As a reminder, let's walk through and example of creating, assigning to, and checking if a value is in a dictionary.

```python
# Creating a dictionary called my_dict
my_dict = {}

# Assigning key-value pairs to my_dict
my_dict["foo"] = 1

# Checking whether my_dict contains the key "bar"
if "bar" in my_dict:
    print("bar is here")
else:
    print("bar is not here") # This is what prints
```

**Hint 3:**

Careful! Python requires that you insert a key into a dictionary before you try to modify its value. If you try to access a dictionary at a key that hasn't been added you'll get an error and the program will crash. Remember to use an if statement to see if a key is `in` a dictionary before you try to read it!

```python
d2 = {}
d2["foo"]
# KeyError: 'foo'
```
------------

## Problem 5: Hey Jude, don't make me count!

### Skill You're Practicing: Using dictionaries and writing a function with a parameter

Write a function called `letter_counter` that returns a dictionary called `counts` which has a character as the key and a count as a value. The goal is to count up the number of occurrences of each letter in a string.

Here is how your function will be called, and what is expected as the output.

#### Example Test Code
```python
word_to_count = "banana"

result = letter_counter(word_to_count)

print(result)
```

#### Example Test Output
```python
{'b': 1, 'a': 3, 'n': 2}
```

**Hint 1:**

Remember that you can iterate over a string one letter at a time using a for loop.
```python
for letter in "alpha":
    print(letter)
```

**Hint 2:**

Remember to write a return statement at the end of your function. No code will execute after the return statement, because the return statement also exits the function. What you return from the function will be assigned to the variable `result` in the example above.


**Hint 3** Think you have the answer?

To really test your function, try putting in a whole song as your string! Here are the lyrics of [Hey Jude](https://repl.it/@GAcoding/Python-02-HW-2) already written into a python string. Here's the expected output:

```python
{'H': 4, 'e': 143, 'y': 45, ' ': 368, 'J': 23, 'u': 53, 'd': 52, ',': 44, 'o': 69, 'n': 191, "'": 11, 't': 84, 'm': 23, 'a': 205, 'k': 15, 'i': 33, 'b': 19, '.': 20, 'T': 7, 's': 18, 'g': 11, 'r': 49, 'R': 3, 'l': 24, 'h': 208, 'c': 5, 'f': 7, 'Y': 3, 'w': 11, 'A': 2, 'p': 4, 'D': 1, 'F': 1, 'B': 2, 'N': 18, 'v': 2, 'S': 1, 'j': 1}
```
