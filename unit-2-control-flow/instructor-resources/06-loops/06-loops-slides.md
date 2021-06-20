<!--
title: Python Programming: Loops
type: lesson
duration: "01:00"
creator: Susi Remondi
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Loops</h1>


<!--

## Overview
This lesson introduces students to the concept of creating `for` and `while` loops. It begins with `for`, covering lists and strings, then goes into using  `range` to modify a list. It then dives into `while` loops.

## Learning Objectives
In this lesson, students will:
- Use a `for` loop to iterate a list.
- Use `range()` to dynamically generate loops.
- Use a `while` loop to control program flow.

## Duration
60 minutes

### Note on timing:
Loops are crucial to programming. If students are struggling, extend the amount of time here. You can generate exercises by  giving sample scenarios. Fizzbuzz is a great problem to give them, if you have time!


## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:00 - 0:33 | `For` Loops |
| 0:33 - 0:50 | `While` Loops |
| 0:50 - 1:00 | Summary |

## In Class: Materials
- Projector
- Internet connection
- Python3
-->


---

## Learning Objectives
*After this lesson, you will be able to:*

- Use a `for` loop to iterate a list.
- Use `range()` to dynamically generate loops.
- Use a `while` loop to control program flow.
- Use `break` to exit a loop.

<aside class="notes">

**Teaching Tips**:

- Briefly overview today’s learning objectives.

</aside>

---

## Discussion: A Small List


This situation isn't so bad:

```python
visible_colors = ["red", "orange", "yellow", "green", "blue", "violet"]
print(visible_colors[0])
print(visible_colors[1])
print(visible_colors[2])
print(visible_colors[3])
print(visible_colors[4])
print(visible_colors[5])
```

But what would we do if there were 1,000 items in the list to print?

<aside class="notes">

**Teaching Tips**:

- Try to get students to guess at the idea of putting the print statement in a loop.

**Talking Points**:

- "But, what if we had a list with 283,000 items in it? We can't write one line for each element. We need a way to write the `print` statement once and have it run for every element in the list."

- "One of the most powerful things that programming can do for you is automatically perform repetitive tasks.
In the tiny scripts we've been writing, printing out every variable has not been much of an issue. But with lists in the game now, things can get a bit more challenging. We need a way to automate some tasks so that they repeat for every item in a list."

</aside>

---

## The `for` Loop

<!--

**Talking Points**:
"A common and extremely useful type of loop is the `for` loop. `for` loops appear in several computer programming languages and get their name from the fact that they loop (or iterate) **for** a specific number of times: once **for** each item in a list."

"The `for` loop is perfect for when you have a specific collection of items — each of which must be processed once — or for when you know that you must execute a set of instructions a specific number of times. Those are the use cases for which it was designed."

"This is our template. When we write a `for` loop we do the following:
* We replace `item` with a meaningful name for the items in the collection.
  * We use this name as the name of the item within our loop.
* We replace `collection` with the name of our list (or other collection).
* Indented inside the loop, we write the code to be run for each item.
* Python will start with the first item and automatically stop after it loops with the last item."
-->

The `for` loop always follows this form:

```python
for item in collection:
  # Do something with item
```

For example:

```python
visible_colors = ["red", "orange", "yellow", "green", "blue", "violet"]

for each_color in visible_colors:
  print(each_color)
```


<aside class="notes">

**Teaching Tips**:

- Go over the syntax.  Point out the indentation - point out that it's like the `if` statement they learned.

**Talking Points**:

- "We need what is called a `Loop`."

- "A common and extremely useful type of loop is the `for` loop. `for` loops appear in several computer programming languages and get their name from the fact that they loop (or iterate) **for** a specific number of times: once **for** each item in a list."

This code:
* Creates a new list containing some name strings.
* Begins the `for` loop. We loop once for each "name" in the list (`names`).
* Prints the current name inside the loop."

- "The `for` loop is perfect for when you have a specific collection of items — each of which must be processed once — or for when you know that you must execute a set of instructions a specific number of times. Those are the use cases for which it was designed."

- "This is our template. When we write a `for` loop we do the following:
* We replace `item` with a meaningful name for the items in the collection.
  * We use this name as the name of the item within our loop.
* We replace `collection` with the name of our list (or other collection).
* Indented inside the loop, we write the code to be run for each item.
* Python will start with the first item and automatically stop after it loops with the last item."

</aside>

---


## Knowledge Check: What will this code do?


Think about what the code will do before you actually run it.

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-for-indents?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

**Talking Points**:

- "The statements inside a loop that you want to repeat must be indented like the statements inside an `if` block. So, if you have three lines of code that you want to execute on each loop iteration, each must be indented one level underneath your `for` line."

- "Each name is met with `"THUNDEROUS APPLAUSE!"` because that line, and the two above it, are indented to be in
the body of the `for` loop."

**Repl.it Note**: This replit has:

```python
for name in ["Tom", "Deborah", "Murray", "Axel"]:
  print("Now appearing in the Refreshment Room...")  # in the loop
  print(name)                                        # in the loop
print("THUNDEROUS APPLAUSE!")                      # OUTSIDE the loop
```

</aside>

---

## We Do: Writing a Loop

Let's write a loop to print names of guests.

First, we need a list.

- Create a local `.py` file named `my_loop.py`.

- Make your list: Declare a variable `my_list` and assign it to a list containing the names of at least five people.

<aside class="notes">

**Teaching Tips**:

- Do this with them! Make sure they're typing with you, to practice. See if they can give you the syntax you should write.

**The code is**:

```python
guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]

```

</aside>

---

## We Do: Write a Loop - Making the Loop


Now, we'll add the loop.

- Skip a line and write the first line of your `for` loop.
    - For the variable that holds each item, give it a name that reflects what the item is (e.g. `name` or `person`).
- Inside your loop, add the code to print `"Hello,"` plus the name.

```
"Hello, Felicia!"
"Hello, Srinivas!"
```


<aside class="notes">

**Teaching Tips**:

- Do this with them! Make sure they're typing with you, to practice. See if they can give you the syntax you should write.

**Talking Points**:

- Remind them that the word collection is a list; this collection is the list variable they have.

**The code is**:

```python
guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]

for guest in guest_list:
  # Print out a greeting in here
  print("Hello, " + guest + "!")
```

</aside>

---

## We Do: Write a loop to greet people on your guest list

Our guests are definitely VIPs! Let's give them a lavish two-line greeting.

- Inside your loop, add the code to print another sentence of greeting:

```
"Hello, Srinivas!"
"Welcome to the party!"
```


<aside class="notes">

**Teaching Tips**:

- Do this with them! Make sure they're typing with you, to practice. See if they can give you the syntax you should write.
- Point out the indent.

**The code is**:

**Talking Points**:

- "Fantastic! Now each guest is greeted by their name and welcomed to the party. Those two `print()` lines are executed on every iteration because both are indented to be in the `for` loop's code block. Think of the indented block as a unit of instructions executed as a group each time the loop runs."

```python
guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]

for guest in guest_list:
  # Print out a greeting in here
  print("Hello, " + guest + "!")
  print("Welcome to the party!")
```

</aside>

---

## Discussion: Where Else Could We Use a Loop?


A loop prints everything in a collection of items.

- `guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]`

What, besides a list, could we use a loop on?

*Hint: There are six on this slide!*

<aside class="notes">

**Teaching Tips**:

- The answer is a string! We can loop through the characters.

</aside>


---

## Looping Strings

Loops are collections of strings and numbers.

Strings are collections of characters!

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-string-for?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

**Teaching Tips**:

- Don't spend more than a minute or two on this slide - it's not  an exercise; just a demonstration.
- The point is to understand that  a string is a collection of characters, and any collection can be looped.

**Talking Points**:

- "You may not realize it, but a string is a collection of characters. Just so you can see that a for loop has the same syntax for any collection, let's add the following code below what we've just written"

**Repl.it Note:**: This code has:

```python
my_string = "Hello, world!"

for character in my_string:
  print(character)
```

</aside>

---

## What about...Looping For a Specific Number of Iterations?


We have:
```python
guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]

for guest in guest_list:
  print("Hello, " + guest + "!")
```

The loop runs for every item in the list - the length of the collection. Here, it runs 6 times.

What if we don't know how long `guest_list` will be?

Or only want to loop some of it?

<aside class="notes">


**Talking Points**:

- "Whenever we have a collection, such as a list or string, and we want to iterate over each item it contains,
we should use a `for` loop. Python has internal logic for determining exactly how many times the loop should
run based on the length of the collection."

- "But, what if we want to do something in a loop a specific number of times, but we don't have a collection to start with? Maybe we are initializing a new collection and we need to add a specific number of items to it or maybe we just want something to run exactly 15 times. In this case, we can have the `for` loop iterate over a range of numbers."


</aside>
---

## Enter: Range


`range(x)`:

- Automatically generated.
- A list that contains only integers.
- Starts at zero.
- Stops before the number you input.

```python
range(5)  # => [0, 1, 2, 3, 4]
```

<aside class="notes">

**Talking Points**:

- "You can actually feed more parameters into `range()` to control what number it starts at and how big each step is to the next number, but we will keep it simple for now. For now it is enough to know that if you loop over `range(5)` then your loop will execute **five** times. Let's use this in a loop..."

</aside>

---

## Looping Over a Range

Let's look at `range` in action:

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-for-range?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">


**Teaching Tips**:

-  This isn't an exercise, just  a quick demo. Make sure they understand how range is working.

**Talking Points**:

- "We can see that this code prints each of the numbers in our range of 0 through 9 (10 numbers total.) We don't need to have our loop print anything. This loop could be used to execute any sequence of code 10 times. "


**Repl.it Note:** This code is:
```python
for i in range(10):
  print(i)

squares = []

for num in range(5):
  sqr = num ** 2
  squares.append(sqr)

print(squares)
```
</aside>

---

## Looping Over a Range

Looping over `names` here is really just going through the loop 4 times -  at index `0`, `1`, `2`, and `3`.

We can instead use `range(x)` to track the index and  loop `names`: `range(4)` is `[0, 1, 2, 3]`.

We can then use `len(names)`, which is 4, as our range.

<iframe height="300px" width="100%" src="https://repl.it/@GAcoding/python-programming-range-loop?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">

**Teaching Tips**:

-  This isn't an exercise, just a demo. Make sure they understand how range is working. This  can be a bit tricky!
-  Show a  regular loop again, if you need to.
- Vary the size of range - try `range(4)`  and `range(2)` - so  students can see the differences.
- Give a bunch of examples. Range might make sense conceptually, but be hard to remember the syntax for and use.

**Talking Points**:

- "Recall that you can use the `len()` function to get the length of a list. Since that will always be an integer, we can feed that value into the `range()` function to generate a range that contains each index in the list."

- "Don't be alarmed about the function inside the function. That's fairly common. Let's break it down: `len(names)` will return the length of the `names` list; in this case, 4. The number 4 is then used as the parameter for `range()` creating a range containing 0, 1, 2, and 3. These happen to all be valid indices for our list so we can use them to modify the values stored at those indices."


**Repl.it Note:** This code is:
```python
names = ["Flint", "John Cho", "Billy Bones", "Nanda Yuna"]

for each_name in range(len(names)):
  print(names[each_name])
```
</aside>

---

## Range to Modify Collections

Why would you use `range` on a list, when you could just loop the list?

We can't do:

```python
guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]

for guest in guest_list:
  guest = "A new name"
```

But we can do:

```python
guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]

for guest in range(len(guest_list)):
  guest_list[guest] = "A new name"
```

<aside class="notes">

**Talking Points**:

- "But there is one special use for this that is vital to know about. When we loop using `for item in collection` we can't ever really **modify** the elements in the list. Whenever we access `item` we are actually getting a copy of the item in the list. In order to **modify** the item in the list, we would need the index of that item in the list. And guess what `range()` gives us..."

</aside>


---

## Looping Over a Range


Let's make the list all uppercase:

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-range-modification?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">

**Teaching Tips**:

- This is a bit difficult. Make sure they understand that range hits the index versus a regular for loop makes a copy.
- Give different examples if need be.


**Talking Points**:

- "Now when we run this we see that the `names` list has had all the string changed to uppercase. It is necessary to use list indices if you want to modify list elements. If we tried doing the same thing with an `item` from that `list` then the changes would only apply to the temporary copy stored in `item` and would never actually make it into the list."


**Repl.it Note:** This code is:
```python
# This won't work

guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]

for guest in guest_list:
  guest = guest.upper()

print("Without range, guest_list is", guest_list)

# This will!

for guest in range(len(guest_list)):
  guest_list[guest] = guest_list[guest].upper()

print("With range, guest_list is", guest_list)
```
</aside>


---

## Knowledge Check: Which of the following lines is correct?

```python
my_list = ['mon', 'tue', 'wed', 'thu', 'fri']
```
```python
for day in range(my_list):       # answer A
for day in range(len(my_list)):    # answer B
for day in range(my_list.length):  # answer C
```

<aside class="notes">

**Teaching Tips**:

- Give them time to discuss and come up with an answer!
- The answer is B

</aside>

---

## You Do: Range

Locally, create a new file called `range_practice.py`.

In it:

- Create a list of colors.
- Using a `for` loop, print out the list.
- Using `range`, set each item in the list to be the number of characters in the list.
- Print the list.

For example:
```python
["red", "green", "blue"]
# =>
[3, 5, 4]
```


<aside class="notes">

5-10 minutes

**Teaching Tips**:

- If students seem a bit lost when you get here, run this as a partner exercise.

- This is tough! Give them a bit before going over the answer - bring up your own file or a repl.it and write it, talking through each step.

</aside>

---

## Quick Review: For Loops and Range


`for` loops:

```python
# On a list (a collection of strings)
guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]
for guest in guest_list:
  print("Hello, " + guest + "!")

# On a string (a collection of characters)
my_string = "Hello, world!"
for character in my_string:
  print(character)

##### Range #####

range(4)  # => [0, 1, 2, 3]

# Using Range as an Index Counter
names = ["Flint", "John Cho", "Billy Bones", "Nanda Yuna"]
for each_name in range(4):
  print(names[each_name])

# OR

for each_name in range(len(names)):
  print(names[each_name])

# Using Range to Change a List:

guest_list = ["Fred", "Cho", "Brandi", "Yuna", "Nanda", "Denise"]
for guest in range(len(guest_list)):
  guest_list[guest] = "A new name"
```


<aside class="notes">

**Teaching Tips**:

- Quickly review key takeaways.
- Ask if there are questions. That was a lot!



</aside>

---

## The While Loop


What about "While the bread isn't brown, keep cooking"?

Python provides two loop types.

`for`:

- You just learned!
- Loops over collections a finite number of times.

`while`:

- You're about to learn!
- When your loop could run an indeterminate number of times.
- Checks if something is `True` *(the bread isn't brown yet)* and runs until it's set to `False` *(now the bread is brown, so stop)*.

<aside class="notes">

**Talking Points**:

- “Now that we’ve learned how to write for loops to to iterate lists, and how to use range to dynamically generate loops, we’re going to transition to while loops. I’m going to show you how to write while loops, and then you’re going to practice while loops with your partner.”

</aside>

---

## While Loop Syntax

```python
# While <something> is true:
#     Run some code
#     If you're done, set the <something> to false
#     Otherwise, repeat.

a = 0
while a < 10:
  print(a)
  a += 1
```

![](https://upload.wikimedia.org/wikipedia/commons/4/43/While-loop-diagram.svg)


<aside class="notes">

**Teaching Tips**:

- Call out that it won't print 10.
- Call out the indents!

**Talking Points**:

- "We won't always have the luxury of a collection of discrete data items for controlling our loop. Frequently, we will need to write a loop that will run an unknown number of times. This is what the `while` loop is for. It's
another loop construct that will continue to iterate __while a given condition is true__. These loops are quite
useful for data sets of unknown sizes, or for when we need to loop until some value changes."
- "Outside of our `while` loop, we create the variable `a`, which we'll use as our conditional. We then start our loop. We say to loop "while `a` is less than 10." Then, in the loop, we print `a` and add one to its value.
Once the value of `a` reaches 10, the loop condition evaluates to false and the loop finishes."
</aside>

---

## While Loop: Be Careful!


Don't *ever* do:
```python
a = 0
while a < 10:
  print(a)
```

And don't ever do:

```python
a = 0
while a < 10:
  print(a)
a += 1
```

Your program will run forever!

If your program ever doesn't leave a loop, hit `control-c`.

<aside class="notes">

**Teaching Tips**:

- We're telling them this in advance of practicing, in  case they do it!
- Make it clear why this runs forever.


**Talking Points**:

- "`While` loops present a potential "gotcha" in programming: the infinite loop. Because the `while` loop only terminates when a condition turns to false, it's possible to write the loop in such a way that it never terminates. This creates a serious bug in your code where the loop never, ever returns control to the app, and it will freeze indefinitely. The way to avoid this is to __always__ remember to update your conditional variable inside your loop block."


</aside>

---

## We Do: Filling a Glass of Water

Create a new local file, `practicing_while.py`.

In it, we'll create:

- A variable for our current glass content.
- Another variable for the total capacity of the glass.

Let's start with this:

```python
glass = 0
glass_capacity = 12
```

Can you start the `while` loop?

<aside class="notes">

**Teaching Tips**:

- Make sure they're typing this with you and not just copying and pasting the code.
- Before you go to the next slide (adding the loop), see if they can guess the syntax.

**Talking Points**:

- "Can you think of the mental process you follow when pouring water into a glass? You start with an empty
glass and begin adding water to it, right? While you are adding the water, you must constantly check
to see if the glass has reached its maximum capacity. If it has, you then stop pouring.
Otherwise, you continue adding water. Let's see how that would work as a `while` loop..."

- "We a variable for our current glass content and we need one for the total capacity of the glass."

- "What we want to do is add water to the glass one unit at a time until the glass reaches capacity. Said another way, **while** the glass contains less than its capacity, add another unit of water. Can you start the loop code before we move to the next slide?"

</aside>

---

## We Do: Filling a Glass of Water


Add the loop:

```python
glass = 0
glass_capacity = 12

while glass < glass_capacity:
  glass += 1  # Here is where we add more water
```

That's it!

<aside class="notes">

**Talking Points**:

- "We declare our `glass` variable and set it to `0` water, currently. Then, we declare our glass' capacity and
set it to `12` units. Next, we set up our `while` loop. We want to loop while the glass has a value less than `glass_capacity`. Inside of our loop, we add `1` unit of water to our glass. Each time the loop runs, it checks the value of `glass` to see if it has reached the same value as `glass_capacity`. The loop stops once `glass` reaches `12`, conveniently before we spill."

</aside>

---


##  Side Note: Input()

Let's do something more fun.

With a partner, you will write a program that:

- Has a user guess a number.
- Runs until the user guesses.

But first, how do we have users input numbers?

Using `input()`.

```python
user_name = input("Please enter your name:")
# user_name now has what the user typed
print(user_name)
```

Erase the code in your `practicing_while.py` file and put the above. Run it! What happens? Does it work?


<aside class="notes">

**Teaching Tips**:

- Don't put them in partners yet - make sure they all have `input` working on  their own.
- Demo that the text in the `input` prompt can be anything, and the variable `user_name` can be named anything.
- There is a lesson teaching `input` in depth in unit 5, so you just need them to be able to use the code. Put any further questions into the parking lot.

**Talking Points**:

- "`While` loops are also great for guessing games. Let's use a small function called `input()` to get some
user input so that they can take guesses about our secret number. Here's how `input()` works."

- "Whatever string you put in the parentheses is printed to the screen. The user then has the opportunity to type something. The script will wait patiently for the user until something is typed and entered (a perfect example of a while loop in the Python internals.) When the user hits Enter, the string they typed is stored in the variable `user_name` above."

</aside>

---

## You Do: A Guessing Game

Now, get with a partner! Let's write the the game.

Decide who will be driver  and who will be navigator. Add this to your existing file.

- Set a variable, `answer` to `"5"` (yes, a string!).
- Prompt the user for a guess and save it in a new variable, `guess`.
- Create a `while` loop, ending when `guess` is equal to `answer`.
- In the `while` loop, prompt the user for a new `guess`.
- After the `while` loop, print "You did it!"

Discuss with your partner: Why do we need to make an initial variable before the loop?

<aside class="notes">

5 MINUTES

**Teaching Tips**:

- Run this as a partner exercise. Set student up in pairs, then walk around to be sure they're all working and no one is stuck.

**Talking Points**:

- "Now that you know how to accept input from the keyboard, make a game where the player must correctly guess a number. The game will continually prompt the user to enter a guess if they did not guess correctly. Once they correctly guess the number, the program congratulates them and exits. Can you think of how this would be written?"

- "You need a variable to hold the correct answer. You need another variable to hold each subsequent guess. We will need to compare the guess to the answer and if it is wrong, ask the user again for a guess. This sounds like we will be repeatedly asking for a guess **while** the previous guess was incorrect."

- "One thing to keep in mind is that `input()` returns a string so if the user types `5` it will result in the string `"5"`. You cannot compare numbers to strings in Python. To work around this for a number guessing game, set your correct answer variable to be the string of the number (e.g. "4" or "9") instead of the number itself. This way when you do your loop comparison, you'll be comparing the same types."

</aside>


---

## You Do: A Guessing Game (Solution)

```python
answer = "4"
guess = input("Guess what number I'm thinking of (1-10): ")
while guess != answer:
  guess = input("Nope, try again: ")
print("You got it!")
```

How'd you do? Questions?

<aside class="notes">

**Teaching Tips**:

- Walk through the  answer here. Show it working. Check for understanding.

</aside>

---

## Exiting a Loop

There are times when you may want to exit a loop before the final condition has been met. Perhaps the input from another part of the program has satisfied another, separate condition that makes the rest of the loop unnecessary. Enter the `break` statement.

```python

while True:

  if my_condition == 1:
      # my condition is met! No need to continue on
      break
  else my_condition == 0:
      my_condition = 1

  # note that this is within the scope of the while loop
  print('This doesn\'t get run if the break is triggered!')
```

---

## Continuing a Loop

There are times when you may want to to `continue` a loop _without running code beneath the `continue` statement_. The `continue` allows you to do just that! After the `continue` statement is triggered, the loop _continues the next iteration of the loop without executing any code beneath it on that iteration_.

```python
  number = 0
  for number in range(5):
      number = number + 1
      if number == 3:
          continue
          print('My number is currently 3')
      print(f'Number is {str(number)}')
  print('Out of loop')
```

Prints:

```python
  Number is 1
  Number is 2
  Number is 4
  Number is 5
  Out of loop
```

---

## Passing within a Loop

The `pass` statement is like a placebo in a loop: it allows a loop to execute without any interruption. This example may seem odd, and we'll cover the more common use case in the next example.

```python
  number = 0
  for number in range(5):
      number = number + 1
      if number == 3:
          pass
          print('My number is currently 3')
      print(f'Number is {str(number)}')
  print('Out of loop')
```

Prints:

```python
  Number is 1
  Number is 2
  My number is currently 3
  Number is 3
  Number is 4
  Number is 5
  Out of loop
```

---

## Passing within a Function or Class

The most common use case for `pass` is to act as a placeholder for a function that has yet to be written. Developers will often do this if they're creating the architecture for a program but haven't gotten to actually building the logic yet.

```python
  def my_empty_function():
      pass
```

What happens if we _don't_ put the `pass` statement in the code and attempt to execute the function definition?

<aside class="notes">

**Teaching Tip**:

- The students should be able to guess that without `pass`, execution  will not proceed properly, resulting in our architectural scaffold breaking.

</aside>

---

## Throwing Exceptions within a Function or Class

Note that the previous example will allow the function to be called, but the function won't do anything. If the programmer wishes to alert the user, they may also use `raise` to interrupt the program execution. The following is common to see in larger applications that are in the process of being built by a dev team:

```python
  def my_empty_function():
      raise NotImplementedError
```

What happens when we call this function? _Hint: look at the type of  error that is returned!_

<aside class="notes">

**Talking Point**:

- The `raise` statement will halt the program and verbosely tell the programmer that the function is not implemented!  

</aside>

---

## Summary + Q&A

Loops:

- Common, powerful control structures that let us efficiently deal with repetitive tasks.

`for` loops:

- Used to iterate a set number of times over a collection (e.g. list, string, or using `range`).
- `range` use indices, not duplicates, so it lets you modify the collection.

`while` loops:

- Run until a condition is false.
- Used when you don't know how many times you need to iterate.

That was a tough lesson! Any questions?

<aside class="notes">

**Teaching Tips**:

- Briefly recap.
- Check for understanding! Bring up an interpreter if needed,  or if you have extra time. The  more they see this, the better!
- Then, go over next steps.
- Encourage students to check out all the additional resources at the end of each presentation.

</aside>

---

## Additional Reading

- [Learn Python Programming: Loops Video](https://www.youtube.com/watch?v=JkQ0Xeg8LRI)
- [Python: For Loop](https://wiki.python.org/moin/ForLoop)
- [Python: Loops](https://www.tutorialspoint.com/python/python_loops.htm)

<aside class="notes">

**Teaching Tips**:

- Encourage students to go through these in their spare time, especially if they need more help.

</aside>
