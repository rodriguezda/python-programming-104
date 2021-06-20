
## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>APIs and Requests in Flask</h1>

---

## Learning Objectives
*After this lesson, you will be able to:*

- Create an API that makes a `GET` request with Flask.
- Create an API that makes a `POST` request with Flask.

---

## Discussion: Remember APIs?

- We can call them.

- But who publishes them?

- Do you think we could make one?

---

## APIs

In your browser, head to [https://swapi.co/api/people/13/?format=json](https://swapi.co/api/people/13/?format=json).

- That's a collection of data about Chewbacca.

What would it look like in Chewbacca's language?

Head to [https://swapi.co/api/people/13/?format=wookiee](https://swapi.co/api/people/13/?format=wookiee).

- This is the same data written in Wookiee!

---

## Web API Recap

- A list of function calls that are made to remote servers.
  - Sent by encoding a URL (an HTTP request).
  - We could **call** the OMDb API to get a movie's information.

- Now, we're going to **create** an API using Flask.

<aside class="notes">

**Talking Points:**

- At a theoretical level, you can think of interfaces kind of analogous to real-world counterparts:
  - Door handles. These interfaces get pushed or pulled, and the door opens to a new space. We could even have crazy DeLorean style doors that open upward.
  - A standard telephone. When you call someone, you are connected from your space to another space using this interface.

- Today, we'll write a function based on displaying a list of heroes of the Python/programming world.
- Using the abstracted examples from a second ago, you can think of the function call as the phone number that you're dialing, or the handle that you make a request on.
- Many web programmers today use web APIs. The rise of JavaScript and the current state of programming techniques are the principal movers of this rise. We're going to create an API today using Flask.
- Because of how interactive many websites have become (again, fingers pointed at JavaScript), many other languages like Python started co-opting standards to communicate data to and from servers.

</aside>


---

## Discussion: The Sides of an API

What's the difference between calling and creating an API?

<aside class="notes">

**Talking Point:**

- Answer: Calling an API allows you to retrieve data, while creating an API makes some data that you want to publish accessible.
</aside>

---

## HTTP

- Stands for Hypertext Transfer Protocol.
- A system of rules (protocol) that determines how webpages (hypertext) get sent from one place to another (transfer).

<aside class="notes">

**Talking Points:**

There are **clients** that:

- HTTP clients respond to HTTP responses from a web server/HTTP server.
- Web servers receive HTTP requests and generate HTTP responses.

</aside>

---

## Recap: Clients and Servers

With HTTP, there are two sides:

- Clients
  - Make the requests.
- Servers
  - Receive those requests.

---

## CRUD

These four functions are everywhere in programming:

- **C**reate
- **R**ead
- **U**pdate
- **D**elete

<aside class="notes">

**Talking Points:**

- CRUD operations are the four basic functions in persistent storage.
- CRUD operations are everywhere in programming.
- Here, we're most concerned with how our API is going to create, read, and update data via an HTTP URL.

</aside>


---

## CRUD Mapped to HTTP Requests

What potential operations could we do when calling an API?

- `GET`:
	- *Read*.
	- "Tell me all values in `instrument_list`."
- `POST`:
	- Usually *Create*, sometimes *Update*.
	- "Add `cello` to `instrument_list`."
- `PUT`:
	- Similar to `POST`.
	- *Create* or *Update* an entity.
- `PATCH`:
	- *Update* only a specified field.
	- "In `instrument_list`, change `guitar_type` to `bass`."
- `DELETE`:
	- *Delete!*
	- "Delete `instrument_list`."
	- Doesn't necessarily happen immediately.

We're going to be using GET and POST in this lesson.

<aside class="notes">

**Talking Points:**

- Here are HTTP methods used to map to CRUD (create, read, update, delete) operations to HTTP requests:
  - `GET`, `PUT`, and `PATCH`.
- They must be safe and idempotent (i.e., regardless of how many times it repeats with the same parameters, the results are the same).

</aside>

---

## Knowledge Check:
What does CRUD stand for?

<aside class="notes">

**Talking Point:**

- Answer: "Create, Read/Retrieve, Update, and Delete/Destroy."

</aside>

---

## Knowledge Check: `POST` and `GET`

What's the difference between a `POST` and `GET` request?

<aside class="notes">

**Talking Point:**

- Answer: A `POST` request will create or update something, while a `GET` request will read something.

</aside>

---

## Creating an API With Flask

We're going to create an example of an API that:

- Takes in a list of dictionaries.
- Parses that list based on what we pass into the API.
- Returns a JSON payload with the appropriate data.

---

## Remember JSON?

- Both dictionaries and JSONs have key-value pairs.
- Both dictionaries and JSONs are wrapped in curly brackets (`{}`).

```python
heroes_dictionary = {'person': 'Peter_Norvig', 'person': 'Gilbert_Strang', 'person': 'Ada_Lovelace', 'person': 'Guido_van_Rossum'}
heroes_json = [{'person': 'Peter_Norvig'}, {'person': 'Gilbert_Strang'}, {'person': 'Ada_Lovelace'}, {'person': 'Guido_van_Rossum'}]
```

<aside class="notes">

**Talking Points:**

- The most that we need to know right now about JSON is that it has a similar data structure in Python: the dictionary.
- We're going to modify `hello_api.py` again in your code editor.

</aside>

---
## We Do: Basic App

- Create a new Flask app, `hello_api.py`.

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello, World"

if __name__ == '__main__':
	app.run(debug=True)
```

Check that it works!

---

## We Do: New Functions

- Import two new functions: `jsonify` and `request`.

```
from flask import Flask, jsonify, request
```

<aside class="notes">

**Talking Point:**

- Explain why we're taking these in.

</aside>


---

## We Do: First API Route

- Add a new route under our `hello` home page.

```python
@app.route('/api', methods=['GET'])
def returnJsonTest():
    return jsonify({'What happened?': 'It worked!'})
```

- Test both routes:

  - `localhost:5000`

  - `localhost:5000/api`

<aside class="notes">

**Talking Points:**

- Let's add a new route under our `Hello World` home page.
- Save your Python file. If we have our code right, our new page should return our JSON!
- Open your browser and first head to `localhost:5000`.
- Then head to `localhost:5000/api`.
- It worked! Congratulations!

</aside>

---

## Knowledge Check: Discussion

What two new functions did we add into our import?

What do they do?

<aside class="notes">

**Talking Point:**

- Answer: `jsonify` and `request`.

</aside>

---

## We Do: Altering Data With APIs

- Cool!

- What if we want the data to change?

- Add a list under the `app` instantiation, above the routes.

	```python
	heroes = [{'person': 'Peter_Norvig'}, {'person': 'Gilbert_Strang'}, {'person': 'Ada_Lovelace'}, {'person': 'Guido_van_Rossum'}]
	```

What can we do with that?

<aside class="notes">

**Talking Points:**

- This is cool, but what if we want that data to change?
- Let's create a list like the one on the screen.
- Let's add that into our script in `hello_api.py`.

**Teaching Tips:**

The code currently is:
```
from flask import Flask, jsonify, request

app = Flask(__name__)

heroes = [{'person': 'Peter_Norvig'}, {'person': 'Gilbert_Strang'}, {'person': 'Ada_Lovelace'}, {'person': 'Guido_van_Rossum'}]

@app.route('/')
def hello():
	return "Hello, World"

@app.route('/api', methods=['GET'])
def returnJsonTest():
    return jsonify({'What happened?': 'It worked!'})

if __name__ == '__main__':
	app.run(debug=True)
```
</aside>


---

## We Do: APIs to Return All Data

- We have a list.
- We need to get data from it.
- Make a new route:

```python
@app.route('/heroes', methods=['GET'])
def gimmeAllHeroes():
    return jsonify({'heroes': heroes})
```

<aside class="notes">

**Talking Points:**

- We also need to add in some code to give us the data from our list.
  - We'll add a function to return all the data.
  - Type out the code on the slide in your `hello_api.py` script, below the `def`.

- There are a few things going on here:
  - We loop over our list of heroes.
  - We return one of the heroes if our name in the HTTP address matches the name in our function.

</aside>

---

## We Do: APIs to Return Only SOME Data

- At this route, loop over the heroes.
- Try to find the one we want!

```python
@app.route('/heroes/<string:name>', methods=['GET'])
def gimmeOneHero(name):
		names = [hero for hero in heroes if hero['person'] == name]
  	return jsonify({'hero': names[0]})
```

<aside class="notes">

**Talking Point:**

- There are a few things going on here:
  - We loop over our list of heroes.
  - We return one of the heroes if our name in the HTTP address matches the name in our function.

</aside>

---

## We Do Aside — Always Error-Check

What happens when you input something that's inaccurate?

This is a good time for error-checking!

```python
def gimmeOneHero(name):
    names = [hero for hero in heroes if hero['person'] == name]
    if names:
        return jsonify({'hero': names[0]})
    else:
        return "Hero not found"
```

---

## Create a POST Request With Flask

- What if we want more heroes?
- Let's add data to our list of heroes with a `POST` request.
	- `POST` was "Create" (and, very rarely, "Update").

<aside class="notes">

**Talking Point:**

- Let's try adding data to our list of heroes with a `POST` request. Right now, our app looks like the following on the screen.

</aside>

---

## Adding Our New `POST` Function

- We can use the same route — with a different method.

```python
@app.route('/heroes', methods=['POST'])
def addMyHero():
    newhero = {"person": request.get_json()["person"]}

    heroes.append(newhero)
    return jsonify({"heroes": heroes})
```

<aside class="notes">

**Talking Points:**

- We'll use the same route, and if a `POST` request gets made, we'll append that into our heroes list.
- Add in the following function that I've named `addMyHero()`.

</aside>

---

## Knowledge Check

Assuming our code doesn't have any errors, what should happen when our `POST` request takes place?

<aside class="notes">

**Talking Point:**

- We should append a hero (our data) into our heroes list (our database).

</aside>

---

## Profit

Now we'll check to see if our `POST` request works.

- Open a new terminal window, and `python hello_api.py`.
  - Launch the app!

- Going to `/heroes` gives us the heroes list.
- How do we `POST`?

- We'll use a sample program:

```python
import requests

payload = {'person':'Alan_Turing'}

r = requests.post('http://localhost:5000/heroes', json=payload)

```

Save this code in a new file named `api_test.py`.

<aside class="notes">

**Talking Points:**

- Now we'll check to see if our `POST` request works.
  1. Open a new terminal window, and `python hello_api.py`.
- This will launch our server.
  2. Once your Flask app has started, open a new tab using `Command + T`.
We need the server to remain running locally.
  3. In the new tab, we're going to make a `POST` request with a particular content type of JSON.
  4. Run `python api_test.py` and then open  `http://localhost:5000/heroes`  
  5. We should see our new hero list with Alan appended!

</aside>

---

## Quiz

Which of these is the right code for a POST request?

- Option A

```python
@app.route('/myapiroute', methods=['POST'])
def butAmIMakingARequest():
    type_of_request = {"requestType:" :" This is definitely a GET Request"}
    requestage.append(type_of_request)
    return jsonify({"theAnswer" :  requestage})
```

- Option B

```python
type_of_request = [{"requestType:" :" This is definitely a POST Request"}]
@app.route('/myapiroute', methods=['GET'])
def butAmIMakingARequest():
    return jsonify({"theAnswer" :  type_of_request})
```

<aside class="notes">

**Talking Point:**

- Answer: Despite what the variables and key-value pairs are named, the correct answer is Option A.

</aside>

___

## Summary

We covered APIs and requests in Flask:

- We made an API using JSON!
- We used `GET` to display it.
- We used `POST` to add to it.

---

## Additional Reading
- [Flask JSONify Documentation](http://flask.pocoo.org/docs/1.0/api/#flask.json.jsonify)
