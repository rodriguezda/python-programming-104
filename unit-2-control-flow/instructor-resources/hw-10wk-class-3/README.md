### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Brandi

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack @brandib.
--->

# Python Conditionals: Practice Problems

In this homework, you're going to write code for two challenge problems.

You will practice these programming concepts we've covered in class:

* Declaring and using lists.
* Using the Python conditionals `if`, `elif`, and `else`.
* Using `for` and `while` loops.

---

## Deliverables

Part of this homework will be code challenges and part will be reading with comprehension questions.

For the reading questions, make a text file called `answers.txt` and use it to compile your answers to all of the numbered questions.

For each of the code challenges listed below, you will create a new `.py` file and write code to solve the problem. For example, you would create `problem1.py` with your solution code to the first problem. Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following:*

```python
python problem1.py
```

> **Hint:** Make sure you are printing something out with the `print` statement! Otherwise, you won't see any output from running your program!


## Requirements

By the end of this, you should have:
* Two different `.py` files (one for each code challenge).
* One text file with answers to the five reading comprehension questions.

---

# Code Challenges

## Problem 1: IOU!

### Skill you're practicing: Writing `for` loops to iterate over a list.

You have a list of Disney characters and you want to find out if each of them contain `i`, `o`, or `u` in their names. Loop through each character in the list and print out the following:

```
If the name contains a "u," print out the name plus "U are so Uniquely U!"
Otherwise if the name contains an "i," print out the name plus "I bet you're Impressively Intelligent!"
Otherwise if the name contains an "o," print out the name plus "O My! How Original!"
Otherwise, print the name plus "Ehh, a's and e's are so ordinary."
```

#### Starter Code

```python
disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]

```

#### Expected Output

```
simba I bet you're Impressively Intelligent!
ariel I bet you're Impressively Intelligent!
pumba U are so Uniquely U!
flounder U are so Uniquely U!
nala Ehh, a's and e's are so ordinary.
ursula U are so Uniquely U!
scar Ehh, a's and e's are so ordinary.
flotsam O My! How Original!
timon I bet you're Impressively Intelligent!
```


> **Hint**: You can determine whether or not a string contains a particular character with an `if` statement. For example, `if "b" in my_string:` will be true if `my_string` contains any b's.

---

## Problem 2: If You're Cold, Sit in a Corner. It's 90 Degrees!

### Skill you're practicing: Writing `while` loops.

Wow! It's 90 degrees Fahrenheit and you are sweating buckets! Luckily you have air conditioning, but it's really old and kind of finicky. It cools the room by three degrees and shuts off, so you have to keep turning it back on until the temperature gets to where you want it to be. Seventy five sounds much more pleasant than 90, so that's what you're shooting for.

```
While the temperature is greater than 75 degrees Fahrenheit, print "The temperature is XX — crank the AC!" and subtract 3 degrees from the temperature.

Once the temperature is cool enough and the loop is done, print "75. Ahh, that's better."
```

#### Starter Code

```python
temperature = 90
```

#### Expected Output

```
Temperature is 90 — crank the AC!
Temperature is 87 — crank the AC!
Temperature is 84 — crank the AC!
Temperature is 81 — crank the AC!
Temperature is 78 — crank the AC!
75. Ahh, that's better.
```

> **Hint:** Make sure that your loop conditional is being updated each iteration. Otherwise you'll end up with an infinite loop!

---

## Reading Material

Read through the examples in these two articles about [`for` loops](https://www.digitalocean.com/community/tutorials/how-to-construct-for-loops-in-python-3) and [`while` loops](https://www.digitalocean.com/community/tutorials/how-to-construct-while-loops-in-python-3) from Digital Ocean. Then, answer the following questions.

1. What is a nested loop?

2. Which kind of loop is based on a conditional statement: `while` loops or `for` loops?

3. When you want to iterate a specific number of times, would you typically use a `while` loop or a `for` loop?

4. Is it possible to loop through a string one letter at a time? What is the example given in the article?

5. Extrapolate from what you learned in the articles: Do you think a `for` loop be nested inside a `while` loop? Why or why not?

---

## All Done!

Time to get some rest!

![](https://media.giphy.com/media/13h8Y1oVRO30KQ/giphy.gif)
