<!--
title: Python Programming: Advanced Function Arguments
type: lesson
duration: "01:00"
creator: Brandi Butler
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Advanced Function Arguments</h1>


<!--

## Overview
This lesson starts with a review of the previous function lesson, leading into a few recap exercises. After that, it discusses `*args`, `kwargs`, and default argument values.

## Important Notes or Prerequisites
- Important Note: They don't know dictionaries yet! We introduce `**kwargs`, but are careful not to phrase it in terms of dictionaries.

## Learning Objectives
In this lesson, students will:
- Use arbitrary numbers of arguments in functions.
- Use keyword arguments in functions.
- Use default values in functions.

## Duration
40 minutes


## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:10 | Function Review |
| 0:10 - 0:30 | Args / Kwargs |
| 0:30 - 0:42 | Other Args |
| 0:42 - 0:45 | Summary |

## In Class: Materials
- Projector
- Internet connection
- Python3
-->


---

## Lesson Objectives
*After this lesson, you will be able to...*

* Review all topics to this point.
* Use keyword arguments in functions.

<aside class="notes">

Teaching tips:

- Quickly go over the learning objectives.

Talking points:

- What if I want to have a variable number of arguments?
- What if I want to have my arguments out of order?
- What if I want to specify some arguments but not others?
- We're going to learn all of this.

</aside>

---

## Review: Functions

Main points:

* Define functions using the `def` keyword.
* A function must be **called** before the code in it will run!
* You will recognize function calls by the `()` at the end.

```python
# This part is the function definition!
def say_hello():
    print("hello world!")

# This part is actually calling/running the function!
say_hello()
```

<aside class="notes">

Teaching tips:

- They've seen this a few times, but make sure to recap the syntax again. We're throwing a lot at them quickly.
- Try not to spend too much time on any of these review slides; there's a lot of new stuff to  cover.

Talking points:

- Recap the point of functions (e.g. DRY)

</aside>

---

## Review: Function Arguments

* Provide an argument to a function when you need something small to vary.

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-args-practice?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">


Teaching tips:

- This is a demo and recap,  not an exercise.
- They've seen this a few times, but make sure to recap the syntax again. We're throwing a lot at them quickly.
- Give other examples where parameters would be useful.

Talking points:

- "A lot of times, you want to run the same code, but with a teeny tiny difference. Remember the function we looked at before which had the orders with the $5 shipping charge?"

**Repl.it Note**: The code here is:
```python
def print_order(product):
  print("Thank you for ordering the " + product + ".")
  print("There will be a $5.00 shipping charge for this order.")

print_order("Trampoline")
print_order("Spider-Man Comic")
print_order("Hot Cheetos")
```
</aside>


---

## Multiple Parameters

Functions can have...

```python
# No parameters
def add_2_and_3():
    x = 2 + 3
    print(x)

# One parameter
def add_2(x):
    print(x + 2)

# Multiple parameters
def add(x, y, z):
    print(x + y + z)
```


<aside class="notes">

Teaching tips:

- They've seen this a few times, but make sure to recap the syntax again. We're throwing a lot at them quickly.
- Give an example where each case would be useful.

Talking points:

- "Functions can have many parameters... or not!"

</aside>


---

## Discussion: Print vs Return

Why doesn't this do anything?

```python
def add(x, y, z):
    return x + y + z

add(1, 2, 3) # does nothing!
```


<aside class="notes">

Teaching tips:

- Facilitate a discussion! See if one of the students can tell you.
- Bring it up in a repl.it - [here it is with the code](https://repl.it/@GAcoding/python-programming-return-print?lite=true). Add back in the print statement.

</aside>

---

## We Do: Review Exercises


Locally, let's create a file called `function_practice.py`.

- We'll define a function named `areBothEven`.

- It will accept two parameters: `num1` and `num2`.

- Inside the function, we'll return `True` if `num1` and `num2` are both even but `False` if they are not.

- We'll test this with `print(areBothEven(1, 4))`, `print(areBothEven(2, 4))`, and `print(areBothEven(2, 3))`.

<aside class="notes">

Teaching tips:

- Do this with them, but make sure they pull up a file and are following along. We don't have time  for a full exercise - we just want to be sure everyone understands functions before we make this far harder.

- Talk them through this - "Use the modulus operator (`%`) to see if both numbers are even. If you use `num % 2`, it will return `1` if the number is odd and `0` if the number is even.""

</aside>

---

## We Do: Another Review Exercise!

In our file, we'll define another function named `lightOrDark` that takes the parameter `hour`.

- If `hour` is greater than 24, the function will print "That's not an hour in the day!" and **return nothing.**

- If `hour` is less than 7 or greater than 17, the function will return "It's dark outside!"

- Otherwise, the function will return "It's light outside!"

- We'll test this with `print(lightOrDark(4))`,  `print(lightOrDark(26))`, and `print(lightOrDark(`10`))`.

<aside class="notes">

Teaching tips:

- Do this with them, but make sure they pull up a file and are following along. We don't have time  for a full exercise - we just want to be sure everyone understands functions before we make this far harder.

- Talk about how we can just have `if` statements - we don't need an `elif` because the `return` exits the function.

</aside>


---

## Discussion: Arguments

Now, let's make functions a little more sophisticated.

What do you think the following code does?

```python
def multiply(x, y):
    print(x * y)

multiply(1, 2, 3) # Too many arguments! What happens?
```

What if we want all of these to work?

```python
def multiply(x, y):
    print(x * y)

multiply(4, 5, 6)
multiply(4, 5)
multiply(4, 5, 2, 7, 3, 9)
```

<aside class="notes">

Teaching tip:

- After they guess, show them the error in an interpreter.
- There's a lesson on errors later - don't go into it here. Just show that it breaks, but we want to be able to pass `multiply` any number of arguments.

Talking point:

- "When we tried to run the function with too many arguments, we got an error."
- "What if I want to have any number of arguments?"

</aside>


---

## Introducing `*args`

`*args` is a parameter that says "Put as many parameters as you'd like!"

- Pronounced like a pirate - "arrrrghhhs!"
- Known as **positional arguments**
- The `*` at the beginning is what specifies the variable number of arguments

```python
def multiply(*args):
    product = 1

    # We don't know the number of args, so we need a loop
    for num in args:
        product *= num
    print(product)

multiply(4, 5, 6) # Prints 120!
```

<aside class="notes">

Teaching tips:

- Point out why we need a loop, and why we need the `product` declaration  at the top.
- Remind students about the shorthand `*=` syntax.
- Make sure students don't forget the `*` or the `s` in `*args`
- There's a repl.it  [here](https://repl.it/@GAcoding/python-programming-args-multiplication?lite=true) if you  want to run this.

</aside>

---

## We Do: `*args`

Let's create a local file for this lesson - `args_practice.py`.

- We'll write a function, `sum_everything` that takes any numbers of arguments and adds them together.
- At the end, we'll print out the sum.
- Let's try it with `sum_everything(4, 5, 6)` and `sum_everything(6, 4, 5)`. The order doesn't matter!
- `*args` says "any number" - you can pass in none at all!

<aside class="notes">

Teaching tips:

- Do this with them, but make sure they have a file  out and are following along. The more they practice writing this, the better.
- See if they can guess what a line should be before you write it.
- Since it's a loop, the order of arguments doesn't matter.
- Once the code is written, show them a varying number of arguments being passed in. 1? 4? Without any arguments passed in at all (especially this one!).

**Solution Code**:

```python
def sum_everything(*args):
    sum = 0

    # We don't know the number of args, so we need a loop
    for num in args:
        sum += num
    print(sum)

sum_everything(4, 5, 6) # Prints 15
```

</aside>

---

## Discussion: Often, Order Does Matter.

Let's switch gears. Back to a set number of arguments!

Check this out:

```python
def triple_divide(x, y, z):
    print(x / y / z)

triple_divide(1, 2, 10) # Prints 0.05
```

Without otherwise specifying, `x` is `1`, `y` is `2`, and `z` is `10`.

- What if we want `x`, the first parameter to get the value `10`?
- Is there a way to specify which argument goes to which parameter?

<aside class="notes">

Teaching tips:

- Emphasize that we're done with `*args` specifically; we're moving on to a different type of arg specifics.
- Run this a few different ways to show order matters.
- Remind them what "argument" versus "parameter" is.
- Try to get them guessing, here.

Talking points:

- "This lesson is about all types of arguments in functions. We've seen a variable number - now let's look at something else."

</aside>

---

## Forcing the Order

Here we've forced the order to be reversed from the default. In fact, we can specify any ordering we want by using the names of the parameters (keywords) when providing the argument values.

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/02-Python-Kwargs-09?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Take a moment to play around with the values until you really believe it!

---

## Keyword Arguments (kwargs)

Using kwargs, odrer deons't mtater:

- Arguments are named according to their corresponding parameters.
- Order doesn't matter - Python will check the names and match them!
- Values are assigned because the *keyword argument* and the *parameter name* match.


```python
def triple_divide(x, y, z):
    print(x / y / z)

triple_divide(x=10, y=2, z=1)
# This runs 10 / 2 / 1, and prints 5
triple_divide(y=2, z=1, x=10)
# This ALSO runs 10 /  2 / 1, and prints 5.
```

> **Protip**: Keep your parameter names simple and concise to prevent typos and misspellings!

<aside class="notes">

Teaching tips:

- Show this in an interpreter, or bring up a repl.it. Change the values and order of x, y, and z here so students can really understand.
- Get students comfortable with when order matters and what we can do about it.

Talking points:

- "In normal cases for function args a default order is assumed. Much in the same way, if you go to a restaurant, by default you will get drinks, then appetizers, then entrees, then desserts. However, you are free to ask your waiter to bring your dessert first or bring your appetizer with the meal. You don't need to specify anything if the default order will do, but if you are going to reinvent dinner order, you will need to say something!"


</aside>


---

## Mix It Up....  but Not With Every Argument?

Fun fact: You can provide some args in order - **positional** - and some with keywords.

- Undefined are assigned in sequential order.
- Keywords have to come last! - then, in any order.

```python
dinner(app="chicken wings", main_course="medium rare steak", drink="water", dessert="milkshake")
dinner("chicken wings", "water", dessert="milkshake", main_course="medium rare steak")
```

<iframe height="300px" width="100%" src="https://repl.it/@GAcoding/02-Python-Kwargs-08?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

Talking points:

- As you make the demo more and more complex, make sure to talk about what you're doing.

Teaching tips:

- This is a demo, so don't worry about them following along  (though it's great if they do!).
- First, recap and call the function with the kwargs in different orders:
`dinner(app="nachos", main_course="steak", drink="water", dessert="cake")`
- Then, talk about how you don't necessarily need every keyword defined -  but they'll automatically be assigned in order. Demo that:
`dinner("water", "nachos", dessert="cake", main_course="steak")`
`dinner("nachos", "water", dessert="steak", main_course="steak")`
- Then, show what happens if you put a kwarg first: `dinner(main_course= "steak", "nachos", "water", dessert="cake")`
- What happens if you name two arguments the same? `dinner(app="nachos", app="steak", app="water", dessert="cake")`
- End with correct syntax, so that's freshest in their mind.


**Repl.it Note:** The code here is:

```python
def dinner(drink, app, main_course, dessert):
  print("You're drinking", drink)
  print("You're snacking on", app)
  print("You're drinking", main_course)
  print("You're wrapping up with", dessert)

dinner(app="nachos", main_course="steak", drink="water", dessert="cake")
```
</aside>

___

## Quick Review

`*args`: Any number of arguments - even 0! - can be passed in.

```python
def sum_everything(*args):
    sum = 0

    for num in args:
        sum += num
    print(sum)

sum_everything(4, 5, 6) # Prints 15
```

Keyword arguments (kwargs): Arguments can be passed in out of order.

```python
def divide(first, second, third):
    print(first / second / third)

divide(first=10, second=2, third=1)
divide(second=2, third=1, first=10)
```

<aside class="notes">

Teaching tips:

- Do a quick check for understanding.

</aside>

---

## Discussion: Variable Numbers of Kwargs?

What if I go to Froyo? I need:

- One argument `spoon`, to pick a spoon size.
- A variable number of arguments for all the flavors of frozen yogurt I might eat!

`def yogurt_land(*args)`?

- No! `*args` won't work - we need to know which arg is the spoon.

`def yogurt_land(spoon, froyo)`?

- No! We don't know the number of froyo arguments.

Any ideas?

<aside class="notes">

Teaching tips:

- Encourage them to give ideas. See if they can come up with putting the two ideas together. Remind them that the `*` is the important part of `*args`.

</aside>

___

## Introducing: `**kwargs`

The `*` in `*args` means: Any  number of arguments.

Let's add `**` to our kwargs: `**kwargs` can take a variable number of arguments. Note the double `**`!

```python
def yogurt_land(spoon, **kwargs):
  print(spoon)
  # We need a loop, because we don't know how many kwargs there are.
  for keyword, flavor in kwargs.items():
    # kwargs.items has the keyword and the value, which we're calling "flavor" in the loop.
    print("My", keyword, "is a", flavor)

# Like before, the unnamed arg has to come first!
yogurt_land("large!", first_froyo="vanilla", second_froyo="chocolate", third_froyo="banana")
```

<aside class="notes">

Teaching tips:

- The next slide has a repl.it so you can demo the code! If students are lost, just turn the slide earlier.
- They **haven't learned dictionaries**. Don't stress on the structure of kwargs. Just get them to understand that `kwargs` will hold the keyword and then the value.

Talking points:

- Walk through this. Note that the spoon size has to come first, and stress that here, it's two `**`, not just one. Note the `for` loop!
- Note that 'kwargs' is just a convention, but don't press this point - it's a lot to take in already.

</aside>

---

## We Do: 4 Froyos

* Can we subtract one of the froyos?
* Where is my 4th froyo?
* What if I drop all my froyos on the ground? (No kwargs)
* Can I skip the drink or spoon positional arguments?

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/python-programming-args-froyo?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

Teaching tips:

- This is a demo slide, not an exercise. Spend enough time to make sure they understand what's going on, then move on.
- Show changing the order and number of kwargs. Show having no kwargs. Trying giving all kwargs the same keyword. For each of these, talk about what's happening and why. Try putting the kwargs in the definition first, and in the function call first. Remember not to mention dictionaries!
- Show all variations with `spoon`: having no spoon, then giving the spoon the kwarg `spoon`, then putting the `spoon` at the end (and then in the middle) of the kwargs, then putting the spoon argument (with no `spoon` kwarg at other places). For each of these, talk about what's happening and why.
- End again with the correct syntax, so students remember what it should look like.

**Repl.it Note:**  The repl.it has

```python
def yogurt_land(drink, spoon, **kwargs):
  if spoon:
    print("Here is your spoon!")

  else:
    print("No spoon, no worries")

  print("Here is your", drink)

  for keyword, flavor in kwargs.items():
    print("My", keyword, "is a", flavor)


yogurt_land("water", "large", first_froyo="vanilla", second_froyo="chocolate", third_froyo="banana")
```
</aside>

---

## Quick Review of Useful Argument Types:

At this point, we have `*args`, `kwargs` and `**kwargs`:

```python
# Args: Any number of arguments:
def multiply(*args):
    product = 1
    for num in args:
        product *= num

multiply(4, 5, 6)

# Kwargs: Named (keyword) arguments
def triple_divide(x, y, z):
    print(x / y / z)

triple_divide(x=10, y=2, z=1)

# **Kwargs: Any number of Kwargs
def my_froyo(spoon, **kwargs):
  for froyo, flavor in kwargs.items():
    print(froyo, "is a", flavor)

my_froyo("large!", froyo1="vanilla", froyo2="chocolate", froyo3="banana")
```

<aside class="notes">

Teaching tips:

- Do a quick check for understanding.

</aside>


---

## Discussion: Printing

`print` is a function! That's why it has parentheses!
- It's built into Python, so you don't have to define it. You can just use it.

When printing, commas automatically add spaces:

```python
print("Hi!", "Vanilla,", "please.")
```
But since `print` is a function, too - do you think there's anything we can do to change those spaces to something else?

```python
# Hi!-Vanilla,-please,-but-chocolate-is-cool.
# Hi!-and-Vanilla,-and-please.
```

<aside class="notes">

Teaching tips:

- It's probably a revelation that `print` is a function. Start with that - make sure they understand that, first.
- Encourage a discussion. Can they get to the idea of adding arguments to `print`?

</aside>


---


## Print is AWESOME: Optional Parameters


Turns out...

- `print` accepts an optional keyword argument: `sep`.

The `sep` value given will be used as a **separator.**

- It's optional! Without it, `print` by default uses a space, which is why you haven't seen it.
- **This only applies when using commas.**

```python
print("Hi!", "Vanilla", "please,",  "but", "chocolate", "is", "cool.", sep="--")
# => Hi!--Vanilla,--please,--but--chocolate--is--cool.
```

<aside class="notes">

Teaching tips:

- Stress that this only works for commas, not for using `+`!
- Note that the default value, or optional value, is what happens for an argument when you don't specify it.  We'll get to optional parameters next.
- There's a replit on the next slide to demo this.

Talking Points:

- Remind them again that `print` is a function.
- "Remember at the beginning of the class when we were learning variables, and we had a section on how awesome the print statement is? Well, it has even more neat options to offer!"

</aside>

---

## Delicious Printing

- We can replace `name` and `dessert` with your own name and favorite dessert. It's a regular print!
- `sep` can be any string, or even an icon (they're made of strings - we'll see later!) - but not an int.

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/02-Python-Kwargs-6?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

Teaching tips:

- This is just a demo! Show it working and check for understanding.
- Change the value of sep to numbers, other strings, and even back to the default space. Then, leave it out again to remind them that this is a normal print statement. Then try putting `sep` first and show that it doesn't work - it's a kwarg, after all!
- Point out the special character and how cool Python is, but don't go into unicode or how it's done. We can talk about that in unit 4.

**Repl.it Note** The code here is:

```python
name = "Brandi"
dessert = "froyo"
print("Hello", "my", "name", "is", name, "and", "I", "enjoy", dessert, ":)")
print("Hello", "my", "name", "is", name, "and", "I", "enjoy", dessert, ":)", sep=" HELLO ")
print("Hello", "my", "name", "is", name, "and", "I", "enjoy", dessert, ":)", sep="🍧")
```

</aside>

---

## Quick Review

So  far, we've learned:

- `*args`:
    - ​A variable number of function arguments.
- kwargs:
    - ​A set number of function arguments.
    - Can be defined out of order
- `**kwargs`:
    - Any number of positional arguments.
- `sep` in print.

There's one more: Optional parameters.

<aside class="notes">

Teaching tips:

- Do a quick check for understanding.

</aside>

---

## Optional Parameters with Default Values

This idea exists in programming - you've already seen it!

The default value for `sep` in `print` is `" "`. You don't **need** to include it.

This makes it optional! **Optional parameters** have default values, so you don't need to include them.

- Only include them if you want to change them!

```python

# Here, `sep` is optional to include. It defaults to a space " ".
print("Hello", "my", "name", "is", name, "and", "I", "enjoy", dessert, ":)")

# But we can include it, if we want, and `sep` will use our value instead of the space.
print("Hello", "my", "name", "is", name, "and", "I", "enjoy", dessert, ":)", sep=" HELLO ")
```

<aside class="notes">

Teaching tips:

- If they seem confused here, add more real world examples. For example...
  - By default, the name people call you is your legal name, but you can optionally specify a nickname - "Joseph" versus "Joe".  
  - By default, the address the mail man delivers to is your house, unless you optionally specify a P.O. Box.
  - By default, the seat you sit in is the same one every day, unless you specify you want to sit somewhere else.

- Remind them that this optional argument had to come last when calling the function.

</aside>

Default parameters are in the *function declaration*.

They're there if you don't include a value.

---


## Any Functions: Optional Parameters with Default Values

These can be added to any functions.

Here, `c` has a default of `20`. We don't need to include it!

```python
# Optional parameters: Default values are only used if needed.
def my_func(a, b, c=20):
    print(a + b + c)
my_func(1, 2)
# Uses the default! Prints 23.
my_func(1, 2, 4)
# Overrides the default! Prints 7.
```

<aside class="notes">

Teaching tips:

- Show this running a few ways. [Here is the code in a repl.it](https://repl.it/@GAcoding/python-programming-optional-parameters) - open this in a new window and talk through it.
- For advanced students, show kwargs and optional parameters together.

Talking points:

* What are the default values doing?
* Why is this different than keyword arguments?


</aside>

---

## Partner Exercise: Poke At It!

Pair up! Choose a driver and a navigator.

- In your local file, write a function, `print_food` that has four optional parameters (all with defaults of your choice): `favorite_food`, `lunch_today`, `lunch_yesterday`, and `breakfast`.

`print_food` should print out each of these.

Call this with a couple different arguments:

- No arguments.
- All arguments - a regular function call.
- 2 keyword arguments. Give all four arguments, but use a keyword for `lunch_yesterday` and `breakfast`.
- All keyword arguments - out of order.


<aside class="notes">

Teaching tips:

5 minutes or so.

- Pair students up.
- Walk around and offer advice, key questions, and help overcome challenges.
- When everyone, or the majority, have it figured out, go over the answers - bring up a file and walk through this.

</aside>

---


## Partner Exercise: Keep Poking!

Change roles!

Underneath `print_food`, rewrite it, twice.

First, write `print_food_args`, using `*args` as the parameter. Start the function by printing `args`, so you can see what's going on. Then, print the values you pass in.

Then, write `print_food_kwargs`, using `**kwargs` as the parameter. Start the function by printing `kwargs`, so you can see what's going on. Then, as above, print the values you pass in.

<aside class="notes">

Teaching tips:

5 minutes or so.

- Pair students up.
- Walk around and offer advice, key questions, and help overcome challenges.
- When everyone, or the majority, have it figured out, go over the answers - bring up a file and walk through this.

</aside>

---

## Summary + Q&A

- `*args`:
    - ​A variable number of function arguments.
    - Taken in any order.
    - `def multiply(*args):`
- kwargs:
    - ​A set number of function arguments.
    - Can be defined out of order
    - `my_func(a=1, b=2, c=3)`
- `**kwargs`:
    ​- Any number of positional arguments.
    - `def froyo(*kwargs)`
- sep in print.
- Optional parameters:
    - Default values in the function declaration
    - `def my_func(a=10, b=15, c=20)`

<aside class="notes">

**Teaching Tips**:

- Summarize the lesson and provide a preview of what’s coming next.
- Open your own blank [repl.it](https://repl.it/@GAcoding/blank-repl) in a new tab if needed to recap and be sure everyone is clear.


</aside>

---

## Additional Resources

* [Optional Parameter Repl.it](https://repl.it/@GAcoding/python-programming-optional-parameters)
* [Keyword Args](http://treyhunner.com/2018/04/keyword-arguments-in-python/)
* [Args and Kwargs](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)
* [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
