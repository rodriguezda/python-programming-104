<!--
title: Intro to Python Lists
type: lesson
duration: "00:30"
creator: Brandi Butler
Private gist location: https://gist.github.com/brandiw/621c35f1987e5ab680e7de7b05dfe039
Presentation URL: https://presentations.generalassemb.ly/621c35f1987e5ab680e7de7b05dfe039#/
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Lists</h1>

<!--

## Overview
This lesson introduces students to the concept of lists. This begins as basic list operations - accessing elements, `len`, `insert`, `append`, and `pop`.  After an exercise to recap that, it segues into operations on numerical lists - `sum`, `min`, and `max`. It ends with a longer exercise recapping the list operations.

## Learning Objectives
In this lesson, students will:
- Create lists in Python.
- Print out specific elements in a list.
- Perform common list operations.

## Duration
30 minutes

### Notes on Timing

A 30 minute interval has been allotted for this lesson. You may finish up early due to the fact that this lesson doesn't get into loops or ranges. If you have extra time, put it on the activities or start the next lesson early so students do have buffer time later, when they need it.

That said, at the point you give this lesson, students are still on day one. They will require more time than you probably expect to poke around the code.

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:15 | Basic List Operations |
| 0:15 - 0:25 | Numerical List Operations |
| 0:25 - 0:30  | Summary |

## In Class: Materials
- Projector
- Internet connection
- Python3
-->

---

## Lesson Objectives
*After this lesson, you will be able to...*

- Create lists in Python.
- Print out specific elements in a list.
- Perform common list operations.

---

## What is a List?

Variables hold one item.

```python
my_color = "red"
my_peer = "Brandi"
```

**Lists** hold multiple items - and lists can hold anything.

```python
# Declaring lists
colors = ["red", "yellow", "green"]
my_class = ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha"]

# Strings
colors = ["red", "yellow", "green"]

# Numbers
my_nums = [4, 7, 9, 1, 4]

# Both!
my_nums = ["red", 7, "yellow", 1, 4]
```

<aside class="notes">

**Teaching Tips**:

- After explaining what a list is, walk through the syntax (dashes, commas).
- Point out anything  can be in a list - it's just  a  variable that holds many things.

**Talking Points**:

-  "Until now we've used a few different types of variables such as numbers and strings. However, what if we wanted to keep track of more than one thing? Instead of just my single favorite color, how can I store the names of all the colors I like? How can I store the numbers of everyone on my baseball team?

- "Python has this problem solved with something called a *List*."

- "Because a variable is just a box that can hold information, it can also hold lists. Python knows that your variable will hold a list if it begins and ends with square brackets"

- "A list is a data structure in Python, which is a fancy way of saying we can put data inside of it. In the same way you recognize strings by the quotation marks surround them, you can recognize lists by square brackets that surround them."

- "Notice in the example below, we have a list but there are strings inside of it. A list can store data of other types! In this case, I have a list of strings that stores my classmates names."

</aside>


---


## Accessing Elements


**List Index** means the location of something (an *element*) in the list.

List indexes start counting at 0!

|  List | "Brandi" | "Zoe" | "Steve" | "Aleksander" | "Dasha" |
|:-----:|:--------:|:-----:|:-------:|:------:|:------:|
| Index |     0    |   1   |    2    |    3   |    4   |

```python
my_class = ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha"]
print(my_class[0]) # Prints "Brandi"
print(my_class[1]) # Prints "Zoe"
print(my_class[4]) # Prints "Dasha"
```

<aside class="notes">

**Teaching Tips**:

- Starting at 0 is easy to understand and hard to remember. Remind them throughout the presentation.
- Point out the print syntax.

**Talking Points**:

- "A very important thing to note about lists is that they start counting at 0. Thus, the first element is considered index 0, the second element is considered index 1, and so on."

- "In our previous example, let's print a few specific items. We can access an item by counting from 0 and using square brackets to tell the list which item we want."


</aside>

---

## We Do: Lists

1. Create a **list** with the names `"Holly"`, `"Juan"`, and `"Ming"`.
2. Print the third name.
3. Create a **list** with the numbers `2`,`4`, `6`, and `8`.
4. Print the first number.

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/blank-repl?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

1 MINUTE

**Teaching Tips**:

- Run through this quickly - this is just to show them lists working get them practicing typing lists. This is not  mean to be a full fledged exercise.

**Repl.it Note**
It's blank.


</aside>


---

## List Operations - Length


`len()`:

- A built in `list` operation.
- How long is the list?

```python
# length_variable = len(your_list)

my_class = ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha"]
num_students = len(my_class)
print("There are", num_students, "students in the class")
# => 5
```

<aside class="notes">

**Teaching Tips:**

- Stress that even though all examples are strings, these can be performed on any list, no matter what's in it.

**Talking Points**:

- "How many people are in my list? Just as with strings, we can determine how long a list is (i.e., how many elements it has) using the len() method like so."

- "Note: We'll get more into functions later. For now, just know that they perform some operation for you and that you can recognize them by the parentheses on the end."

</aside>

---

## Adding Elements: Append

`.append()`:

- A built in `list` operation.
- Adds to the end of the list.
- Takes any element.

```python
# your_list.append(item)

my_class = ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha"]
my_class.append("Sonyl")
print(my_class)
# => ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha", "Sonyl"]
```


<aside class="notes">

**Talking Points**:

- "Forgot to add something to that list? No problem; you can use the .append() method. Suppose a new student joins our class. We can add them to the end of the list with `append`, which is a function built directly into a list. (Notice it is called with a dot after the list, unlike the other function we've used, `len`)"

</aside>

---

## Adding Elements: Insert

`.insert()`:

- A built in `list` operation.
- Adds to any point in the list
- Takes any element and an index.

```python
# your_list.insert(index, item)

my_class = ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha", "Sonyl"]
my_class.insert(1, "Sanju")
print(my_class)
# => ["Brandi", "Sanju", "Zoe", "Steve", "Aleksander", "Dasha", "Sonyl"]
```

<aside class="notes">

**Talking Points**:

- "However, what happens if we want to add something somewhere else? We can use the .insert() method, which specifies where (i.e., to which index) we want to add the element."

</aside>

---

## Removing elements - Pop


`.pop()`:

- A built in `list` operation.
- Removes an item from the end of the list.

```python
# your_list.pop()

my_class = ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha", "Sonyl"]
student_that_left = my_class.pop()
print("The student", student_that_left, "has left the class.")
# => "Sonyl"
print(my_class)
# => ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha"]
```


<aside class="notes">

**Talking Points**:

- "What if someone leaves our class? We need to remove them from the list."

- "We can do this with `pop`. Pop drops the last thing off the list. It gives us back the value that it removed. We can take that value and assign it to a new variable, `student that left`. This is called a `return value`."

</aside>


---

## Removing elements - Pop(index)

`.pop(index)`:

- A built in `list` operation.
- Removes an item from the list.
- Can take an index.

```python
# your_list.pop(index)

my_class = ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha", "Sonyl"]
student_that_left = my_class.pop(2) # Remember to count from 0!
print("The student", student_that_left, "has left the class.")
# => "Steve"
print(my_class)
# => ["Brandi", "Zoe", "Aleksander", "Dasha", "Sonyl"]
```


<aside class="notes">

**Talking Points**:

- "What if someone specific leaves the class?"

- "We can do this with `pop` again. Here, we can give pop the index we want removed. It gives us back the value that it removed. We can take that value and assign it to a new variable, `student that left`."

</aside>

---

## Partner Exercise: Pop, Insert, and Append


Partner up! Choose one person to be the driver and one to be the navigator, and see if you can do the prompts:

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-lists-intro?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

**Teaching Tips**:

3 MINUTES

- Try to get them in pairs they haven't worked in before.
-  Give them just small bit of time to work through this, then go over the answer.

**Repl.it Note:** This replit has:
```
# 1. Declare a list with the names of your classmates
# 2. Print out the length of that list
# 3. Print the 3rd name on the list
# 4. Delete the first name on the list
# 5. Re-add the name you deleted to the end of the list
```

</aside>


---

## Pop, Insert, Append Solution

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-lists-intro-solution?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

**Repl.it Note**: This replit has:

# 1. Declare a list with the names of your classmates

my_class = ["Brandi", "Zoe", "Steve", "Aleksander", "Dasha", "Sonyl"]

# 2. Print out the length of that list
print(len(my_class))

# 3. Print the 3rd name on the list
print(my_class[2])

# 4. Delete the first name on the list
deleted_classmate = my_class.pop(0)

# 5. Re-add the name you deleted to the end of the list
my_class.append(deleted_classmate)

print(my_class)


</aside>

---

## !! List Mutation: Warning !!

This won't work as expected - don't do this!

```python
colors = ["red", "yellow", "green"]
print colors.append("blue")
#	=> None
```

This will work - do this!

```python
colors = ["red", "yellow", "green"]
colors.append("blue")
print colors
#	=> ["red", "yellow", "green", "blue"]
```

<aside class="notes">

**Teaching Tips**:

- Talk about why this happens, especially in case a student accidentally does it.

**Talking Points**:

- "All of the methods above mutate, i.e., change the array in place; they don't give you the mutated, or changed, array back."

</aside>

---

## Quick Review: Basic List Operations

```python
# List Creation
my_list = ["red", 7, "yellow", 1]

# List Length
list_length = len(my_list) # 4

# List Index
print(my_list[0]) # red

# List Append
my_list.append("Yi") # ["red", 7, "yellow", 1, "Yi"]

# List Insert at Index
my_list.insert(1, "Sanju") # ["red", "Sanju", 7, "yellow", 1, "Yi"]

# List Delete
student_that_left = my_list.pop() # "Yi"; ["red", "Sanju", 7, "yellow", 1]

# List Delete at Index
student_that_left = my_list.pop(2) # 7; ["red", "Sanju", "yellow", 1]
```

<aside class="notes">

**Teaching Tips**:

- Quickly review. Check to see if anyone's stuck.
- Remind them that these operations work on lists with both strings and numbers.

</aside>

---


## Numerical List Operations - Sum

Some actions can only be performed on lists with numbers.

`sum()`:

- A built in `list` operation.
- Adds the list together.
- Only works on lists with numbers!

```python
# sum(your_numeric_list)

team_batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
sum_avgs = sum(team_batting_avgs)
print("The total of all the batting averages is", sum_avgs)
# => 2.409
```

<aside class="notes">

**Teaching Tips**:

- If baseball's not your thing, feel free to change this.
- Stress that these only work on lists with entirely numerical values.
- You might need to explain batting averages.
- Consider demoing trying to sum string numbers.

**Talking Points**:

- "There's another built-in function, `sum`, used to add a list of numbers together."

</aside>

---

## List Operations - Max/Min


`max()` or `min()`:

- Built in `list` operations.
- Finds highest, or lowest, in the list.

```python
# max(your_numeric_list)
# min(your_numeric_list)

team_batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
print("The highest batting average is", max(team_batting_avgs))
# => 0.328
print("The lowest batting average is", min(team_batting_avgs))
# => 0.208
```

<aside class="notes">

**Talking Points**:

- "We might want to simply know what is the largest or smallest item in a list. In this case, we can use the built-in functions `max` and `min`."

</aside>

---

## You Do: Lists


On your local computer, create a `.py` file named `list_practice.py`. In it:

1. Save a list with the numbers `2`, `4`, `6`, and `8` into a variable called `numbers`.
2. Print the max of `numbers`.
3. Pop the last element in `numbers` off; re-insert it at index `2`.
4. Pop the second number in `numbers` off.
5. Append `3` to `numbers`.
6. Print out the average number (divide the sum of `numbers` by the length).
7. Print `numbers`.

<aside class="notes">

**Teaching Tips**:

- Have students run through this exercise on their own. Circulate the room to check questions and challenges.
- Students might pop off index 2 versus the actual 2nd element - remind them to watch out for that.

- Answer that's printed:
Max: 8
Average: 4.75
Final list: [2 8 6 3]

</aside>

---

## Summary and Q&A

We accomplished quite a bit!

```python
# List Creation
my_list = ["red", 7, "yellow", 1]
# List Length
list_length = len(my_list) # 4
# List Index
print(my_list[0]) # red
# List Append
my_list.append("Yi") # ["red", 7, "yellow", 1, "Yi"]
# List Insert at Index
my_list.insert(1, "Sanju") # ["red", "Sanju", 7, "yellow", 1, "Yi"]
# List Delete
student_that_left = my_list.pop() # "Yi"; ["red", "Sanju", 7, "yellow", 1]
# List Delete at Index
student_that_left = my_list.pop(2) # 7; ["red", "Sanju", "yellow", 1]
```

<aside class="notes">

**Teaching Tips**:

- Quickly sum up and check for understanding.
- Reassure students that while this is a lot, the more they practice typing it, the more they'll get used to it. If  they always copy the code off the slide, they won't be very quick to learn it!

</aside>

---

## Summary and Q&A

And for numerical lists only...

```python
# Sum all numbers in list
sum_avgs = sum(team_batting_avgs)
# Find minimum value of list
min(team_batting_avgs)
# Find maximum value of list
max(team_batting_avgs)
```

<aside class="notes">

**Teaching Tips**:

- Quickly sum up and check for understanding.

</aside>

---

## Additional Resources

- [Python Lists - Khan Academy Video](https://www.youtube.com/watch?v=zEyEC34MY1A)
- [Google For Education: Python Lists](https://developers.google.com/edu/python/lists)
- [Python-Lists](https://www.tutorialspoint.com/python/python_lists.htm)

<aside class="notes">

**Teaching Tips:**

- Encourage students to go through these in their spare time, especially if they're a bit lost.

</aside>
