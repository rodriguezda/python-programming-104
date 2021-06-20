<!--
title: Python Programming: Variables
type: lesson
duration: "01:00"
creator: Brandi Butler
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Variables</h1>
<!--

## Overview
This lesson introduces students to the concept of creating and assigning variables - numeric variables (including basic math functions / numerical operators) and string variables (including concatenation). There is a small section near the end on different ways to print these variables.

## Important Notes or Prerequisites
- At the point you give this lesson, students are getting their very first introduction to writing code. Don't assume they know anything! Be sure and explain carefully whenever you change even a little thing.
- Encourage students to type, not copy and paste, for practice. Whenever possible, have students try and guess what will happen and try it out in the slide.
- Note: If the code is too long for students to easily see in the embedded slide, there's an "open with repl.it" icon in the top right of the embed that will open the repl.it in a new, larger window.

## Learning Objectives
In this lesson, students will:
- Define “variable”.
- Use numerical and mathematical operators.
- Use string variables.
- Print complex variable structures.

## Duration
60 minutes

### Notes on Timing

- A full hour has been allotted for this lesson because it is the first opportunity to let students get into writing code - so make sure to give them plenty of time to poke around in the repls!

### Use the Parking Lot!

- While we have dedicated a whole hour to this lesson, a lot of the content pieces in this lesson are easy segues into other topics. Don't forget about the parking lot mentioned in the Cookbook!

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 02:00 | Welcome |
| 02:00 - 05:00 | Variables in Python |
| 05:00 - 30:00 | Numerical Variables + Mathematical Operators |
| 30:00 - 40:00 | Break |
| 40:00 - 60:00 | String Variables |
| 60:00 - 65:00 | Printing Complex Variables |
| 65:00 - 75:00 | Q&A + Close |

## Before Class: Preparation
- Modify the slides and exercises in this file as you see fit.

## In Class: Materials
- Projector
- Internet connection
-->

---

## Lesson Objectives
*After this lesson, you will be able to...*

* Create and re-assign numerical and string variables.
* Use numerical operators.
* Print complex variable structures.

<aside class="notes">
**Talking Points**:
"We’re so excited to have to you here today."

Talk over the general agenda:
- Define “variable.”
- Use numerical and mathematical operators.
- Use string variables.
- Print complex variable structures.
- Q&A and transition.

**Teaching Tips**:

- Write the objectives on the board to reference as you go through the presentation.
</aside>

---

## What's a Variable?

Turn to the person next to you, and together come up with as many definitions for the word "variable" as you can.

- Consider contexts such as mathematics, the sciences, weather, etc.
- No cheating! Phones off and laptops closed.

<aside class="notes">
3 MINUTES

**Teaching Tips**:

- Facilitate a “Turn and Talk”:
  - Ask students to pair up
  - Each group should brainstorm as many definitions for the word “variable” as they can think of.
  - They’re not allowed to use dictionaries on their phones or laptops.
  - Allow 3 minutes for pairs to brainstorm.
  - Debrief the activity.
  - Ask a few pairs to share their definitions.
  - Ask what is common across the different definitions.
- Encourage a discussion to see if students can come up with something resembling the idea of variables, or Python saving information for them.

**Talking Points**:

- As you noticed, all of these different definitions of variables share one thing in common: they all have something to do with change.
- Today, we are going to explore how variables are used in Python.

</aside>

---

## Variable


Variables:

- Are boxes that can hold all kinds of information for you.
- Make it easier to store and re-use values.
- Are the most basic piece of code.

To use a variable, we simply announce that we want to use it (we **declare** it).

```python
# I've eaten 3 cupcakes
cupcakes_ive_eaten = 3
print(cupcakes_ive_eaten)
# Prints 3
```

<aside class="notes">

**Teaching Tips**:

- Bring up a repl.it (they haven't seen an interpreter yet!) and run this. It's already written in [here](https://repl.it/@GACoding/python-pt-cupcakes?lite=true).
- Point out the print statement and comments, as review of the prework.
- For variation, assign simple tasks like printing negatives and decimals.

**Talking Points**:

- While variables can really be anything, we’ll keep it simple to start by looking at numerical variables.
- Go over the syntax!
- "Here, we create a variable called `cupcakes_ive_eaten` and have it hold the number `3`. This is also called assignment. If we print out the contents of `cupcakes_ive_eaten`, Python will tell us that `cupcakes_ive_eaten` currently holds 3. When you create a variable, it's called declaring a variable. The syntax for declaring a variable is what you want the variable to be named, followed by an equal sign, and finally what you want the variable to hold. Notice the space before and after the equal sign! Also, note that in Python, the equal sign doesn't evaluate things the way it does in math. Instead, it assigns them values. Here, we're using the `=` to tell Python that the `cupcakes_ive_eaten` label is going to hold the value `3`."
- "See that underscore? We'll look at variable naming in a second!"

</aside>

---

## Naming Conventions: Mistakes and Syntax

Some common naming mistakes:

- Not using meaningful names. `delicious = 3` doesn't mean anything - `cupcakes_ive_eaten = 3` does!
- Case sensitivity (`CUPCAKES_IVE_EATEN` and `cupcakes_ive_eaten` are not the same!)
- No spaces or punctuation ("cupcakes i've eaten" isn't allowed)
  - This is invalid **syntax**
  - Use snake_case: `lowercase_letters_with_underscores` (it's in the official [Python style guide](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles))


<aside class="notes">
**Teaching Tips**:

- Bring up a replit - [this one](https://repl.it/@GACoding/python-pt-cupcakes?lite=true) already has the code. As you go through, demo each of these and show it breaking.
- Remind the students that if they make a typo, it will create a *new* variable!

**Talking Points**:

- "You can name a variable anything you'd like, but you probably shouldn't. If I called my variable "delicious", would you have any idea that the number it held was the number of cupcakes I've eaten? Probably not. In Python, we try to name variables as closely as we can to what it actually is. Technically, variable names can be almost anything, so it's up to us to be organized and thoughtful when we pick them!"
- "Any name is allowed - Python doesn't enforce helpfulness. Try to always have meaningful variable names so that later, you know what that variable holds!"
- "Variables are case sensitive.
- "When you want to use a variable name consisting of several words, you will get an error if you have spaces between the words. Try creating a variable called `my number` and you'll get an error; specifically, one that says "Invalid Syntax."

- "Syntax is the set of rules surrounding how a language looks. In the English language, we call syntax "grammar." For example, sentences always start with a capital letter and end with something such as a period, exclamation point, or question mark. Other languages have syntax, too, including programming languages like Python."

- "Here, Python is telling us that putting a space between two words in a variable name is invalid syntax. It's not proper grammar and it will not run."

</aside>

---

## Discussion: Changing Values

What if, later, you eat more cupcakes? Now, this is wrong.

```python
cupcakes_ive_eaten = 3
```

What do you think we need to do?


<aside class="notes">

**Teaching Tips**:

- Transition into the topic of reassigning variables. See if they can come up with the idea on their own.

</aside>

---

## Discussion: Reassigning Variables



In the example below, what do you think the output of the code is?

```python
cupcakes_ive_eaten = 3
print(cupcakes_ive_eaten)
cupcakes_ive_eaten = 4
print(cupcakes_ive_eaten)
```


<aside class="notes">

**Teaching Tips**:

- Bring up a repl.it and show this. [Here is one](https://repl.it/@GACoding/python-pt-cupcakes?lite=true) that has this code.
- Make it clear that only the last value is saved!

**Talking Points**:

- "We can always change what a variable is holding; it's just a container. Initially setting a variable to a value is known as assigning the variable. In our example above, we declared the `cupcakes_ive_eaten` variable and assigned it the value of `3`."
- "If we eat more cupcakes, we can *reassign* the variable to a different value - here, 4."
- "We can reassign our variable as many times as we want. However, only the most recent value of a variable will be retained. Once a variable is reassigned, its original value is lost forever. If you think of a box, reassigning a variable is like throwing away what's in the box and replacing it with something new."

</aside>

---

## Quick Review

- A variable is a box that holds a value.

- It can be declared, called, and changed within your program.

- When declaring variables, syntax and naming conventions matter!

- Variables can be reassigned as often as you like, but only the most recent declaration counts.

**UP NEXT:** Math!


<aside class="notes">

1 MINUTE

**Teaching Tips**
Quickly review what you covered so far.
Check for understanding

**Talking Points**
Now it’s time for everyone’s favorite subject -- math!

</aside>

---

## Mathematical Operators

Math works on numerical variables, too!

- The `+`, `-`, `*` (multiply), and `/` (divide) operators work just like they do with regular math.

```python
cupcakes_ive_eaten = 6 + 3
print(cupcakes_ive_eaten)
# Prints 9

cupcakes_ive_eaten = 6 - 3
print(cupcakes_ive_eaten)
# Prints 3

cupcakes_ive_eaten = 6 * 3
print(cupcakes_ive_eaten)
# Prints 18

cupcakes_ive_eaten = 6 / 3
print(cupcakes_ive_eaten)
# Prints 2
```


<aside class="notes">

**Talking Points**:

- "When we're dealing with variables that have numbers for values, the operators work just like they do with regular math."
- We can use pretty much any mathematical operator in Python to manipulate our variables and achieve our goals with our program. We’ve talked about addition, subtraction, multiplication and division so far.
- Note the syntax - the spaces around each character. Note that it works without the spaces, but it's poor practice and harder to read.

</aside>


---

## Even More Mathematical Operators

Beyond the `+`, `-`, `*` (multiply), and `/` (divide) operators, we have modulus and exponents.

```python
making_exponents = 10 ** 2
print(making_exponents)
# Prints 100

more_exponents = 10 ** 3
print(more_exponents)
# Prints 1,000

making_modulus = 10 % 3
print(making_modulus)
# Prints 1

more_modulus = 6 % 2
print(more_modulus)
# Prints 0
```


<aside class="notes">

**Teaching Tips**:

- Be sure students understand what modulus and exponents are. Pull up a blank replit [here](https://repl.it/@GAcoding/blank-repl) if need be.

</aside>


---

## Math On The Same Variable


You can reassign a variable *using that very same variable* - or other variables!

```python
cupcakes_ive_eaten = 3
cupcakes_ive_eaten = cupcakes_ive_eaten + 1
print(cupcakes_ive_eaten)
# Prints 4.
cupcakes_left_in_box = 6
cupcakes_left_in_box = cupcakes_left_in_box - 1 print(cupcakes_ive_eaten)
# Prints 5.
cupcakes_left_in_box = cupcakes_left_in_box - cupcakes_ive_eaten print(cupcakes_ive_eaten)
# Prints 1.
```

<aside class="notes">
**Talking Points**:

- "You may have a scenario where you want to reassign a variable to itself. We do this so we don't have to create extra variables. In our cupcakes example, we don't want to have to use a whole new variable just to add a cupcake."
- "Note that this works because the *right* side of the equals sign is evaluated first. Thus, the `1 + 3`  in the second line is happening before the reassignment. The right side becomes 4, then that value is set to cupcakes_ive_eaten."
- "A great thing about variables is that, because they store a value, you can use them later - even to create new variables. For example, if we have a variable declared `cupcakes_in_a_box = 3`, and we know that there are 5 cupcakes in a box, we can multiply them to determine the number of cupcakes I will eat. Here's an example:"
</aside>

---

## Partner Exercise: Mathematical Operators

Pair up and choose roles:

- Driver
- Navigator

Try to code the below:

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-pt-guitar-prompt?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">
10 MINUTES

**Teaching Tips**

- Facilitate a pair programming activity:
  - Ask students to pair up.
  - One student (the “driver”) should type the code on the slide into repl.it and run it, making sure it works.
  - Then, working together, the two students should complete the code challenges in the comments.

- Once students have all finished, show the answer and recap how it works.

- Whenever possible, have students experiment beyond the prompts on the slide.
- If students grasp the mathematical operators easily, encourage more difficult exercises in the embedded editor - using more than one variable or combining different math symbols. Give few different example exponents to try, like 5**6 or 10%2. Have them guess the answers before running it.

**Talking Points**
- Let’s give it a shot! In a second, I’m going to ask you to pair up and program together in repl.it
- In pair programming, one person serves as the driver -- their hands are on the keyboard -- and one person serves as the navigator -- they provide guidance as the code is written.
- When you pair up, decide who will be the driver and who will be the navigator. Then, follow the directions in the comments.
- Raise your hand when you’ve managed to complete each step, and I’ll come around and provide feedback.

**Repl.it Note:** The code is all comments:

- Make a variable to hold the number of guitars you own (3).

- Make a variable to hold the number of guitars Nikhil owns (1).

- You give 2 of your guitars to Nikhil, so subtract 2 from you and add 2 to Nikhil.


</aside>

---

## Reassignment Shorthand

This is okay:

```python
my_num = 9
my_num = my_num + 7
# my_num is now 16
```

But this is better:

```python
my_num = 9
my_num += 7 # += is short for theSameVariable = theSameVariable + 7
# my_num is now 16
```

This works with `+=`, `-=`, `*=`, `/=` - any math operations.

<aside class="notes">

**Teaching Tips**:

- Stress that the shorthand is equivalent to writing out the reassignment in full.

**Talking Points**:

- "The code on top is good, but it is actually such a common scenario that we want to reassign a variable that we've made a shortcut. For example, saying `my_num += 9` is exactly the same as saying `my_num = my_num + 9`. It's just a shorter way to write it."

- "Keep in mind that we'll always need an `=` somewhere in the line of code when we want to either assign or update the value of a variable"

</aside>

---


## Partner Exercise: Numerical Reassignment

Get with the same partner, but switch driver and navigator roles.

In the environment below, follow the prompts:

<iframe height="400px" width="100%" src="https://repl.it/@GACoding/python-pt-practice-math?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">
10 MINUTES

**Teaching Tips**

- Facilitate a pair programming activity:
  - Ask students to pair up with the same partner, but switch  roles.
  - One student (the “driver”) should type the code on the slide into repl.it and run it, making sure it works.
  - Then, working together, the two students should complete the code challenges in the comments.

- Once students have all finished, show the answer and recap how it works.

- After showing the answer, continue showing experimentations. Spend the majority of the time on the interactive slide - get students doing different shorthands (`+=`, `-=`). These are built into the slide in comments. Encourage experimentation for advanced students.

**Talking Points**
- Let’s give it a shot! In a second, I’m going to ask you to pair up and program together in repl.it
- Remember, in pair programming, one person serves as the driver -- their hands are on the keyboard -- and one person serves as the navigator -- they provide guidance as the code is written.
- Follow the directions in the comments.
- Raise your hand when you’ve managed to complete each step, and I’ll come around and provide feedback.

**Repl.it Note:** The code is all comments:

- Declare two variables `num1` and `num2` and assign them to any numbers you'd like.
- Set `num1` to the result of subtracting `num1` from the `num2`.
- Create a new variable `num3` that will help us tell if `num2` is even or odd.
- Using shorthand, add 5 to `num1`.
- Print out `num1`, `num2`, and `num3`

</aside>

---

## Important Aside: Even or Odd?

Is 6 even or odd?

Is 7 even or odd?

How do you think a computer knows?

Modulus operator shows the remainder of a division problem.

Modding by 2 only gives a `0` or a `1`.

- **4 % 2**:
  - `4 % 2 = 0`. Even!
- **5 % 2**:
  - `5 % 2 = 1`. Odd!


<aside class="notes">

**Teaching Tips**:

- Make sure they understand modulus before talking about how it's helpful! Consider bringing up an [empty replit](https://repl.it/@GAcoding/blank-repl) to demonstrate with various numbers.
- Make sure they understand why this works!

**Talking Points**:

- "This is where modulus is helpful. The modulus operator shows the remainder of a division problem.
-  "For example, five divided by two equals two with a remainder of one. The modulus operator takes two numbers as inputs and returns what is left over from the division."
</aside>


---

## Quick Review

- A variable is a value that can be defined, declared, called and changed within your program.
    - `my_number = 5`
- Naming:
    - Variable names are case sensitive.
    - Use `snake_case`!
- Variables can be reassigned as often as you like, but only the most recent declaration counts.
- Python can do math using operators, such as `+`, `-`, `*`, and `/`
    - You can shorthand the math assignments: `my_num += 7`

<aside class="notes">

1 MINUTE

**Teaching Tips**

- Quickly review what you covered so far.
- Check for understanding


</aside>

---

## Taking a Breather

That was a lot of math!

When it comes down to it, computers operate with a simple, straightforward logic.

Let's switch gears. Up next: Strings!

<aside class="notes">

**Teaching Tips**:

- Use this slide to cue the transition from numerical variables and mathematical operators to string variables.
- Make sure students are all very clear on numerical variables and math operations before continuing past this section.

**Talking Points**:

- "While we've covered what seems like a lot of math in this section, don't worry: You're not going to be doing calculus in this course. However, it's important that we review these concepts, because there will be many times when you'll solve a problem using basic principles. When it comes down to it, computers operate with a simple, straightforward logic."
- “We’ve learned about numerical values and mathematical operators. Now, we’re going to transition to string variables.”


</aside>


---

## Introducing Strings

<!--

**Talking Points**:
> "Because a variable is just a box, it can also hold strings. You tell Python that your variable will hold a string using quotation marks."

> "Strings can be words, like apple. Strings are made of characters. A character is anything on your keyboard , such as a letter or a number. The string apple is 5 characters."

> "A space counts as a character, too (it's on the keyboard). For example, "Marty McFly" is a string. So is this entire sentence:"
-->

A *character* is:

- Anything on your keyboard , such as a letter or a number.
- "Apple" is five characters: a, p, p, l, e.
- Spaces count! (they're on the keyboard!)

A *string* is:

- A complete list of characters.
- "Apple"
- "Chocolate Cupcake"
- This entire sentence: "Hello, you are 1 of a kind!"

<aside class="notes">
**Talking Points**:

- "Because a variable is just a box, it can also hold strings. You tell Python that your variable will hold a string using quotation marks."

- "Strings can be words, like apple. Strings are made of characters. A character is anything on your keyboard , such as a letter or a number. The string apple is 5 characters."

- "A space counts as a character, too (it's on the keyboard). For example, "Marty McFly" is a string. So is this entire sentence:"

</aside>


---

## How Do I Create Strings in Python?


You tell Python that your variable will hold a string using quotation marks.

```python
box_contents = "cupcakes" # This is a string
print(box_contents) # It's a normal variable - we can print it.
best_snack = "Frosted Cupcakes" # This is a string.
cupcakes_ive_eaten = 5 # No quotes - this is a number.
cupcakes_ive_eaten_as_string = "5" # Because this is in quotes, this is a string.
```

<aside class="notes">

**Talking Points**:

- "To declare a string in Python, put it in quotes when you assign it to your variable."

**Teaching Tips**:

- Go over the phrase "numerical variable" versus "string variable".
- Walk through the difference between strings and numbers here. Be clear that they're both variables, just different types.

</aside>

---

## We Do: Declaring Strings

A "We Do" means let's practice together. Follow along!

1. We'll declare a variable called `name` and assign it the value `Marty`
2. We'll declare a variable called `car` and assign it the value `Delorean`
3. We'll declare a variable called `speed` and assign it the *string* value `"88"`
4. We'll print out these variables
5. We'll add `4` to `speed`- what happens?

---

## We Do: Declaring Strings

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/blank-repl?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">

**Talking Points**:

- "Let's declare some variables in and print them. You'll be doing a lot of programming, and if you practice typing variable declarations out, you'll get faster every time."

After you run the very last one...

- "It's important to note that you cannot do math on strings! Even if what's inside the quotations is a number, Python will interpret it as a word."

- "Can you predict what the code below will print?" <wait for them to discuss, then run it.>

- "In our last example, instead of printing `92` like you might expect, Python will throw an error. It sees `speed` as a string, not a number, so it doesn't know how to do addition on it."

- "Make sure that when you want a numerical value you do not use quotes!"

**Teaching Tips**:

- Do this with the students! But make sure they do it, too, so they get the typing practice.
- Go over the phrase "numerical variable" versus "string variable"
- Give them a second to guess the math failure before doing it.

</aside>


---

## String Concatenation

`+` on:

- Numerical variables adds (`5 + 5 = 10`).
- String variables *concatenate* (`"Doc" + "Brown" = "DocBrown"`).
  - *Pssst: Pronunciation tip: con-CAT-en-ATE*
- Numerical strings concatenate to new strings! (`"5" + `"4"` = `"54"`)

```python
first_name = "Doc"
last_name = "Brown"
full_name = first_name + last_name
print full_name
# Prints "DocBrown".
```

<aside class="notes">
**Talking Points**:

- "The `+` operator means addition for numbers, but not for strings. When given string values, the `+` operator actually behaves differently — it concatenates, or combines, two strings together to make one big string. Using the `+` operator to combine the two strings together literally puts them next to each other instead of evaluating their total."

- "Concatenation is a formal term for when strings are glued together. Here's an example of concatenation."

- Stress that the plus sign will not add string variables with numbers in them.

</aside>

---

## We Do: Spaces in Concatenation

It's another "We Do." Let's do this together -  follow along!

To begin: `sentence = name + "is driving his" + car + speed`

We expect the sentence to be `Marty is driving his Delorean 88mph`. Is that what we got?


<iframe height="400px" width="100%" src="https://repl.it/@GACoding/python-variables-marty?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">

**Teaching Tips**:

- Do this on the slide, but make sure students follow along.
- Explain it as you go. After students see the lack of space, show them adding in the spaces yourself: `sentence = name + " is driving his " + car + " " + speed`. Then, show commas: `print(name, "is driving his", car, speed)`
- Stress that commas *only* work for `print`ing, not for concatenation.

**Talking Points**:

- Python put the strings together, but do you notice anything wrong? There is no space between the words! This is because we didn't add the spaces in. It's just one of many reasons why we have to carefully watch our spacing and grammar!"
- "Since a space is a character - it's on the keyboard - we can make it a string. Therefore, we can add it into our concatenation. By default, concatenation doesn't have spaces - you'll always have to add them yourself."
- "You can also `print` directly; you don't necessarily need an extra variable. To print strings next to each other, you separate them with a comma. Then, Python will add the space for you. This isn't concatenating variables, but it's useful to know!" Change code to: `sentence = name + " is driving his " + car + " " + speed`
- "When `print`ing, commas also create spaces." Change code to: `print(name, "is driving his", car, speed)`


**Repl.it Note**: The code is:
```python
name = "Marty"
car = "Delorean"
speed = "88mph"
```
</aside>

---

## Strings and Printing: Review

Strings are made with quotes:

```python
name = "Marty"
car = "Delorean"
speed = "88"
```

String Concatenation - we need to add the spaces!

```python
sentence = name + " is driving his " + car + " " + speed
string_numbers = "88" + "51"
# string_numbers = 8851
```

To easily create spaces while printing:

```python
print(name, "is driving his", car, speed)
```

<aside class="notes">

1 MINUTE

**Teaching Tips**

- Quickly review what you covered so far.
- Check for understanding.
- Use the extra time here to check in with students and make sure they've got the hang of declaring, using, and printing numbers and strings.
- Make sure students don't try to use commas for adding spaces outside of a print statement!


</aside>


---

## Discussion: Some Common Mistakes: 1


Do you think this will run? If yes, what does it print?

```python
my_num
print(my_num)
```

<aside class="notes">

2 MINUTES

**Teaching Tips**:

- Encourage discussion on this and following slides before giving the  answer.

**Talking Points**:

- "Let's look at some code with some common beginner mistakes. What do you think is wrong with the following code? Will it run at all? If yes, what does it print?"
- Answer here: No, it won't run; you've declared a variable without assigning it to a value.

</aside>


---

## Discussion: Some Common Mistakes: 2

How about this? Does it run? If so, what does it print?

```python
my_num = 5
print()
```

<aside class="notes">

Answer: It will run, but it won't print anything.

</aside>

---

## Discussion: Some Common Mistakes: 3

How about this? Does it run? If so, what does it print?

```python
my_num = 5
my_string = "Hello"
print(my_num + my_string)
```

<aside class="notes">

Answer: This won't run, because Python will try to add a string and a number and throw an error.

</aside>

---

## Discussion: Some Common Mistakes: 4

One last question. What does this do?

```python
my_num1 = "10"
my_num2 = "20"
print(my_num1 + my_num2)
```

<aside class="notes">

Answer: There's nothing wrong with this one, except that it makes a string and not a number. It prints the string 1020.

</aside>

---

## Q&A and Summary

We learned a lot today!

- We created, used, and re-assigned number and string variables.
- We used the numerical operators `+ - / * // %`
- We did some complex stuff with the `print` function!

Congrats! You've finished your first programming lesson!

<aside class="notes">

**Teaching Tips**:

- Summarize the lesson and provide a preview of what’s coming next.
- Open your own blank [repl.it](https://repl.it/@GAcoding/blank-repl) in a new tab if needed to recap and be sure everyone is clear.

</aside>


---

## Additional Resources

* [A Repl.it Summarizing Print Statements](https://repl.it/@brandiw/Python-01-Variables-4?lite=true)
* [Python For Beginners](http://www.pythonforbeginners.com/basics/python-variables)
* [Python Programming Tutorial: Variables](https://www.youtube.com/watch?v=vKqVnr0BEJQ)
* [Variables in Python](https://www.guru99.com/variables-in-python.html)
* [Operators Cheatsheet](http://python-reference.readthedocs.io/en/latest/docs/operators/)
* [Python Style Guide: Naming](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)
- [Python-Strings](https://www.tutorialspoint.com/python/python_strings.htm)
- [String Concatenation and Formatting](http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python)
- [String Concatenation and Formatting - Video](https://www.youtube.com/watch?v=jA5LW3bR0Us)


<aside class="notes">

**Teaching tips:**

- Most lessons have additional resources at the end. Encourage students to explore these on their own time - don't go through them now.

</aside>
