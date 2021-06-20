<!--
title: Variable Scope
type: lesson
duration: "00:30"
creator: Brandi Butler
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Unit 3 Lab: Variable Scope</h1>

<!--

## Overview
This lesson introduces local and global scope with a few examples. If there is time, give students examples of broken programs that mix up global and local scopes, and ask them to fix it.

## Learning Objectives
In this lesson, students will:

* Define variable scope.
* Explain the order of scope precedence that Python follows when resolving variable names.


## Duration
20 minutes

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:08 | Local Scope |
| 0:08 - 0:18 | Global scope |
| 0:18 - 0:20 | Summary |

## Differentiation and Extensions
- There are no exercises involving classes, built-in scope, or enclosed scope. If there is time and your students seem confident, create some — or challenge your students to come up with examples themselves.

## In Class: Materials
- Projector
- Internet connection
- Python 3
-->

---

## Lesson Objectives
*After this lesson, you will be able to…*

* Define variable scope.
* Explain the order of scope precedence that Python follows when resolving variable names.

<aside class="notes">

**Teaching Tips:**

- Jot these on the board for reference.

</aside>

---

## Discussion: Delivering a Letter

What if someone wanted to send Brandi a letter?

If you just had "For Brandi," the mail carrier would give the letter to the first Brandi they see!

They'd look:

- First in the class. Is there a "Brandi" here? They get the letter!
- No? OK, look in the town. Is there a "Brandi" here? They get the letter!
- No? OK, look in the state. Is there a "Brandi" here? They get the letter!

<aside class="notes">

**Teaching Tip:**

- Don't mention programming here. Just make sure the class is clear on the idea of scope and how, if we aren't specific, we'll look first in town, then state — continue getting wider.

</aside>  

---

## Discussion: Your Address

That's why **scope** matters. We might have to get more specific. To correctly deliver the letter, if the mail carrier only looked in the scope of:

Your class:

- You're probably the only Brandi.
- "For Brandi" is fine.

Your town:

- There might be multiple Brandis in the town.
- "For Brandi, on Main Street" is a bit more specific.

In your state:

- There are multiple Main Streets in New York!
- "For Brandi, on Main Street in Brooklyn" is more specific.

---

## Discussion: What Is `x`?

Python has **scope**, too. We can have many variables with the same name, and Python will look for the most specific one.

In different scopes, you can reuse the same name. Each one is a *completely different* variable.

Functions and classes create individual **local scopes**. A **local variable** doesn't exist outside its local function or class scope.

```python
def my_func1():
  x = 1    # This is a LOCAL variable.
  print(x) # 1

def my_func2():
  x = 5    # This is a DIFFERENT local variable.
  print(x) #5

print(x) # x is OUT OF SCOPE - no x exists here!
```


<aside class="notes">

**Teaching Tips:**

- Walk through this carefully!
- Run it in an interpreter, repl.it, or file to show it working (remove the last `print` to stop the error).
- Terminology is next — just get students to understand the idea.

**Talking Points:**

- Any variable declared or assigned inside of a function is local to that function.
- This is the most specific level of scope and is, ideally, where most of your variables should be declared.
- Only the function in which the variable was declared has access to this scope — i.e., the variable is out of scope for everything but that function.
</aside>  

---

## Global Scope

- Variables that are in **global scope** can be accessed by any function.
- Python will adopt an 'inside-out' strategy when evaluating variable of the same name, giving precidence to a local variable before using a global one.
- When we define a variable _inside_ a function, it's local by default.
- When we defint a variable _outside_ a function, it's global by default.

```python
x = 2

def my_func1():
  x = 1
  print(x) # 1 - Python checks local scopes first.

def my_func2():
  x = 5
  print(x) # 5 - Python checks local scopes first.

my_func1()
my_func2()

print(x) # 2 - Python found no local scope; prints global variable.
```

<aside class="notes">

**Talking Points:**

- If some variables are specifically local, what are the variables outside of a function or class called?
- Any variable declared or assigned outside of any function or class is considered "global."
- Global variables are accessible from anywhere in the script. This is not necessarily a good thing, however, because those variables can be accessed, changed, or reassigned by anything, and this can lead to troublesome bugs.
- This is another case where Python has our backs. It's preventing us from making an accidental error that could easily occur in many other languages.
* Python assumes local unless otherwise specified.
    * Meaning, these `x`s are three different variables.
* Python does this to prevent unexpected behavior and accidental bad practice.
    * Global variables should be avoided whenever possible. Some argue that you will need to use a global variable _if multiple functions need access to that variable_. This is almost never true. If the function needs access to that variable, it should enter that function as a parameter. This maintains the integrity _of the interface between the data and the function that is called_.
    * _Any_ function that has access to the variable (i.e. all functions) can potentially modify its state. As an application grows, you will likely be unable to determine which function is modifying this global variable's state and it can be extremely difficult to debug.
</aside>

---

## Multiple Variables, One Name

Use case: `x` and `y` are frequently used to represent numbers.

Scope is important so they don't interact!

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

divide (8,2) # Returns 4
multiply(3,1) # Returns 3
```

<aside class="notes">

**Talking Point:**

- Why would you want to have different variables with the same name? Do you expect each `x` and `y` in this code to perform independently?
</aside>

---

## We Do: Accessing Scopes

Let's start with global scope:

```python
foo = 5
print(foo)
foo = 7
print(foo)
```

<aside class="notes">

**Talking Point:**

- Python makes it a little trickier than other languages to fiddle around with global variables if we're not already in that scope. First, start up a blank script. The following line will assign a global variable named foo the value of `5`. We can easily reassign and access that variable with the following lines. That's the global scope: There's no restriction on accessing or mutating a variable.

**Teaching Tip:**

- Run all the code in these slides in an interpreter for students to see. Encourage them to do this with you.
</aside>

---


## We Do: Accessing Local Scope

What if we add a variable in a local function scope and try to access it from the global scope?

```python
foo = 5

# Delete your other code.
# Add this function and print calls instead.
def coolFunc():
  bar = 8

coolFunc()
print(foo)
print(bar)
```

It fails!

<aside class="notes">

**Talking Points:**

- If you run this code, you will get an error: `NameError: name 'bar' is not defined.`.
- The variable bar is only accessible from inside the `coolFunc()` function.
- We called the `coolFunc()` function, but as soon as it finished running, the variable bar ceased to exist. Even while the function was running, it was only accessible to itself. But, `foo` in the global scope was still accessible.
</aside>

---

## Scope Can Be Tricky

What do you think happened here?

```python
foo = 5
def incrementFoo():
  foo = 6
  print(foo) # prints 6

print(foo) # prints 5
incrementFoo()
print(foo) # prints 5
```

<aside class="notes">

**Teaching Tip:**

- Spend some time here. Ensure student understanding.

**Talking Points:**

- Hey! The variable `foo` went back to its old value after the function finished! Actually, not quite. Here's what happened:
    - The line in the function where `foo` is assigned the value of `6` causes the creation of a new local variable.
    - We then set this variable's value to `6`, the function prints the value, and the function finishes. However, the global variable `foo` was never touched by the function.

**Teaching Tips:**

- Run this!
</aside>

---

## You Do: Just a Day in the Jungle

Open a new local file, `piranhas.py`.

* Declare a global variable `piranhas_hungry` and set it to `True`.
* Write two functions, `swing_vine_over_river` and `jump_in_river`.
* In `swing_vine_over_river`:
  * Print `Ahhh! Piranhas got me!`.
  * Change `piranhas_hungry` to `False`.
* In `jump_in_river`:
  * If `piranhas_hungry` is `True`:
    * Print `I'm not going in there! There are hungry piranhas!`.
  * Otherwise:
    * Print `Piranhas are full! Swimming happily through the Amazon!`

---

## You Do: Just a Day in the Jungle

* Try this first by _not_ passing `piranhas_hungry` as an argument to `swing_vine_over_river` and `jump_in_river`. Can you make it work?
* If you can't make it work, _pass_ `piranhas_hungry` as an argument to the two functions. Does it work now?

```python
# Call functions in this order.
jump_in_river()
swing_vine_over_river()
jump_in_river()
```

Speak up if you need some help!

<aside class="notes">

**Teaching Tip:**

- Give students a few minutes. The answer is on the next slide.
</aside>

---

## We Do: Check Your Answers

* Are you able to access the global variable `piranhas_hungry` if it is _not_ passed as an argument to your functions?
  * Why or why not?
* What is the solution to this?

<iframe height="500px" width="100%" src="https://repl.it/@GAcoding/variable-scope?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

---

## Summary and Q&A

Python checks **scope** to find the right variable.

- Functions and classes create individual **local scopes**.
    * A `local` variable doesn't exist outside its local function or class scope.
- Any variable declared or assigned outside of any function or class is considered "global."
    - Variables that are in **global scope** can be accessed anywhere.

Python will check for a `local` variable before using a `global` one.

There can be more levels. Python always works from the inside out — keep that in mind as your programs get more advanced!

<aside class="notes">

**Teaching Tip:**

- Do a check for understanding.
</aside>

---

## Additional Resources

* [Global vs. Local Variables](https://www.python-course.eu/python3_global_vs_local_variables.php)
* [Variables and Scope](http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html)
* [Nested Functions — What Are They Good For?](https://realpython.com/inner-functions-what-are-they-good-for/)
