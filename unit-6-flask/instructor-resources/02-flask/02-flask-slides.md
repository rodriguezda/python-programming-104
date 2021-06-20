<!--
---
title: Python Basics: Intro to Python Web Development
type: lesson
duration: “:60”
creator: Anna Zucher + Susi Remondi
---
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Intro to Flask</h1>

<!--

## Overview
We're introducing Flask. After a brief introduction, we jump into a We Do that walks students through running a basic Flask app. Near the end, there's a slide on the history of Flask.

## Important Notes or Prerequisites
- Make sure you have Flask installed!

## Learning Objectives
In this lesson, students will:
- Write a basic Flask application.

## Duration
30 minutes

#### Notes on timing:
- This seems like a long time, but spend time on each slide going through variations of what can be written, whether it's a variable name or the return. Be sure everyone has a basic Flask app at the end.

---

## Suggested Agenda

| Time | Activity | Purpose |
| --- | --- | --- |
| 0:00 - 0:02 | Welcome |
| 0:02 - 0:07 | Flask Introduction |
| 0:07 - 0:25 | Building a Flask App |
| 0:25 - 0:28 | History |
| 0:28 - 0:30 | Summary |


## Differentiation and Extensions
- Feel free to come up with a few different things for the Flask app to display — more complex code between the `index` declaration and the `return`. Give advanced students more challenges to bring in dictionaries, lists, or loops.


Materials needed:
- Projector
- Slides
- Python 3
- Flask

-->

---

## Learning Objectives:
*After this lesson, you will be able to:*

- Write a basic Flask application.
    - Note to instructor: If you are running this in a Jupyter Notebook,
        please see the speaker notes of this slide for necessary
        changes.

<aside class="notes">

**Jupyter Notebook Specific Notes:**

- When running the flask application in a jupyter notebook, note that the
    execution of process, app.run(), will occupy the kernel and no other
    commands passed to the notebook will be processed until this thread
    is terminated. Any debug output from the app.run() process will be
    written to the stdout(), which is the normal 'cell output' area.
- Running app.run() with a kwarg of 'debug=True' yielded a port in use
    exception during testing. The root cause wasn't investigated,
    however this error can be avoided by omitting the kwarg entirely (it
    has a default value of False), or explicitly setting it to False.
- The default port of 5000 may conflict with other applications (such as npm
    defaults). Use the 'port=' kwarg in app.run() to set to an unused port.
    Note that local admin permissions will be needed for port numebers
    <= 1024.
- Setting of the host kwarg in app.run() can also be used to limit
    incoming connections (for example, host=127.0.0.1 to limit to loopback
    only instead of the default 0.0.0.0).
- The 'render_template' Flask function appears to _only_ be able to
    reference templates in the './templates' directory relative to the path
    the 'app.run()' is instantiated from. Passing an argument of
    './index.html' will yield a file not found error. The html file must be
    placed into './templates', with an argument of 'index.html' passed to
    'render_template' (with no relative path reference).
</aside>

---

## Discussion: Commonalities


What do you think these websites have in common?

- [Pinterest](http://www.pinterest.com)
- [Instagram](http://www.instagram.com)
- [LinkedIn](http://linkedin.com/)

They're each:

- High on user interactivity.
- Handling a large server load.

What else?


<aside class="notes">

**Teaching Tips:**

- Try to lead them toward the idea of a Python web framework module.
- A large server load means lots of images to download and lots of actions on the part of each user.
- Show LinkedIn and Pinterest if the students aren't familiar. Get them excited!
</aside>

---

## They All Use **Flask**


![](https://qph.fs.quoracdn.net/main-qimg-cd83cf9ee7ad51b8af4d0c4d5220f534.webp)

Some quick notes about Flask:

- It's a Python micro web framework.
- It can create and write the entire back-end in Python!
- It can do small tasks (e.g., create a microblog or stand up a simple API).
- It can do complex tasks (e.g., Pinterest's API or create a Twitter clone).


<aside class="notes">

**Talking Points:**

- Flask is classified as a microframework because it does not require particular tools or libraries.
- Open the lesson by describing what students are going to do (build a Flask app), and why this is so exciting ("We are using Flask to actually put your stuff on the internet!").
- Why do we use a lighter web framework like Flask?
- Talk about how these sites work (lots of interaction and data) and why it is helpful to use Flask for these (get to focus on the interactivity/data and not just getting the thing up on to the internet and staying there).

</aside>

---

## Flask Syntax

How?

We just make a normal Python app.

It looks like:

```python
# Import Flask class from flask library. (Note the upper/lowercase convention.)
from flask import Flask

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
# Could be instead "my-website.com/about" or anything - more on this later.
@app.route('/')

# Function that returns the page: Display "Hello, World!"
def index():
  return 'Hello, World!'

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)

```


<aside class="notes">


**Teaching Tips:**

- Walk through this line by line.
- The code includes comments for students' reference, but be sure to still talk through it. There's a lot more to say than what's written!
- Give URL examples — pull up websites.

**Talking Points:**

*<Note: This is copied from the Flask docs.>*

- First we imported the Flask class.
- Next, we create an instance of this class. We use `__name__` so that Flask knows where to look for templates, static files, and so on.
- We then use the `route()` decorator to tell Flask what URL should trigger our function.
- The function is given a name, which is also used to generate URLs for that particular function and returns the message we want to display in the user’s browser.

</aside>

---

## We Do: Let's Try!

We'll run the Flask app like any other app.

- We need to install Flask!
  - `pip install flask`

Create a file called `my_website.py`.

Start with:

```python
# Import Flask class from flask library.
from flask import Flask
```


<aside class="notes">

**Talking Points:**

- Flask (and lots of web frameworks) can be launched on the command line, giving developers more control and clarity into what is going on.
- Set global variable (so Flask knows where our main application logic lives).

**Teaching Tips:**

- Make sure everyone has done these steps!
- If there are difficulties with `pip`, check `sudo`.
- Demo these so students have the idea, then let them experiment on their own.
- For more advanced students, write longer scripts in the `index()` function, or, if time, assign them the task.
</aside>

---

## We Do: The Main Flask App

Let's add:

```python
# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
@app.route('/')

# Function that returns the page: Display "Hello, World!"
def index():
  return 'Hello, World!'

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)
```


<aside class="notes">

**Teaching Tip:**

- Continuously walk through the code.
</aside>


---

## We Do: Flask App — Try it!

Run the app like normal:

`python my_website.py`

Go to:

`http://localhost:5000/`

You made a web app!

Let's change the string:

```python
def index():
  # The "return" determines what's displayed.
  return 'Hello, World!'
```


<aside class="notes">

**Teaching Tip:**

- Change around what's returned in `index()`, so they can see that that's what makes the display.

</aside>

---


## I Do: Displaying the App

It's just Python — we can write any code.

- But `return` essentially just takes strings.

```python
def index():
  my_list = ["Hey", "check", "this", "out"]
  return my_list[0] # Works!
```

Conversely:

```python
def index():
  my_list = ["Hey", "check", "this", "out"]
  return my_list # WON'T WORK
```


<aside class="notes">

**Teaching Tips:**

- Change around what's returned in `index()` in a more advanced way.
- They can follow along if they'd like.
</aside>


---

## We Do: Flask Variations

`app` and `index` are just naming conventions.

- `def index():` could be `def monkey():`.
- `app` could be `guitar`.
    - Be sure to change it in all places!

But, naming variables sensibly is important!

```python
from flask import Flask

guitar = Flask(__name__)
@guitar.route('/')

def monkey():
  return 'Hello, World!'

if __name__ == '__main__':
    guitar.run(debug=True)
```


<aside class="notes">

**Teaching Tip:**

- Show this.
</aside>


---

## Flask History

Let's back up. Where did Flask come from?

- Before 2010:
    - No easy method for Python websites.
- 2010:
    - A few developers built Flask to fix this.

Flask is built on two libraries:

- *Werkzeug*:
    - Interfaces with the web.
    - Helps handle request and connections.
- *Jinja*:
    - We'll be using this later!
    - We can write templates for all pages across our web app.


<aside class="notes">

**Teaching Tips:**
- Some students might not care about history, but go over it for those who do.
- Don't spend too much time on the libraries — we're hitting Jinja later!

**Talking Points:**

* Around 2010, a group of open-source Python developers release the first version of Flask!.
* Before this, there was no easy way to use Python on the internet/for web apps.
* Flask is built using two libraries (already written bundles of code).
1. *Werkzeug* is a library to interface with the web. It helps to handle request and connections.
2. *Jinja* is a templating engine, which lets us write an HTML file once and then apply that file to all of our site.
</aside>


---

## Summary: Flask

- A Python micro web framework
- Developed in 2010

Looks like this:
```python
# Import Flask class from flask library.
from flask import Flask

# Initialize an instance of the Flask class.
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
@app.route('/')

# Function that returns the page: Display "Hello, World!"
def index():
  return 'Hello, World!'

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)
```

<aside class="notes">

**Teaching Tip:**

- Be sure everyone has a basic Flask app at the end and understands why.
</aside>

---

## Additional Reading

- [Flask Documentation](http://flask.pocoo.org/docs/0.11/)
- [A Flask Tutorial to Follow Along With](https://github.com/miguelgrinberg/flask-pycon2014)
- [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- [A Great Guide to Those Weird "Decorators"](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
