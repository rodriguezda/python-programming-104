### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Brandi

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack at @brandib.
--->

# Python Classes and Data Structures: Practice Problems + Reading

In this homework, you're going to write code for two challenge problems.

You'll practice these programming concepts we've covered in class:

* Using dictionaries to solve problems.
* Storing data in tuples and sets.

---

## Deliverables

Part of this homework will be code challenges and part of it will be some reading with comprehension questions.

For each of the code challenges listed below, you will create a new `.py` file and write code to solve the problem. For example, you would create `problem1.py` with your solution code to the first problem. Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following:*

```python
python problem1.py
```

> **Hint:** Make sure you are printing something out with the `print` statement. Otherwise, you won't see any output from running your program!


## Requirements:

By the end of this, you should have:
* Two different `.py` files (one for each code challenge).

---

# Code Challenges

## Problem 1: I Love You, Tuple

### Skill you're practicing: Using tuples.

You may recall tuples from your in-class lesson. Tuples are *immutable* data structures, which means they can't be changed after they're created. They are typically used to store related information that doesn't need to be changed, such as a student record or, in this case, some stats about a movie. It's your job to create some `print` statements that access the appropriate values inside each tuple to produce the expected output.


#### Starter Code

```python
# My favorite romance movies
# title, release year, runtime, tagline, main characters
romantic_movie1 = ("The Princess Bride", 1987, 98, "The story of a man and a woman who lived happily ever after.", ["Buttercup", "Westley", "Fezzik", "Inigo Montoya", "Vizzini"])
romantic_movie2 = ("Groundhog Day", 1993, 101, "He's having the day of his life… over and over again.", ["Phil Connors"])
romantic_movie3 = ("Amélie", 2001, 122, "One person can change your life forever.", ["Amélie Poulain", "Nino Quincampoix", "The Garden Gnome"])
```

#### Expected Output

```
Here are my favorite romance movies:

The Princess Bride (1987): The story of a man and a woman who lived happily ever after.

Groundhog Day (1993): He's having the day of his life...over and over again.

Amélie (2001): One person can change your life forever.
```

**Hint:** Remember, you can access a tuple sort of like a list, with the square brackets `[]` counting from zero (e.g., the value of `romantic_movie1[0]` is `"The Princess Bride"`).

### Bonus:
Change the `print` statement's separator character to an empty string `""` instead of a space so that you can print the year as `(1987)` instead of `( 1987 )`.

---

## Problem 2: Friends, Colleagues, and Details

### Skill you're practicing: Using dictionaries, lists, and key-value pairs.

Your boss tasks you with creating a company directory. Make a list called `employees`, which will contain one dictionary per person and include the keys `name`, `age`, `department`, `phone`, and `salary`. Once you have the list of dictionaries set up, loop through the list and print out the `name`, `department`, and `phone` number of each employee. Their `age` and `salary` should remain secret!

#### Starter Code

A dictionary should be set up in the following way:

```python
{
    "name": "Ron Swanson",
    "age": 55,
    "department": "Management",
    "phone": "555-1234",
    "salary": "$87,000"
}
```

#### Expected Output

```
Ron Swanson in Management can be reached at 555-1234.
Leslie Knope in Middle Management can be reached at 555-4321.
Andy Dwyer in Shoe Shining can be reached at 555-1122.
April Ludgate in Administration can be reached at 555-3345.
```

**Hint:** Dictionaries have values that can be accessed with keys, for example, `employees["name"]`. Keys are typically strings.

---

## Celebrate!

You're all finished!

![](https://media.giphy.com/media/UkhHIZ37IDRGo/giphy.gif)
