<!--
title: Variables and Routing in Flask
type: lesson
duration: "01:00"
creator: Kevin Coyle
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Variables and Routing in Flask</h1>

---

## Learning Objectives
*After this lesson, you will be able to:*

- Display variables on a webpage.
- Create a route in Flask.

---

## Multiple Routes

<aside class="notes">

**Talking Points:**

- One of the things that makes Python so fantastic is that it is object-oriented.
- Assigning variables turns them into a type of object — with an object, we can do some awesome things.
- We're going to look at variables in our Flask app. Creating variables allows us to return values of those variables, as well as provides us with all the methods and attributes in that type of object.
- Routes allow us to extend this a step further — we can take variables and put them into our URL, which we can then use to render some data on the page.
</aside>

- Our website is cool, but it's just one page.
- What about recipe pages? "About" pages?
- We need to use `routes`.

But first, we need to learn `variables`.

---

## Variables? Again?


- Yes! Regular variables.

	`x = "this string"`

- Difference: Here, we're in the Flask app.

- Very specific use cases:

	- Routes (We're learning now.)
	- Templates (We'll learn next.)
	- Requests (We'll learn later.)

<aside class="notes">

**Talking Points:**

 - When we're talking about variables here, we're talking about the same thing as variables in base Python.
 - You assign a variable to a value and that value gets stored in memory.
 - We'll go over some common use cases for including variables in your Flask app.
 - Note, however, that using variables in templates and requests will be covered in a later lesson.

</aside>

---

## Three Ways to Read in a Variable

<aside class="notes">

**Talking Points:**

- There are several ways to obtain the value for a variable.
- Depending on that value and what it represents, there are different ways of going about entering that into our Flask app.
- The first is to have the variable assignment take place right in our Flask app.
- Another is to read it from a Python script, like you would for any other library.
- Yet another is to read it in from a file, unlike you would import any library.
</aside>

Variables come from:

- Within our Flask app.
- From another Python file.
- From any other file.

---

## Method 1: Set Variables in Our Flask App

<aside class="notes">

**Talking Points:**

- The easiest way to obtain a value from a variable in Flask is to assign it directly in your Flask app.
- This makes sense if we are only trying to output a very small amount of information.
- Consider the following modification on our `Hello World` app.
</aside>

These *aren't* set inside `def hello()`.

- What does that make them?

`hello_variables.py`

```python
from flask import Flask

app = Flask(__name__)

my_job_title = "Python pro"

@app.route('/')
def hello():
	return "Hello, " + my_job_title

if __name__ == '__main__':
	app.run(debug=True)
```

---

## We Do: In-App Variables

- We can practice this: In your existing `my_website.py`, comment out the `return render_template("index.html")`.

Instead, have:

```python
my_job_title = "Python pro"

@app.route('/')
def home():
	return "Hello, " + my_job_title
```

<aside class="notes">
**Current Code Status**:

The code could look like this now:

```python
from flask import Flask, render_template
app = Flask(__name__)

my_job_title = "Python pro"

@app.route('/')
def home():
	return "Hello, " + my_job_title

def hello_world():
    line1 = "<h1><b>Hello</b> World!</h1>"
    line2 = "<p>If music be the food of love, play on!</p>"
    line3 = "<img src='https://media.giphy.com/media/sWrDT2OqxJ3Fu/giphy.gif'>"
    total = line1 + line2 + line3
    # return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)
```
</aside>
---

## Method 2: Read Variables From a Python File

<aside class="notes">

**Talking Points:**

- The next way to read in a variable is to assign it in a Python file, then import that file.
- This is considered the most "pythonic" way to read variables into other Python files.
- In order to use this approach, you need another file that ends in `.py`.
- You then read this file into your Flask app with an `import <myFile>`.
</aside>

- You're never limited to just one `.py` file!

- New Python file: `mySecrets.py`

```python
username = "Guy Fieri"
password = "flavortown"
```

How would we print that in our Flask app?

Any ideas?

---

## We Can Import the File

Your normal Flask app:

```python
from flask import Flask
import mySecrets ## You can import any file!

app = Flask(__name__)

## Call it like a module.
my_name = mySecrets.username
my_password = mySecrets.password

@app.route('/')
def hello():
	return "Hello, " + my_name + ", welcome to " + my_password

if __name__ == '__main__':
	app.run(debug=True)
```

---

## Method 2: Use Cases

<aside class="notes">

**Talking Points:**

- A great use case for this is when you'd like to have your secret info (tokens, passwords, etc.) in a file that isn't your Flask app.
- When you push your code to GitHub, you can then have your Flask app open for the world to see, and your passwords safely in a file on your local drive.
- Another use case is file management. Pretend you have a lot of variables that may not make it into every file, but you want a "master file" from which to read all these variables.
</aside>

Why?

- You have secret info (tokens, passwords, etc.) — keep them locally!
- You have many Flask pages, so you make a "master file" to hold all variables.

---


## Your Turn: Another `py` File

Now it's your turn!

- Make a file called `python_variables.py` in the same folder as `my_website.py`.
- Insert some variables into `python_variables.py` - perhaps some books you like.
- Import `python_variables` into your Flask app, `my_website.py`.
- Display the values from `python_variables` in your Flask app.

---

## Method 3: Reading From a Non-Python File

<aside class="notes">

- Yet another way to read variables in is in non-Python files.
- Not all data/info you'll need will be in a static Python file.
- This approach is a combo of one of the earlier two approaches.
- Pretend say you have another file that's a .txt file.
- We can do two things:
  - Read that .txt file in directly in our Flask app and set that to a variable (like Approach 1).
  - Read that .txt in with another file and save that to a variable which your Flask app reads (like Approach 2).
    - Here, we take Approach 1. First, though, we create a .txt file.
    - Then, we open it with `os` and `file open`.
    - Then, we set that .txt to a variable and print that variable in our `route()` function.
</aside>

Let's create a `.txt` file called `hi.txt` in the same folder where our app lives. We'll include some Shakespeare poetry.

```
So are you to my thoughts as food to life,
Or as sweet-seasoned showers are to the ground;
```

How do you think we get this into our Flask app?

---

## With File Open

Then, we'll add a bit in our Flask app:

```python
import os # Note the new import — to be in the file system.

file_path = '.'
# Note the "with"! We don't need "close".
with open(os.path.join(file_path, 'hi.txt')) as f:
    the_text = f.read()

@app.route('/text')
def read_txt():
	return the_text

```

---

## You Do: Add a `.txt` File

Now it's your turn!

- Make a file called `more_variables.txt` in the same folder as `my_website.py`.
- Write some information into `more_variables.txt` — perhaps what you'd like for breakfast tomorrow.
- `import os` so you can find the file.
- Use this code:

```python
with open(os.path.join(file_path, 'more_variables.txt')) as f:
	the_text = f.read()
```

- Display the text from `more_variables` in your Flask app.

<aside class="notes">

**Current Code Status**:
Possible solution code:

```python
from flask import Flask
import mySecrets ## You can import any file!
import python_variables
import os # Note the new import — to be in the file system.

app = Flask(__name__)

## Call it like a module.
my_name = mySecrets.username
my_password = mySecrets.password

student_name = python_variables.student_name

file_path = '.'

with open(os.path.join(file_path, 'more_variables.txt')) as f:
	the_text = f.read()

@app.route('/text')
def read_txt():
	return the_text

@app.route('/')
def hello():
	return "Hello, " + my_name + ", welcome to " + my_password + ". You are " + student_name + ". More variables are: " + the_text

if __name__ == '__main__':
	app.run(debug=True)

```


---

## Knowledge Check

What are the three approaches to read in variables to a Flask app?

<aside class="notes">

**Teaching Tip:**

- Answer: Reading directly in our Flask app, from a Python file and importing, and from a non-Python file.
</aside>

---

## Part 2. Routing {.separator}

---

## What Is That `@app.route('/')`, Anyway?

<aside class="notes">

**Talking Points:**
- By now, you may be wondering about that `@app` that we keep putting on the line before our function.
  - `@` is a way to use a "decorator."
  - A decorator is a way to put one Python function into another Python function.
  - More formally, this process is called "wrapping a function" inside of another function.
  - You can check out more on decorators later, but for now, knowing that our `@app.route(endpoint)` is a way that we pass an argument — the endpoint — into a routing function.
  - In other words: We tell our Flask app to listen to a particular endpoint and then we have a function that happens if that endpoint gets hit.
</aside>

We have:

- Listen to an endpoint (here, `/`).
- Do `def home()` if someone goes there.

```python
@app.route('/') # When someone goes here...
def home(): # Do this.
  return render_template("index.html")
```

`http://127.0.0.1:5000/`
`=> render_template("index.html")"`

What if we want to go to `http://127.0.0.1:5000/sayHi`?

---

## Suddenly, a New Page!

- This is **routing**.
- New pages on our web app!

```python
@app.route('/sayHi') # When someone goes here...
def hello(): # Do this.
	return "Hello, Mr. Fieri."
```

---

## We Do: Add a Route

- In `my_website.py`, under `def home()`, add:

	```python
	@app.route('/sayHi') # When someone goes here...
	def hello(): # Do this.
		return "Hello, Mr. Fieri."
	```
- Reload the page! Go to `http://127.0.0.1:5000/sayHi`.

<aside class="notes">
**Current Code Status**:
Possible code:

```python
from flask import Flask, render_template
import mySecrets ## You can import any file!
import python_variables
import os # Note the new import — to be in the file system.

app = Flask(__name__)

## Call it like a module.
my_name = mySecrets.username
my_password = mySecrets.password

student_name = python_variables.student_name

file_path = '.'

with open(os.path.join(file_path, 'more_variables.txt')) as f:
	the_text = f.read()

@app.route('/text')
def read_txt():
	return the_text

@app.route('/') # When someone goes here...
def home(): # Do this.
    return render_template("index.html")

@app.route('/sayHi') # When someone goes here...
def hello(): # Do this.
    return "Hello, Mr. Fieri."


if __name__ == '__main__':
	app.run(debug=True)


```

---


## What Is a Route?

<aside class="notes">

**Talking Points:**

- A route in our context here consists of our `localhost:5000`, as well as the rest of our URL.
- We pass the rest of our endpoint into our `app.route()` function as an argument.
- This means everything inside of the parentheses and inside of quotes becomes our URL.
</aside>

- The URL: `http://127.0.0.1:5000/sayHi`
- We *route* to different URLs:
	- `http://127.0.0.1:5000/sayHi`
	- `http://127.0.0.1:5000/Cats`
	- `http://127.0.0.1:5000/profile`

- `sayHi`, `Cats`, `/`, and `profile` are **endpoints** from our main app.

- We only need to add:

	```python
	@app.route('/<endpoint>') # When someone goes here...
	def function_name(): # Do this.
		return string
	```

---

## You Do: Adding a Route

- In `my_website.py`, add a new route to a `randnum` endpoint.
- In the function for this endpoint, display a string that's a random number.
	- *Hint:* Remember the `random` module? You can use `randint(1, 100)`.
	- *Hint:* You can turn an integer to a string with `str(number)`.

- Reload the page and go to your endpoint to try it out!


<aside class="notes">
**Current Code Status**:

```python
from flask import Flask, render_template
import mySecrets ## You can import any file!
import python_variables
import os # Note the new import — to be in the file system.
import random

app = Flask(__name__)

## Call it like a module.
my_name = mySecrets.username
my_password = mySecrets.password

student_name = python_variables.student_name

file_path = '.'

with open(os.path.join(file_path, 'more_variables.txt')) as f:
	the_text = f.read()

@app.route('/text')
def read_txt():
	return the_text

@app.route('/') # When someone goes here...
def home(): # Do this.
    return render_template("index.html")

@app.route('/sayHi') # When someone goes here...
def hello(): # Do this.
    return "Hello, Mr. Fieri."

@app.route('/randnum')
def randnum():
    return str(random.randint(1, 100))

if __name__ == '__main__':
	app.run(debug=True)


```
---


## Variables in the Route

<aside class="notes">

**Talking Points:**

- OK, so I said these are two separate concepts, but that's only halfway true.
- We can actually assign values in the URL to into variables in our Flask app.
- Why would we do this? Because we can change the URL to reflect what sort of data we wish to see.
- In the code snippet you see here: We are assigning the name variable to a value, which we insert into our function and then return to the user, in the middle of a sentence.
</aside>

- You can pass a variable in the route itself.
- It's a dynamic endpoint!
- You can use that variable in your function.

```python
@app.route('/sayHi/<name>')
def hello(name):
	return "Hello, " + name + ", your coding skills impress me!"
```

`http://localhost:5000/sayHi/Hari`
`=> Hello, Hari, your coding skills impress me!"`


<aside class="notes">
**Current Code Status**:

```python
from flask import Flask, render_template
import mySecrets ## You can import any file!
import python_variables
import os # Note the new import — to be in the file system.
import random

app = Flask(__name__)

## Call it like a module.
my_name = mySecrets.username
my_password = mySecrets.password

student_name = python_variables.student_name

file_path = '.'

with open(os.path.join(file_path, 'more_variables.txt')) as f:
	the_text = f.read()

@app.route('/text')
def read_txt():
	return the_text

@app.route('/') # When someone goes here...
def home(): # Do this.
    return render_template("index.html")

@app.route('/sayHi/<name>')
def hello(name):
	return "Hello, " + name + ", your coding skills impress me!"

@app.route('/randnum')
def randnum():
    return str(random.randint(1, 100))

if __name__ == '__main__':
	app.run(debug=True)
```

---

## Your Turn!

Try adding route in your Flask app to have:

- A `/timesfour/<number>` route that displays the product of an integer in the route multiplied by four.
- A `repeat` route that takes a string passed into the URL, then displays it four times in a row.

---

## Final Code Status

Your code should look similar to this:

```python
from flask import Flask, render_template
import mySecrets ## You can import any file!
import python_variables
import os # Note the new import — to be in the file system.
import random

app = Flask(__name__)

## Call it like a module.
my_name = mySecrets.username
my_password = mySecrets.password

student_name = python_variables.student_name

file_path = '.'

with open(os.path.join(file_path, 'more_variables.txt')) as f:
	the_text = f.read()

@app.route('/text')
def read_txt():
	return the_text

@app.route('/') # When someone goes here...
def home(): # Do this.
    return render_template("index.html")

@app.route('/sayHi/<name>')
def hello(name):
	return "Hello, " + name + ", your coding skills impress me!"

@app.route('/timesfour/<number>')
def timesfour(number):
    return str(int(number) * 4)

@app.route('/repeat/<number>')
def repeat(number):
    return number * 4

if __name__ == '__main__':
	app.run(debug=True)
```

---

## Summary

We covered variables and routing in Flask:

- Variables can be made:
	- In the Flask app: Used like normal variables.
	- In a Python file: Imported like a module.
	- In another file: Used `file` to read it.

- Routing:
	- `@app.route(<endpoint>)` is how we make new pages in our app!
