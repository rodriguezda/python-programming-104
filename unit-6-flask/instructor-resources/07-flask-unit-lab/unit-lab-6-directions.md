### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming


<!---
This assignment was developed by Cody Soyland

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Cody's not at GA; hit me up on Slack at @zoe.lubitz.
--->

# Unit 7 Lab: Flask

## Overview
Welcome to the Flask unit lab! You're going to use some logic from Lab 5's `movie_app.py` so make sure you understand what it's doing!

You'll create a web app where a user can enter and search for a movie, then see the results and details. So basically, you're creating a website version of what the `movie_app.py` was able to do.

-------------

## Deliverables

You should have a `movie_flask_app.py` that starts Flask website.

```bash
# This runs the Flask app!
python movie_flask_app.py
```

---------------

## Requirements

Your program will:

- Be accessible by a local web browser.
- Use the Flask microframework for a user interface.
- Leverage the code already written in previous labs to query the OMDb API.

Your program has three main components:
- Landing page.
- Search results page.
- Movie details page.

Your program's functionality should look like this (with variation on styling, but it needs some styling):

1. Search Results at `127.0.0.1:5000/`

    <img src="https://gist.github.com/sonylnagale/e064a3414930c0870e369c24b2723b61/raw/f2efde3eb35a8ad718740a9ebe2b24c8887ab290/movie-search.png" width="450"/>

1. Movie Details at `127.0.0.1:5000/movie`

    <img src="https://gist.github.com/sonylnagale/e064a3414930c0870e369c24b2723b61/raw/f2efde3eb35a8ad718740a9ebe2b24c8887ab290/movie-details.png" width="650"/>

-------------

## Directions

### Step 1: Set up your folders (Flask)

Set up a directory that looks like this. Copy the Lab 5 `movie_app.py` and put it into the `app/` directory. Make a copy of `movie_app.py` and rename it to `movie_flask_app.py`

```
project
│   
│
└───app
│   │   movie_app.py
|   |   movie_flask_app.py
|   |   omdb_api_key.txt
│   │   
│   │
│   └───templates
│   │    └─── home.html
│   │
│   │
│   └───static
│       └───style.css
```

Click [here](starter-code/static/style.css) for the starter CSS file and [here](starter-code/templates/home.html) for the `home.html` file. Be sure to place them in a `static` and `template` folder appropriately. Take this time to read through and understand what `home.html` and `style.css` are doing.


### Step 2: Setting Up a Basic App (Flask)

#### Make the app appear

1. In your new `movie_flask_app.py`, import the correct pieces from `flask` to run Flask, a template, and a request.
    ```
    from flask import Flask, render_template, request
    ```
1. Initialize your app at the top of the file
    ```
    app = Flask(__name__)
    ```
1. At the bottom of the file, replace the `if __name__` code block with this:
    ```
    if __name__ == "__main__":
      main()
    ```
1. Start the app inside the `main()` function. Remember to start a Flask app, you need the following line:
    ```
    app.run(debug=True)
    ```
    Replace everything in your `main()` function with just that line.
1. Above the `if __name__ == "__main__"` condition, create an `@app.route` to handle user traffic to the `127.0.0.1:5000/` page.
1. On this page, add a `return` string of your choosing — it's just a test for now.

### Step 2 Checkpoint!

Try running the app! Remember, it'll be at `http://127.0.0.1:5000/`.


### Step 3: Making the App More Complex with Search (Flask)

The `127.0.0.1:5000/` page should allow a user to search and display the results.

#### Understanding the `home.html` template

1. Render the `home.html` template inside of `home()`. Remember how to do this?
You want to return the rendered form of the `html` page. Use the `render_template` function we learned in class.
1. What happens when you input text into the form and click the "Find Movie!" button?
  - Notice that the url changed to include the `query` of whatever you input

We want the app to hit the OMDB API when we click that button. So let's do that!

#### Use form input to hit OMDB API

1. We are try to get form input into our app, so we need to tell Flask that this is a page with a form now. Add the `methods` argument to `@app.route`. We just need the `GET`, so it should look like this:
    ```
    @app.route("/", methods=["GET"])
    ```
1. In your Python app, add a line like this in `home()`:
    ```python
    # Get the search query from the form.
    movie_query = request.args.get("query", "")
    ```
    This will get whatever the user put into the form (aka `query`).
1. Inside of `home()`, do the following (Hint: most of this is already done in `list_search_results()`):
    - get the api key
    - create an OMDB object
    - call the OMDB `search()` function with the `query`
    - from the `matching_movie_list`, create a list of just the movie titles from that list
    - _return_ the rendered `home.html` just like before, but this time using the `query` and `results` arguments of the `render_template` function.
1. Have the OMDb search run *only* if `movie_query` exists. Either way, render the `home.html` template.

### Step 3 Checkpoint!

At this point your app should behave like so:
- If you do not provide any form input and just press "Find Movie!", nothing but the url should change to `http://localhost:5000/?query=`.
- If you give an input (i.e. `star wars`) and press "Find Movie!", your `127.0.0.1:5000/` should have changed to `http://localhost:5000/?query=star+wars` **and** the page should have turned into something like

<img src="https://gist.github.com/sonylnagale/e064a3414930c0870e369c24b2723b61/raw/f2efde3eb35a8ad718740a9ebe2b24c8887ab290/movie-search.png" width="500"/>

Awesome! You're almost done with the search functionality of your site!

### Step 4: Write your own HTML

You can see that each movie title in the search results is hyperlinked, but the link is broken. Try clicking on the links now.

Let's fix that — we'll add the page and display movie details on it.

1. Create a new template for a movie detail page, `movie.html` (you can use the `home.html` as an outline!). In it:
    - Title the page "Movie Search." Remember this is done with the `<title>` tag in the `<head>` portion of your `HTML` page.
    - Underneath the `<head>` section, display the title and rating as an `h2`. `title` and `rating` will be values the template receives from your Python script. Remember template variables need the `{{ }}` around it.
    - Beneath that, put an image link for the poster. The image source here will be `poster`, another value received from your Python script.
    - Beneath that, make a paragraph (`p`) that says "Year Released:" and the `year`, which will be a value received from your Python script.
    - Below that, have a new paragraph with "Plot Summary:", then `plot`, which will be a value received from the Python app. Wrap the "Plot Summary:" and "Year Released" text in a `strong` opening and closing tag.
    - Don't forget to close all tags!

At this point your `movie.html` should look something like:
```
<!doctype html>
<html lang="en">

<head>
... some stuff, maybe a title...
</head>
<body>
... a heading, an image, the year released, and the plot summary...
</bod>
</html>
```

Back in your `movie_flask_app.py`, create a route to `/movies/<id>` called `movie`, which takes an `id` value.

### Step 4 Checkpoint!

Now that we have the `movie.html` HTML template and the `/movie` route defined in `movie_flask_app.py`, we can test both of these together. Test just the route by rendering the template with hard-coded values for `title`, `year`, `poster`, `plot`, and `rating`:

For example if we passed the following values into our `render_template`:
```
title="My Bird Movie", year=1990, poster="https://cdn.pixabay.com/photo/2016/10/27/07/49/bird-1773616__340.png", plot="The > plot is a bird saying hello", rating="99%"
```
Then we should get something like this at `127.0.0.1:5000/movie`:

<img src="https://i.imgur.com/kTU1Ovp.png" width="400"/>

Now that we can render `movie.html`, let's move on to getting the actual values for `title`, `year`, `poster`, `plot`, and `rating`.

### Step 5: Working with Templates

1. We have our list of search results, each of which has an `id` value identifying it uniquely on Rotten Tomatoes. To get more details about a specific movie, we should search for that specific `id`. Searching for a movie result given the `id` seems like something that should go in the `OMDb` class!
    - In that class, create a new method, `get_movie_by_id()`. You can copy (don't delete) your existing `get_movie()` method, but change the parameter to `id`. Also, in the call to `self.call_api`, pass in `i=id` instead of `t=movie_query`.
    - How did we know to do that? It's in the OMDb API docs! Go [here](https://www.omdbapi.com/) and scroll down to "Parameters."

1. Back to your `movies()` route, get the API key, create the OMDb object, and then call your new `get_movie_by_id()` method, passing it the `id` parameter. The website's behavior now isn't different than at the last checkpoint, but run the app and test everything at this point to make sure you haven't broken anything.
    - Refresh the `127.0.0.1:5000/`, make sure the form still works correctly
    - Refresh `127.0.0.1:5000/movie`, make sure the hard coded values still show up on your webpage.
1. Now, let's display the actual movie information. Change what's passed into your template to be actual values from the `movie` object.
    - **Hint**: Check your `Movie` class to see how to get information!
    - **Hint**: You'll have to call the `get_movie_rating()` method to specifically get the Rotten Tomatoes rating.

Try it out! Try a bunch of different movies to see your app in action. At this point, you should be able to search for any movie and click on the title for that movie and go to it's own movie page.

### Step 5 Checkpoint!

If you input "moana" into the form field and press "Find Movie!", you should get a page that looks like this (url: `http://localhost:5000/?query=moana`):

<img src="https://imgur.com/5wzHvPg.png" width="450"/>

And if you click on the first title on the page (the 2016 one), you should get a page that looks like this (url: `http://localhost:5000/movies/tt3521164`:

<img src="https://imgur.com/yjsHYhr.png" width="650"/>

Great job!

### Step 6: Making the App a Little More Colorful (CSS)

Your app is functional, but a little plain. Modify the CSS file your app has to be a little more fun!
- **Note**: You probably haven't seen some of the CSS that's currently there! Leave those alone for now, but if you have time after adding your own styling, play around with it to see what changes.

If you'd like inspiration, here is what we have to make the images at the top of the page. All of it applies to the `body`:
- A `font-family` of `"Georgia, sans-serif"`.
- A `color` of `#333a56`.
    - This changes the text color.
- `text-align` to `center`
- `font-size` to `16px`.
- `background: #f7f5e6`.

We also added styling to the `h2`:
- `text-transform` to `uppercase`.
    - This makes the text all capitals.
- `font-weight` to `bold`.
    - This bolds the text.

Tweak some of the colors and styling around to your liking! Change at least 3 stylings in the `style.css` file.
