<!--
title: Next Steps in Web Development
type: lesson
duration: "01:00"
creator: Kevin Coyle
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Templates</h1>

---

## Learning Objectives
*After this lesson, you will be able to:*

- Create a template HTML document.
- Pass variables to a template HTML document via a Flask app.

---

## A Million Copies

- Don't you hate it when you have to repeat yourself?

- What if you had a website with 10 pages that were almost the same?

- Would you code them all from scratch?

---

## We Do: Your `index.html` Page

- Any route can use an `html` page.

- Try it!
	- In your `my_website.py`, set the `/randnum/<inte>` and `/` routes to both `render_template("index.html")`.

- What if we want them to display a different heading?
- Do we need to rewrite the whole file?

---

## No! That's What Templates Are For!

<aside class="notes">

**Teaching Tip:**

- Talk for a few minutes here about design patterns and why it's important to split data from presentation.
</aside>

We use templates to:

- Write one HTML file.
- Pass it variables.
- Transfer info from Flask to HTML.

As well as for one important design reason:

- We can separate data from how we present data to users.

---

## Jinja2

- One of the most widely used template engines for Python.
- Used in places that you might have visited already, like Instagram or NPR.

---

## Why Jinja2?

<aside class="notes">

**Talking Points:**

- Jinja2 is kind of like the engine that powers our vehicle (Flask). However, this happens behind the scenes.
- We're quickly peering behind the scenes to get an idea of what our engine can do.

- Some examples of what makes Jinja2 awesome are:
  - **Template inheritance:** You can extend templates in very efficient ways.
  - **HTML escaping:** Malicious hackers can create XSS attacks by injecting HTML code into our site where other users insert data. Jinja2 helps us avoid that.
  - **Speed and efficiency:** Jinja2 is very fast. It compiles optimized Python code.
  - **Flexibility and extensibility:** It's really easy to add our own filters and functions.
</aside>

Jinja2 has some really powerful features that web design folks want to take advantage of:

- Template inheritance
  - Like class inheritance!
- HTML escaping
  - Stops some hacking attacks (XSS and SQL injection).
- Speed and efficiency
  - Optimized Python code.
- Flexibility and extensibility
  - We can add our own filters and functions.


---
## Knowledge Check: Discussion

- What's one reason why we might want to use templates, other than staying DRY?

<aside class="notes">

**Talking Point:**

- Answer: Templates allow us to add programming languages to our HTML templates.
</aside>

- What's template inheritance?

<aside class="notes">

**Talking Point**:

- Template inheritance is extending templates in very efficient ways.
</aside>


---

## Expanding on Our `index.html`

- We'll send a `greeting` variable into our `index.html` from both routes.

- The routes will display different things!

---

## Adding Templates

<aside class="notes">

**Talking Points:**

- This is the function that Flask uses to… you guessed it: Render our template(s)!
- For this exercise, we want to add some programming language (Python) into our HTML template.
</aside>

- Remember `import render_template`?
- This is the function that Flask uses to… you guessed it: Render our template(s)!

---

## Edit `index.html`

- Change the `<h1>` to be `{{ greeting }}`.

```html
...
   <body>
      <h1>Hello {{ name }}!</h1>
			<p>If music be the food of love, play on!</p>
	....
```

---

## Templating Syntax With Jinja

<aside class="notes">

**Talking Points:**

- What's awesome about this is that inside of these brackets, we can pass in Python syntax.
- In our example, we have a variable, which we're calling `name`.
- Whatever we assign to the variable `name` will be rendered when our page renders.
- Statements are where we would pass in logic like {%if this thing%} {% else that thing%}.
</aside>

- Recognize the `{{}}`?

- In Jinja, **templates** are rendered with double curly brackets (`{{ }}`).

- **Statements** are rendered with curly brackets and percent signs (`{% %}`).

  - A use case here is passing in logic like:
	```python
	{% if name == 'kevin' %}
	# Do the thing
	{% else %}
	# Do all the other things.
	```

---

## Rendering a Template in Flask

<aside class="notes">

**Talking Points:**

- We're going to modify the rest of our Flask app to pass some values into our variable in the template (curly braces).
- Let's change the rest of our `hello_flask.py` so that the whole thing looks the following script on screen.

- Here, we use `render_template` function which takes in two arguments:
  1. Our template name, `index.html`.
  1. Our **context** which, from the documentation is "the variables that should be available in the context of the template."

- Here, our variable is name which is passed into the <user> part of our route, and then becomes the value that we assign to the variable called `name`.
</aside>

Let's change our `my_website.py` accordingly:

```python
@app.route('/')
def home():
  return render_template("index.html", greeting="Hello World!")

...

@app.route('/shownum/<inte>')
def shownum(inte):
  my_greeting = "Your number is " + str(inte)
  return render_template("index.html", greeting=my_greeting)
```

---

## Try it!

- Check out: `http://localhost:5000`.
- Then: `http://localhost:5000/shownum/26`.

Do your other routes still work?

---

## Knowledge Check: Discussion

What two arguments did we pass into the `render_template` function?

<aside class="notes">

**Talking Point:**

- Answer: `index.html`, our template name, and `greeting`, which is our context.
</aside>

What's one reason we use templates?

<aside class="notes">

**Talking Points:**

Possible answers:
- Adding programming languages to our HTML templates.
- Transferring info from Flask to HTML.
- Lets us separate data from how we present data to users.
</aside>

---

## Your Turn!

- Create a new Flask app, `shakespeare.py`.
- Create a new template HTML file, `hello.html`.
  - It will display a paragraph with a parameter `poem` in it.
- Render it from the index endpoint.
- Remember calling in variables from the last lesson?
  - Have your Flask app read in the poem saved in `hi.txt`, then pass that to the `hello.html` template to display.
- Launch your Flask app and check the results!

---

## Template Solution

```html
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Shakespeare</title>
</head>
<body>
    <p>{{text}}</p>
</body>
</html>
```

---


## Python Solution

```python
from flask import Flask, render_template
import os # Note the new import — to be in the file system.

app = Flask(__name__)

file_path = '.'

with open(os.path.join(file_path, 'hi.txt')) as f:
	the_text = f.read()

@app.route('/') # When someone goes here...
def home(): # Do this.
    return render_template("hello.html", text=the_text)

if __name__ == '__main__':
	app.run(debug=True)
```



---

## Summary

- Jinja:
  - A popular templating engine.
  - Templates save us time and abstract presentation from data.

- Template fun:
  - We can pass variables into the template from the Flask app and the URL.
