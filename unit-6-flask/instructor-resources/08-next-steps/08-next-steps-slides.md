<!--
title: Next Steps in Web Development
type: lesson
duration: "01:00"
creator: Kevin Coyle
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Next Steps in Web Development</h1>

---

## Learning Objectives
*After this lesson, you will be able to:*

- Identify common web concepts to dive into next.
- Identify common Python libraries used for front-end web development.
- Identify common Python-based tech stacks for back-end web development.

---

## Web Development Is Pretty Cool. What's Next?

Web development is a huge field. Where should you go next?

There are a few options to explore:

- Front-end web development.
    - Code in Python to just host the site.
- Back-end with Python.
    - Code in Python

With one of those, you can also explore...

- Extending Flask.
- Other popular Python web framework libraries.

<aside class="notes">

**Talking Points:**

- When you know Python, there are multiple areas of web development open to you.
- Because Python is both a front- and back-end language, you have a wide array of options.
  - Flask has built the whole website for you — the front and back ends. But you can do each side individually, without Flask. People can write the front end using HTML and JavaScript (maybe add "HTML and JavaScript are done for you" as a sub-bullet under back-end), and rely on your Python skills to host the site.
- What's this front-end/back-end distinction? To be honest, there's usually a bit of overlap and people are required to wear hats from one side or another, but generally:
  - Front-end people handle the part of the website that people see.
  - Back-end people handle the server side — where the site works, updates, and changes.
- Front-end development is for you if you're more interested in a website's design than how it gets online.
- Back-end programming route is for you if you don't want to worry about how the site's appearance; you just want the programming challenges of getting the site online.
</aside>


---

## Path 1: Front-End Development?


Configuring the part of the website people see.

**Why might you go this route?**

- You're design-inclined.
- You want to make cool sites!
- You're using Python to accomplish the goal of propping up your designs.

---

## Path 1: Front-End Development — What Next?

GA has some classes! (A shameless self-plug, but part-time Front-End Web Development is a good place to start.)

For your own study:

- Get better at HTML and CSS (*important*).
  - The core of front-end web development.
- Check out Bootstrap and Flexbox.
  - HTML/CSS frameworks.
- Check out JavaScript and JavaScript frameworks.
  - Add interactivity to your webpages.
  - React, Angular, jQuery, and Ember are all popular in different locations.

---

## Path 1: Front-End Development — Then What?

Start building up a portfolio of projects.

- Make yourself a portfolio website to showcase your work!

Once you're comfortable, try modifying premade Bootstrap themes.

---

## Path 2: Back-End Development?

Handle the server side:

- Make websites work.
- Bring in data.

**Why might you go this route?**

- You love programming!
- You don't care how the website looks.
- You just want to write Python.
- The idea of using someone else's designs sounds great.

---

## Path 2: Back-End Development — What Next?

GA has some classes! (Another shameless self plug. The full-time Web Development Immersive will give you a strong foundation in back-end essentials.)

For your own study:

- Learn Git version control (*important*).
  - Learn GitHub or another version control system.
- Check out connecting to databases.
- Learn SQL.
- Learn about SQLAlchemy and PyMongo.
- Learn about servers like WSGI and NGINX.

---

## Path 2: Back-End Development — Then What?

Start a portfolio (preferably on GitHub or another version control system).

Once you're comfortable:

- Try starting a MongoDB yourself, then having Flask retrieve data from there.


---

## Knowledge Check: I want to…

**… make a beautiful website.**

All this Python coding is a bit much for me, but I like websites.

Which should I look into?

- Front-end web development
- HTML/CSS/JavaScript
- Flask extensions
- Back-end web development

Which do you think?

<aside class="notes">

**Teaching Tips:**

- Answer: Front-end web development or HTML/CSS/JavaScript.
</aside>

---

## Solution: I want to…

**… make a beautiful website.**

All this Python coding is a bit much for me, but I like websites.

Which should I look into?

- Front-end web development
- HTML/CSS/JavaScript

<aside class="notes">

**Teaching Tips:**

- Answer: Front-end web development or HTML/CSS/JavaScript
</aside>

---

## Path(ish) 3: Expanding on Flask

This is not really a path! But you can do it in conjunction with either of the above.

Look into integrating these with Flask:

- Bootstrap
- SQLAlchemy/PyMongo

<aside class="notes">

**Talking Points:**
 - Flask is fantastic web development framework.
 - Our first `Hello World` app was about seven lines of code.
   - However, building modern websites with any framework (even one as lightweight as Flask) takes work.
 - As we are primarily concerned here with Python and Flask, I'll give you a couple shortcuts, listed here on the slides.
 - These integrate with Flask fairly easily. Yay!
 </aside>

---

## Bootstrap

Front-end or Flask? This slide's for you.

Like awesome-looking websites?

Don't like typing out HTML and CSS?

Bootstrap is for you!

- It's a free and open-source front-end framework.
- Handles all of the "pretty" stuff.

Bootstrap is great for:

- Prospective front-end developers.
    - Extremely popular in many companies.
- Integrating with Flask!
    - Bootstrap makes a site pretty, and Flask makes it work.

<aside class="notes">

**Talking Points:**
 - Bootstrap was started by Mark Otto and Jacob Thornton at Twitter.
 - One of the main use cases for Bootstrap is people who like the idea of great-looking websites, but don't want to write the CSS and/or HTML.
 - Bootstrap can connect to Flask.
 </aside>

---

## How to Get Started With Bootstrap and Flask

Here's how to get it:

- `pip install Flask-Bootstrap`.
- `git clone https://github.com/mbr/flask-bootstrap.git`.
- `cd` into the `flask-bootstrap` directory.
- Run `pip install -r sample_app/requirements.txt` to install the required packages.

And here's how to run it:

- Deploy Flask with Bootstrap by running `flask --app=sample_app dev`.
- Go through directories.
    - Comment out code to be certain you know exactly what every line is doing.

Here's where you can read the docs: https://getbootstrap.com/docs/3.3/getting-started/.

---

## SQLAlchemy and PyMongo

Back-end or Flask? This slide's for you.

We can't always connect to a list!

- Most information is stored in databases (like a spreadsheet).

**SQL** is *the* language for working with databases.

Knowing a database is also crucial! Popular databases include:

- MySQL
- MongoDB
- PostgresQL

Some Python libraries to look into include:

- SQLAlchemy
- PyMongo

<aside class="notes">

**Talking Points:**
 - When we added data to our Flask app, we appended to a list.
 - This is fantastic first start, but if you'd like to have a larger database, you'll need to look into databases like PostgreQL, MySQL, or MongoDB.
 - Flask can integrate with a number of databases.
 - Although there is no out-of-the-box with Flask, there are many libraries in Python.
 - Two that we'll highlight here are SQLAlchemy and MongoDB.
 - There's an extension of Flask called Flask-SqlAlchemy — `pip install Flask-SqlAlchemy` — that allows you to connect to SQL databases using Python.
 - You might be asking yourself, "What about these 'NoSQL' databases I keep hearing about?"
 - Remember how we "JSON-ified" our `return`? MongoDB is an open-source database that stores JSON like "documents."
 - Instead of rows like in PostgreSQL and such, there can be any number, name, or hierarchy of fields.
</aside>
---

## How to Get Started With PyMongo

This slide's long! It's for your later reference.

How do I use Flask and databases?

- Install Flask SQLAlchemy with `pip install Flask-SqlAlchemy`.
- Install Flask PyMongo with `pip install Flask-PyMongo`.

What about back-end database with no Flask?

- Install just PyMongo with `python -m pip install pymongo`.

Either way, you need a database. Install MongoDB:

- `brew update`
- `brew install mongodb`
- `brew install mongodb --devel`

---

## How to Get Started With PyMongo

Start your MongoDB instance:

- `mkdir -p /data/db`
    - Note: If that results in an error, you need different privileges.
    - Run: `sudo mkdir -p /data/db`.
- Start your database with the Mongo daemon with the command `mongod`.

---

## How to Get Started With PyMongo

Then, add some data to your database. Save the below to a Python file and then try making `GET` and `POST` requests!


```
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'burritodb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/burritodb'

mongo = PyMongo(app)

@app.route('/burrito', methods=['GET'])
def get_all_burritos():
  burrito = mongo.db.burritos
  output = []
  for s in burrito.find():
    output.append({'ingredient' : s['ingredient'], 'burrito_necessity' : s['burrito_necessity']})
  return jsonify({'result' : output})

@app.route('/burrito/', methods=['GET'])
def get_one_burrito(ingredient):
  burrito = mongo.db.burritos
  s = burrito.find_one({'ingredient' : ingredient})
  if s:
    output = {'ingredient' : s['ingredient'], 'burrito_necessity' : s['burrito_necessity']}
  else:
    output = "No such ingredient"
  return jsonify({'result' : output})

@app.route('/burrito', methods=['POST'])
def add_burrito():
  burrito = mongo.db.burritos
  ingredient = request.json['ingredient']
  burrito_necessity = request.json['burrito_necessity']
  burrito_id = burrito.insert({'ingredient': ingredient, 'burrito_necessity': burrito_necessity})
  new_burrito = burrito.find_one({'_id': burrito_id })
  output = {'ingredient' : new_burrito['ingredient'], 'burrito_necessity' : new_burrito['burrito_necessity']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)

```


---

## Knowledge Check: I want to…

**…make a beautiful database.**

All this Python coding is exciting!

Which of these should I look into?

- Bootstrap
- Back-end web development
- SQLAlchemy
- MySQL
- PostgreSQL
- MongoDB
- HTML and CSS

Which do you think?

<aside class="notes">

**Teaching Tips:**

Answer: Back-end web development, SQLAlchemy, MySQL, PostgreSQL, and MongoDB.
</aside>

---

## Solution: I want to…

**…make a beautiful database.**

All this Python coding is exciting!

Which of these should I look into?

- Back-end web development
 - SQLAlchemy
 - MySQL
 - PostgreSQL
 - MongoDB

<aside class="notes">

**Teaching Tips:**

Answer: Back-end web development, SQLAlchemy, MySQL, PostgreSQL, and MongoDB.
</aside>

---

## Path(ish) 4: Web Frameworks That Aren't Flask

Flask isn't the only Python web framework.

There are also:

- Pyramid
- Zope
- Bottle
- CherryPy
- **Django**
- **Pelican**

<aside class="notes">

**Talking Points:**
 - You may have heard of some other Python-based web frameworks like these listed.
 - We're going to focus on the last two: Django and Pelican.
 </aside>

---

## What's Django?

- A complete, "batteries-included" approach philosophy.
  - Conversely, Flask is lightweight; you add pieces on as you need them.

- A more secure framework.

- Highly scalable — think Disqus and Instagram.

- Get started at djangoproject.com.

<aside class="notes">

**Talking Points:**
- Django is similar to Flask in that it's a web framework.
- However, whereas Flask takes a "Lego-like" building-blocks approach, Django comes with more of the bells and whistles built in.
- What's great about Django is that other developers have taken a lot of the hassle out of web development.
- This includes some things that help developers out like everything listed here.
</aside>

---

## What's Pelican?

- A Python library for static sites.
  - Blogs don't need to change beyond the text!

- Generates the HTML for you.

- You just need Python code and text!

This is a really quick way to get a site up and running.

`pip install pelican`

<aside class="notes">

**Talking Points:**
- Recently, there's been a resurgence in the popularity of static webpages.
- Blogs and other sites that don't require as many code updates are prime examples of sites that would use static webpages.
- Python has a library called Pelican, which can generate these static sites for you (they generate all the HTML from a markdown file that you create).
- This means: You just write some Python code, and all the HTML gets made for you!
</aside>
---

## Web Development in General

There's so much more!

Mozilla (the company that makes Firefox) is an amazing resource.

- [developer.mozilla.org/](https://developer.mozilla.org/)

<aside class="notes">

**Talking Points:**
- We've covered some libraries as well as some places to go for front-end and back-end tech stacks.
- However, we haven't even scratched the surface of web development as a whole.
- The fine folks at Mozilla have put together a web development resource that you can check out at developer.mozilla.org.
</aside>

---

## Knowledge Check: I want to…

**… make a blog.**

I want to build simple, static websites in less than 10 minutes and then work on content.

Which of these should I look into?

- Pelican
- Databases
- Bootstrap
- Django

Which do you think?

<aside class="notes">

**Talking Point:**

Answer: Pelican!
</aside>

---

## Solution: I want to…

**…make a blog.**

I want to build simple, static websites in less than 10 minutes and then work on content.

Which of these should I look into?

- Pelican!

<aside class="notes">

**Talking Point:**

Answer: Pelican!
</aside>

---

## Knowledge Check: I want to…

**…make an awesome Flask-based website.**

I really liked all the above and am right at home between front-end and back-end with Flask.

Which of these should I look into?

- More [Flask extensions](http://flask.pocoo.org/extensions/)
- Bootstrap
- PostgresSQL
- HTML and CSS
- Pelican
- Django

Which do you think?

<aside class="notes">

**Teaching Tips:**
- More [Flask extensions](http://flask.pocoo.org/extensions/)
- Bootstrap
- PostgreSQL
</aside>

---

## Solution: I want to…

**…make an awesome Flask-based website.**

I really liked all of the above and am right at home between front- and back-end with Flask.

Which of these should I look into?

- More [Flask extensions](http://flask.pocoo.org/extensions/)
- Bootstrap
- PostgreSQL

<aside class="notes">

**Teaching Tips:**
Answer:
- More [Flask extensions](http://flask.pocoo.org/extensions/)
- Bootstrap
- PostgreSQL
</aside>

---

## Knowledge Check: I want to…

**Make a website, but without all these libraries and extensions**

I really the idea of this whole framework thing, but I wish there were only one, obvious way to do things.

Which of these should I look into?

- More [Flask extensions](http://flask.pocoo.org/extensions/)
- Bootstrap
- PostgreSQL
- HTML / CSS
- Pelican
- Django

<aside class="notes">

**Teaching Tips:**
Answer: Django
</aside>

---

## Solution: I want to…

**… make a website, but without all these libraries and extension.s**

I really the idea of this whole framework thing, but I wish there were only one obvious way to do things.

Which of these should I look into?

- Django

<aside class="notes">

**Teaching Tips:**
Answer: Django
</aside>

---

## Summary

There are a lot of ways to go!

- Extending Flask.
- Python front-end libraries.
- Python back-end libraries for databases.
- A few other Python-based web frameworks.
- General front-end or back-end web development.

---

## Additional Reading
- [Explore Flask](http://exploreflask.com/en/latest/pym)
- [PyMongo Documentation](https://api.mongodb.com/python/current/)
- [SQLAlchemy's Fantastic Object Relational Mapper Tutorial](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html)
- [Django Documentation](https://docs.djangoproject.com/en/2.0/)
- [Pelican Documentation](http://docs.getpelican.com/en/stable/)
- [The Flask Docs](http://flask.pocoo.org/docs/1.0/)
- [Beginner Git Tutorial](https://www.atlassian.com/git/tutorials/what-is-version-control)
