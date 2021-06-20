<!--
title: Running Python on Your Computer
type: lesson
duration: "01:00"
creator: Brandi Butler
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Running Python on Your Computer</h1>


<!--

## Overview
This lesson gets students set up and comfortable working with Python on their local environment by running `python3 file_name.py` from their command prompt. After installing Python 3 and Atom, they'll run through a few practice scripts they've already seen to get used to editing files locally.

## Important Notes or Prerequisites
- At the point you give this lesson, students are getting their very first introduction to writing code. Don't assume they know anything! Be sure to explain carefully whenever you change even a little thing.
- Encourage students to type, not copy and paste, for practice. Whenever possible, have students try to guess what will happen and try it out in the slide.
- Note: If the code is too long for students to easily see in the embedded slide, there's an "open with repl.it" icon in the top right of the embed that will open the repl.it in a new, larger window.

## Learning Objectives
In this lesson, students will:
- Install Python 3.
- Write Python 3 scripts locally.
- Run Python 3 scripts via the command prompt.

## Duration
20 minutes

## Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:01 | Welcome
| 0:02 - 0:14 | Installfest](#activity-installfest-12-min
| 0:15 - 0:19 | Running Local Files
| 0:19 - 0:20 | Summary

## Before Class: Preparation

- Change the location of the installation directions.

- **IMPORTANT:** Watch the clock! There may be a couple students with a slow computer. We can't have everyone wait on them, so make sure that you cut this activity off at the time limit! Follow up with those students at lunch.

- In advance, check if students will run the code with `python3 file.py` or `python.py`. The later lesson slides usually have `python.py` in their You Do instructions. Have students adjust accordingly.

## In Class: Materials
- Projector
- Internet connection
- Python 3.0
- Installation directions

-->

---

## Lesson Objectives
*After this lesson, you will be able to…*

- Write Python 3 scripts locally.
- Run Python 3 scripts via the command prompt.

---

## Defining Assumptions


We can't use repl.it forever! We can run Python right on our computers.

* GA uses Macs for its default curriculum.
* We are happy to help you program Python on Windows or Linux as well.
* Sometimes you may need to ask questions about subtle differences!

<aside class="notes">

**Teaching Tips:**

- Make sure students are aware that GA uses Macs as a default, but that you have directions for installing and can provide guidance on Linux and Windows as well.

</aside>

---

## Let's Get Installing!


This will take us 10 to 15 minutes, then we'll regroup.

First, install Atom from <a href="https://atom.io/">https://atom.io/</a>. This is where you'll write your code.

Then, follow the [Python 3 installation directions](python3-installation-directions.md.html).

<aside class="notes">

**Teaching Tips:**

- Students can use a different text editor if you or they prefer, but any reference to a text editor throughout this course is "Atom."

- Point a link to where the directions are, or, if students downloaded them as a PDF, point out which PDF.

- You may have to cut off a student who is taking way too long to do this. It really isn't fair to make everyone else wait in this case. Reassure the student that you will follow up with them during lunch or a break. Meanwhile, they should continue to use the website repl.it.

</aside>

---

## Regroup

* You have Python 3 installed!
* You may have seen the in-line REPL (we'll revisit!).
* You have a text editor — Atom — installed.
* You are ready to create a local `.py` file and run it.

<aside class="notes">

**Teaching Tips:**

- Make sure everyone has either installed Python 3 or knows that it's shelved until lunch.
- Make sure everyone has downloaded and can open the Atom text editor.

</aside>


---

## In-Line REPL

Let's check out a REPL.

- `Read-Evaluate-Print-Loop`.
- An interactive way to code.

Let's do it!

* Open your terminal.
* Then, open your in-line REPL:

Mac/Linux:
```
python
```

Windows:
```
py
```

<aside class="notes">

**Teaching Tips:**

- This seems simple, but go slowly.
- Some students might need `ipython`, not just `python`, or even `python3` — walk around and make sure they have it.

</aside>

---

## We Do: Interactive Development

You can type any Python code you want here. Let's declare a variable and do some math:

```python
x = 4
y = 5
print(x + y)
```

> **Pro tip:** `exit()` is the command for when you want to get out of this environment!

<aside class="notes">

**Teaching Tips:**

- Have everyone practice this with you.
- Practice `exit` as well.
- Some students might need `exit`, not `exit()` — walk around and make sure they have it.

Talking Points:

- "You're running Python locally!"

</aside>

---

## We Do: Local Files

We can create a file with a `.py` extension — we can execute properly written Python code in a `.py` file.

1. Create a new file with a `.py` extension. Let's call it `my_file.py`.
2. Open `my_file.py` in `Atom`.
3. In this file, declare some variables. Let's mix integers and strings!

```python
favorite_tv_show = "Ninja Warrior"
obstacles_cleared = 5
time = "3 min, 20 sec"
print("I cleared", obstacles_cleared, "on", favorite_tv_show, "in", time)
```

Save and close your file.

> **Pro tip:** Make sure you have a `print` statement.


<aside class="notes">

**Teaching Tips:**

- Have everyone practice this with you. We want them to be able to run local code on their own.

</aside>


---

## We Do: Running Local Files

Now we have code in a file, but we need to run it.

* Back on your terminal, we'll navigate to where that file is located:

    * `cd` stands for "change directory" ("directory" is another word for "folder").
    * `cd my_folder` changes to the directory `my_directory`.
    * `cd ..` goes up to the parent folder of the one you're in.

* Running the file varies slightly between Windows and Mac/Linux:

    * Mac/Linux: `python my_file.py`
    * Windows: `py my_file.py`

Raise your hand if you need help!


<aside class="notes">

**Teaching Tips:**

- Students have probably never seen a command line before this presentation. Show them how to do it, then walk around and make sure everyone is clear.

</aside>


---

## Summary

* We now have Python 3 — the latest and greatest — installed.
* We can use our in-line REPL in the terminal.
* We can execute a local `.py` file with Python code in it.
* We know how to do this regardless of whether we use Mac, Linux, or Windows.

> Any questions?

<aside class="notes">

**Teaching Tips:**

- If students seem a bit lost and there's time, have them keep practicing this. Consider giving different tasks for them to perform in the REPL and the `.py`, and be clear about the difference between the two.

</aside>


---

## Additional Resources

* [Linux Command Line Cheat Sheet](https://www.cheatography.com/davechild/cheat-sheets/linux-command-line/)
* [Mac Command Line Cheat Sheet](https://www.git-tower.com/blog/command-line-cheat-sheet/)
* [Windows Command Line Cheat Sheet](https://gist.github.com/Gmanweb/c18785da8b34fab800a3)

<aside class="notes">

**Teaching Tips:**

- Encourage students to go through these in their spare time if they're curious.

</aside>
