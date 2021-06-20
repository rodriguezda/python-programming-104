<!--
title: Scripting
type: lesson
duration: "00:35"
creator: Brandi Butler
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Scripting</h1>


<!--


## Overview
This lesson starts with an explanation of a scripting language vs a compiled language, then goes on to discuss the idea of a script. The majority of the lesson is spent teaching file I/O, with just a couple slides near the end for user input.


## Learning Objectives
In this lesson, students will:
* Explain the uses of scripting.
* Write scripts that perform file I/O.
* Write scripts that take user input.

## Duration
35 minutes.

### Notes on Timing

It would be easy to get carried away and spend a lot of time covering all the tiny pieces of file I/O. There are many slides that introduce terms, such as `with` or `append`, so that students won't be lost if they later find them in a tutorial online. Spend very little time here - enough to ensure the student conceptually understands the concept. They don't need to actually practice it.

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:04 - 0:08 | Introducing Scripting |
| 0:08 - 0:24 | File I/O |
| 0:25 - 0:32 | User Input |
| 0:32 - 0:35 | Summary |


## In Class: Materials
- Projector
- Internet connection
- Python3
-->

---

## Lesson Objectives
*After this lesson, you will be able to...*

* Explain the uses of scripting.
* Write scripts that perform file I/O.
* Write scripts that take user input.

---

## Introduction

Discussion: What comes to mind when you hear the word "scripting"?

![](https://c1.staticflickr.com/2/1570/25942496133_27fb6f2261_b.jpg)


<aside class="notes">
**Talking Points**:

- "Chances are you've run into a problem and heard a coworker smugly say, 'don't worry!, I'll just write a script for it'. Maybe it sounded fancy or mysterious at the time, but today we'll demystify it, and well, now you're going to be that coworker!"

🚫 Scripting is NOT

* ~~Mysterious~~
* ~~Difficult~~
* ~~Impossible~~
* ~~Only for super smart, expert programmers~~

✅ Scripting IS

* Helpful.
* Convenient.
* Fun.
* Makes you look cool to your coworkers!
</aside>

---

## What's a Scripting Language?

There are only two types of programming languages in the world: **scripting languages** or **compiled languages**.

All languages, like Python, are one of these two categories.

Scripting languages:

- One is Python!
- Write code, then immediate run it: `python my_file.py`
- Executes statements in order.
- Find a bug? Fix it, run it, repeat.

---

## What's a Scripting Language?

Compiled languages:

- Compile means "build".
- *We can't immediate run code - the computer can't just read the code and needs to translate it to something it understands first.*
- Write code, *then compile it (not quick!),* then run it.
- Find a bug? Fix it, *wait for the code to compile,* run it, repeat.

You don't need to memorize this - just know that there's a difference, and Python is scripting.

What do you think a *script* is?


<aside class="notes">

**Teaching Tips**:

- It's not important for them to memorize what compiled is - just get the idea that it's a different kind of language.

**Talking Points**:

* A `scripting language` or interpreted language like Python executes statements in order
* A `script` is typically a file with some Python code in it
* A script might calculate something, take input, give output, or do file I/O

All programming languages that exist  in the world fall into one of two buckets. A `scripting language` or interpreted language like Python executes statements in order. A compiled language needs to build your program before running it.

Imagine; you wrote an application with Java. Before  you can run it, you need to compile it - turn it  After compiling completed, you run your application. When running your application, you notice a bug. To fix it, you have to stop your application, go back to source code, fix the bug, wait for the code to recompile, and restart your application to confirm that it is fixed. And if you find another bug, you’ll need to repeat that process again.

In a scripting language, you can fix the bug and just need to reload your application —no need to restart or recompile anymore. It’s as simple as that.

Technically, you've been writing scripts already.

</aside>

---

## What is a Script?

Just some code that does something.

- Usually written in a scripting language.
- Can be as simple or as complex as needed!

Let's write a script:

- Create a file called `my_script.py`
- Open the file in `Atom`.
- Type the line

```python
print("hello world!")
```

**CONGRATS**: You now have a script!

Look familiar? You've been scripting since day 1!

<aside class="notes">
**Talking Points**:

It turns out, you already know how to do this!
</aside>

---

## Scripting, Commonly

When people say scripts, though, they usually mean code that:

* Takes input.
* Gives output.
* Reads or writes to a file.
* Performs a task.

We have "perform a task" down!

<aside class="notes">
**Talking Points**:

All Python files you write are scripts! But when people say scripts, that's not really what they mean.
</aside>

---

## Quick Review

**Script**:

- Just code that does something. You've written dozens of scripts in Python so far!

**Scripting Language**:

- A language where you can immediately run code. Python is one!
- Write -> Run.

**Compiled Language**:

- Compile means build! We can't immediately run code.
- Write -> Build -> Run.

We're only working with Python, so we can just write and run our code!

**Next Up**: Playing with files in Python.

<aside class="notes">

**Teaching Tips**:

- Do a quick check for understanding. Compile can be tough to wrap their head around, since they aren't doing it.

</aside>

---


## Scripting, Part 1: Files

Let's further our programming toolkit.

On your computer, you can:

- Create or open a file (text, jpg, Word doc...).
- Read it.
- Edit it.
- Close it.

These are pretty basic actions. Can we do it in Python?


<aside class="notes">

Teaching tip:

- This is to get them to conceptually understand what we're about to do - don't mention code here.

</aside>

---

## We Do: Let's Read a File!

With files, there are three key points.

1. Tell Python to open the file: `my_file = open(<file name>)`
2. Do something with the file! (Read it, edit it, etc).
3. Close the file when you're done: `my_file.close()`

First, let's check out **read**: View, but not change, the contents, with `read()`.

Let's try. On your Desktop, create a file called "hello.txt" with the word "hi" in it.

1. Now, also on your Desktop, create a file, `first_reading.py`.  Fill it with:
    ```python
    my_file = open("hello.txt")
    print(my_file.read())
    my_file.close()
    ```
2. Run it!

Note: The file must exist already!


<aside class="notes">

**Teaching Tips**:

- Do this with them.
- Make sure they successfully make the .txt file and have all successfully run the code.

</aside>


---

## What About Editing Files?

In programming, "edit" is referred to as "write", short for "write to." How do we write a file?

`open(<file name>)` has optional parameters: `open(<file name>, <mode>)`

- Mode: "What do you want to do with the file?" The default is "read." Use `w` for "write":


```python
# To read a file:
my_file = open("hello.txt")
print(my_file.read()) ## We want this to be write, not read!
my_file.close()

# To write a file:
my_file = open("hello.txt", "w")
## Write some stuff
my_file.close()
```

**Important:** Write *overwrites* the current file!


<aside class="notes">

**Talking Points**:

- Reinforce that write is "replace what's there", not "add to the file".

</aside>


---

## We Do: Writing Files

Let's try this. Change your script. We're going to make it a little more complex - since we're programming, we can use variables!

```python
# Open the file hello.txt
my_file = open("hello.txt", "w")

# Write some content to my_file.txt
my_file.write("Hello world")
my_text = "Apple juice is delicious." # Use the variable!
my_file.write(my_text) # Writes "Apple juice is delicious."
my_file.write("Have a nice day!")

# Always close the file
my_file.close()
```

Run it!

Open the file to check.

**Thought:** How could you make new lines?

<aside class="notes">

**Teaching Tips**:

- Do this with them.
- Make sure they have all successfully run the code.
- Have them talk about making new lines - they've learned `\n` previously.
- If you think they can handle it, give them a few reasons to always close the file.

</aside>

---

## Discussion:  Writing Complex Strings

What happens if we try to `write` multiple strings?

```python
# But it doesn't  work with write.
my_file = open("a_file.txt", "w")
my_text = "Apple juice is delicious."
my_file.write(my_text, "Don't you think?") # Error! Write takes 1 argument (2 given).

my_file.close()
```

Error! `write` only takes one argument. We need to concat the strings. *Always just pass one argument to file.write()*.

```python
my_file = open("a_file.txt", "w")
my_text = "Apple juice is delicious."
string_to_write = my_text + "Don't you think?" # Make one string here!
my_file.write(string_to_write)
my_file.close()
```


<aside class="notes">

**Teaching Tips**:

- Demo this!

</aside>

---

## We Do: Creating Files

What if the file doesn't exist yet?

**Write** to the rescue!

* Write opens a file for writing...
* But it also creates it if need be!

At the bottom of your script, add:

```python
# Open OR create file totally_new_file.txt
my_new_file = open("totally_new_file.txt", "w")

# Write some content to totally_new_file.txt
my_new_file.write("Content goes here")

# Always close the file
my_new_file.close()
```

Check your desktop after running it!


<aside class="notes">

**Teaching Tips**:

- Do this with them.
- Make sure they have all successfully run the code.

</aside>

---

## You Do: Create a File

Now, try it yourself. Write a new script:

- `open()`, in read mode, your existing `a_file.txt`.
- `.read()` the file and save the contents into a variable, `file_contents`.
- Using `.write()`, create a new file called `b_file.txt`.
- Write `file_contents` to `b_file.txt`.

Don't forget to `close()` your files!

<aside class="notes">

3 minutes

</aside>

---

## Create a File: Solution

```python
my_file = open("a_file.txt", "r")
file_contents = my_file.read()
my_file.close()

my_file_script = open("b_file.txt", "w")
my_file_script.write(file_contents)
my_file_script.close()
```

<aside class="notes">
**Teaching Tips**:

- After they do this, show it to them. Show them opening multiple files at the top, too, so they know you don't have to go sequentially: e.g.

```python
file_to_read = open("a_file.txt")
file_to_write = open("b_file.txt", "w")


file_contents = file_to_read.read()
file_to_write.write(file_contents)

file_to_read.close()
file_to_write.close()
```
</aside>

---

## Quick Review

You can open, read, and write files with Python.

Write will create the file if it doesn't already exist.

Always close your files!

```python
file_to_read = open("a_file.txt")
file_to_write = open("my_file_script.txt", "w")


string_to_write = file_to_read.read()
file_to_write.write(string_to_write)

file_to_read.close()
file_to_write.close()
```

**Next up:** More advanced file options.

<aside class="notes">

**Teaching Tips**:

- Do a quick check for understanding.

</aside>

---

## Other File Modes

What if we want to read AND write a file? Or write to the end of a file instead of overwriting what's there?

`open` has a few other modes.

| Value | Mode | Purpose |
| ----- | ------------ | -------------- |
| `r` | Reading | Read only. The default! |
| `w` | Write | Use to change (and create) file contents |
| `a` | Append | Use to write to the end of a file |
| `r+` | Read Plus | Can do both read and write |


> Don't memorize this; just know it's there. A lot of programming is understanding your options and then Googling the syntax! The biggest thing for you to learn is the concepts that Python can do.

<aside class="notes">

**Teaching Tips**:

- Stress that this is a lot to take in and they don't need to remember it all. We're practicing for their understanding, not their memorization. (Also, the more we practice, the more likely they'll just remember it).

- Show `r+` and `a`. You can work off this basic code:

```python
# Open the file hello.txt
my_file = open("hello.txt", "w")
my_file.read() # Error! Not readable.
my_file.write("hey")
# Close the file
my_file.close()
```

</aside>

---


## I Do: The With Keyword

Always remembering to close a file can be hard.  There's another way to open files so Python closes it for us!

```python
# Instead of:
file_object = open("my_file.txt", "w")
file_object.write("Hello World!")
file_object.close()

# We can say:
with open("my_file.txt", "w") as file_object: # This line replaces the open and close above
  file_object.write("Hello World!") # This line is the same; note the indent!
````


<aside class="notes">
**Talking Points**:

* As you can see, file I/O is associated with a lot of potential errors.
* Sometimes if a file doesn't close properly, this can lead to:
    * Memory pollution on your computer
    * Keeping a file in use when it isn't
* These are bad problems! Luckily, Python has our back once again with `with`!
* `With` shortens our code, catches errors gracefully, and makes `close` unnecessary.

**Teaching Tips**:

It's not necessary they become experts in this. Just show it to them so that they're aware if they  find  it in a tutorial.
Here is a repl.it, if you'd like:
https://repl.it/@GAcoding/03-Python-Scripting-03
</aside>

---

## What Else is in File?

These are just for reference - we won't be using them!

- Do you have a list that you want to write on multiple lines? Use `my_file.writelines([<your list>])`

- Does your file have things on multiple lines you want to read into a list variable? Use `list_contents = my_file.readlines()`

- Separating some written lines? Add `\n` to the `write()`

<aside class="notes">
**Teaching Tips**:

- If you have time (remember, user input is still coming), open a file and show these in action.
- It's not essential for students to know, but it's good for them to see.
- Skim this slide quickly if students are starting  to look lost.

Here is a repl.it, if you'd like:
https://repl.it/@GAcoding/03-Python-Scripting-01
</aside>

---

## Quick Review:

File has a lot of advanced options.

- You can write a list across multiple lines, or read a file with multiple lines into a list variable.
- Write only takes one argument, so concat your strings!
- You can open files using `with` to automatically close them.

```python
# Instead of:
file_object = open("my_file.txt", "w")
file_object.write("Hello World!")
file_object.close()

# We can say:
with open("my_file.txt", "w") as file_object: # This line replaces the open and close above
  file_object.write("Hello World!") # This line is the same; note the indent!
````

**Next up:** User Input!

---

## What about User Input?

We've just done a lot with file I/O (in/out).

We can prompt users for information, too.

You've seen this a few times (remember the error checking, with the try/catch?)! It's very common.

```python
# Prompts with "input"
# Saves result in user_name
user_name = input("Please type your name:")
```

<aside class="notes">
**Teaching Tips**:

- Run this! Show this a few ways. Try type casting the input to an int.

Here's a repl.it, if you'd like:
https://repl.it/@GAcoding/03-Python-Scripting-04
</aside>
---

## You Do: Bring it all Together!

1. Create a file called `about_script.py`.
2. In it, prompt the user for their name. Then, prompt them for their favorite food.
3. Using write, create a file called `about_me.txt`.
3. In `about_me.txt`, write out the name and favorite food in a sentence.

**Bonus**: Use `format` for forming your sentence!


<aside class="notes">
5 minutes

**Teaching Tips**:

- After students give this a shot, show the answer (next slide).
- If there's still time, show a few variations of this with other things we've covered, like append and `with` to open.
</aside>

---

## Bring it all Together, Solution

```python
user_name = input("Please type your name: ")
user_food = input("Please type your favorite food: ")

file = open("about_me.txt", "w")
file.write("My name is " + user_name +  " and my favorite food is " +  user_food)
```

---

## Summary and Q&A

Scripting language vs compiled language.

- Scripting languages: Write -> Run.
- Compiled languages: Write -> Build -> Run.

Script:

- Just some code!

---

## Summary and Q&A

File I/O:

- `my_file = open("a_file.txt", "w")`
- `my_file.write("Some content")`
- `my_file.write(my_text)`
- `my_file.close()`

User input

- `user_name = input("Please type your name:")`


<aside class="notes">

**Teaching Tips**:

- Check for understanding; review key concepts.

**Talking Points**:

*We accomplished quite a bit!*

* Defined what a script means contextually.
* Showed how to open and close a file on your computer.
* Discussed different modes of opening files.
* Wrote a script that accepted a user's input
</aside>

---

## Additional Resources

* [Socratica Video: Text Files](https://www.youtube.com/watch?v=H_R5yRtFtuc)
* [Executing a Python Script](https://www.python-course.eu/python3_execute_script.php)
* [Reading and Writing Files](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)
* [File Object Documentation](https://www.tutorialspoint.com/python3/python_files_io.htm)
* [Binary vs Text Files](https://www.nayuki.io/page/what-are-binary-and-text-files)
