### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Brandi

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack at @brandib.
--->

# Advanced Python: Practice Problems

In this homework, you're going to write code for a few problems. Like before, we'll be practicing new material, but you may need to break out your skills from previous units.

You will practice these programming concepts we've covered in class:
* Using `itertools` and `random` functions.
* Type conversion and more advanced variable usage.
* Calling an API to get data using `requests`.
* Debugging code that doesn't work using `print` statements.
* Scripting and file I/O.
* Using list comprehensions to simplify list creation.

------------

## Deliverables

For each of the challenges listed below, you will create a new `.py` file and write code to solve the problem. For example, you would create `problem1.py` with your solution code to the first problem. Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following:*

```python
python problem1.py
```

> **Hint:** Make sure you are printing something out with the `print` statement. Otherwise, you won't see any output from running your program!


## Requirements:

* By the end of this, you should have five different `.py` files (one for each problem).

------------

## Problem 1:

### Skills you're practicing: Generating random numbers and type conversion.

Make your own version of the `Guess a Number` game. Generate a random integer and store it in a variable called `answer`. Print a statement asking the user to guess a number.

If the user's guess is:
* Higher than the `answer`: print `That is too high!`.
* Lower than the `answer`: print `That is too low!`.
* Exactly the `answer`: print `That's it! You win!`.

Your program should keep prompting the user until they enter the correct answer.

#### Example Output
```
I'm thinking of a number between 1 and 10.
Please guess what it is:
> 4
That is too low!
> 8
That is too high!
> 6
That's it! You win!
```

> **Hint 1:** User input comes to you as a string. How can you make it into an integer so you can properly compare the user's guess with the `answer` (which is an integer)?
> **Hint 2:** You can set a variable to `False` or `True`.

------------

## Problem 2: D'oh!

### Skills you're practicing: Using `try`/`except` statements and error handling.

Bart Simpson has gotten ahold of your program from Problem 1 and started entering a bunch of values that are NOT numbers! How do you handle it?

Create a new file with your code from Problem 1 and modify it to print `D'oh! That is NOT a number, Bart!` if the user doesn't enter an integer.

#### Example Output
```
I'm thinking of a number between 1 and 10.
Please guess what it is:
> Eat my shorts!
D'oh! That is NOT a number, Bart!
Please guess what it is:
> Ay, caramba!
D'oh! That is NOT a number, Bart!
Please guess what it is:
> 5
That is too low!
Please guess what it is:
> 8
That's it! You win!
```

> **Hint:** The `continue` keyword can be called in a loop and means "skip the rest of this loop iteration." It may be useful to call this in an `except` clause.
------------

## Problem 3:

### Skill you're practicing: Debugging built-in errors.

Copy the code out of the repl.it below into your file and fix the errors in the code. Don't change the `rainbow`'s contents.

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-eod-hw-3?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

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

> **Hint:** You may encounter: `NameError`, `SyntaxError`, `IndentationError`, `KeyError`, `TypeError`, etc. Refer to the class notes for common causes of these errors.

------------

## Problem 4: Three Commas

### Skill you're practicing: Formatting numbers.

Russ is a billionaire and he'd like to count his wealth in the number of commas it contains. For example, someone who is a millionaire would have only two commas (1,000,000). Russ, however, has three commas and would like to see those commas displayed. Help Russ format his integer so that commas appear when it is printed out. Make sure your program will work for any value of `wealth`.

#### Example Code
```python
wealth = 1000000000
```

#### Example Output
```
1,000,000,000
```

> **Hint:** Look up `format` if you've forgotten how to use it!

------------

## Problem 5: My Favorite TV Characters

### Skills you're practicing: Scripting and debugging.

I'm trying to write a list of favorite TV show characters to a file called `my_characters`. I'm nearly there, but instead of printing the whole list, I'm just getting the last line. Help me out: Can you get the whole list to print to a file?

#### My Code

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-hw-eod-3-prob-5?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


#### Desired Output
```
1: Will Byers
2: Tyrion Lannister
3: Oliver Queen
4: Jean-Luc Picard
5: Malcolm Reynolds
6: The Doctor
7: Sam Winchester
8: Sherlock Holmes
```

#### Actual Output
```
8: Sherlock Holmes
```

> **Hint:** Remember the [spreadsheet](https://www.dropbox.com/s/cqsxfws52gulkyx/drawing.pdf) we looked at earlier? See if it can help!

------------

## Last, But Not Least

You're all done! Wow! Time for a well-earned break!

![](https://media.giphy.com/media/SJsuD0XD2zNug/giphy.gif)
