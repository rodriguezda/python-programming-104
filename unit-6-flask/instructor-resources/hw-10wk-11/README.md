### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Kevin

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack at @kevin.coyle.
--->

# Flask: Intro Practice Problems

In this homework, you're going to write code for a problem. We'll be building on older material like basic Python function writing and argument settings in functions.

You will practice this programming concept we've covered in class:
* Writing a basic Flask app.

------------

## Deliverables

You will create a new `.py` file and write code to solve the problem. For example, you would create `problem1.py` with your solution code to the first problem. Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following:*

```
python problem1.py
```

> **Hint**: After finish writing your code, launch your server, go into your browser, and be sure that your Flask app is outputting the intended data.


## Requirements:

* By the end of this, you should have one `.py` file.

------------

## Problem 1: "Today Your Love, Tomorrow the (Hello) World"

### Skill You're Practicing: Writing basic Flask applications.

Write a Flask app that returns your favorite food.

#### Example Code
```
def giveFood():
    return "I could eat pepperoni pizza all day everyday."
```

#### Example Test Output
```
I could eat pepperoni pizza all day everyday.
```

**Hint 1:**

Refer to your class notes for details about how to import the proper libraries and use the `if __name__ == '__main__'` pattern.

**Hint 2:**

Don't forget that you need to specify the URL's ending with our @app.route decorator.

```
@app.route("/")
```

... is our way of saying "at the home page."
