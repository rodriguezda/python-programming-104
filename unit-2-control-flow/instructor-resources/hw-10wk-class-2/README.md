### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Brandi

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack at @brandib.
--->

# Python Conditionals: Practice Problems

In this homework, you're going to write code to solve a few problems.

You will practice these programming concepts we covered in class:
* Declaring and using variables.
* Using mathematical operators.
* Implementing Python conditionals: `if`, `elif`, and `else`.

---

## Deliverables

The first part of this homework is a mini-quiz. You can put all of your answers for that in a single text file.

For each of the code challenges listed below, you will create a new `.py` file and write code to solve the problem. For example, you would create `problem1.py` for your solution code to the first problem. Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following command:*

```python
python problem1.py
```

> **Hint**: Make sure you are printing something out with the `print` statement. Otherwise, you won't see any output from running your program!


## Requirements:

By the end of this, you should have:
* One text file for your mini-quiz questions.
* Two different `.py` files (one for each coding problem).

---

# Part 1: Mini-Quiz

Put your solution into a file called `quiz.txt`.

1. True or false: An `if` statement can live without an `else` statement.

2. True or false: An `else` statement can live without an `if` statement.

3. True or false: An `elif` statement can live without an `if` statement.

4. True or false: An `if` + `elif` statement can live without an `else` statement.

5. True or false: The following statements are equivalent.

```python
if a == True:
```

```python
if a:
```

6. In the following code block, what prints?

```python
a = True
b = True
c = False

if a:
    print("1")

if b:
    print("2")

if c:
    print("3")

if a and b:
    print("4")

if a and c:
    print("5")

if b and c:
    print("6")

if a or b:
    print("7")

if a or c:
    print("8")

if b or c:
    print("9")
```

7. In the following code block, what prints?

```python
a = False
b = True
c = True

if a:
    print("1")
elif b:
    print("2")
elif c:
    print("3")
else:
    print("4")
```

---

# Part 2: Code Challenges

## Problem 1: Most Clocks Are Normal, But Some Are Cuckoo!

### Skill you're practicing: Writing conditionals.

For this problem, put your solution into a file called `problem1.py`.

You're making a program for your coworkers that displays a message on their desktop's idle screen. Depending on the time of day, you want to print a different quote. You'll create a variable, `time`, which has an integer value between zero and 23, representing the hour of the day in [military time](https://www.thebalancecareers.com/military-time-3356971), which is a 24-hour clock. Write a conditional statement with Python code that prints exactly one message using the following rules:

```
If the time of day is before 9 a.m. --> print the quote "Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day."

Otherwise if the time of day is before or exactly 4 p.m. --> print the quote "Working hard or hardly working?"

Otherwise, if the time of day is before 8 p.m. --> print the quote "How did it get so late so soon?"

Otherwise if the time of day is before 10 p.m. --> print the quote "A day without sunshine is like, you know, night."

Otherwise, for any time 10 p.m. or later --> print the quote "Burning the midnight oil!"
```

#### Starter Code

```python
time = 8
```

> **Hint:** Test your code with different values for time of day. Make sure you are only printing one statement, regardless of the value of `time`!

---

## Problem 2: I Came, I 'Saur, I Conquered

### Skill you're practicing: Writing conditionals with multiple conditions.

For this problem, put your solution into a file called `problem2.py`.

The mighty Tyrannosaurus rex is the king of dinosaurs, and he does whatever he pleases. When he's hungry, he eats. When he's angry, he fights. When he's bored, he roars. When he's tired, he sleeps! Write a conditional statement that selects one of the following actions for T-Rex based on his current mood. T-Rex's actions are ordered by precedence:

```
If T-Rex is angry, hungry, and bored he will eat the Triceratops.
Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
Otherwise if T-Rex is tired, he goes to sleep.
Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
Otherwise if T-Rex is angry or bored, he roars.
Otherwise T-Rex gives a toothy smile.
```

#### Starter Code

```python
angry = True
bored = True
hungry = False
tired = False

# Example `if` statement:
if bored:
    print("T-Rex roars! Rawr!")
```

---

## All Done!

Now, go be like a T-Rex and do what you please!

![](https://media.giphy.com/media/1NFXnqVxzGr6w/giphy.gif)
