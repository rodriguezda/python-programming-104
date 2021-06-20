### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Brandi

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack at @brandib.
--->

# Python Modules, Packages, and APIs: Practice Problems, Part 2

In this homework, you're going to write code for the second of the two challenge problems. This code will continue off your code from the previous homework.

You will practice these programming concepts we've covered in class:

* Including and using modules and packages.
* Using data from APIs.
* Reading documentation for modules and APIs.

---

## Deliverables

This homework is the second of a two-part code challenge, plus a bonus challenge. It is a little different than the other homeworks because this assignment will build on the code from Part 1, the previous homework. For your solution here, you can directly edit the `solution.py` file from the previous assignment.

*Reminder: On your laptop, you can run the file from your command line with the following:*

```python
python solution.py
```

> **Hint:** Make sure you are printing something out with the `print` statement. Otherwise, you won't see any output from running your program!


## Requirements:

By the end of this, you should have:
* A file called `solution.py` with your combined code from Parts 1 and 2 (and, if you attempted it, the bonus portion).

---

# Code Challenges

## Problem 1: Geo Cody

You already have the solution to this section from the previous homework. As a reminder, you put several destinations into a list of strings called `destinations`. Then, you imported the the [geocoder module](https://geocoder.readthedocs.io/providers/ArcGIS.html#geocoding) and used it to translate each landmark into latitude-longitude coordinates. You looped through the list and printed each location's latitude and longitude, then used `arcgis` to translate the places to coordinates.

Your code should currently have this functionality:

#### Sample Test

```python
import geocoder

g = geocoder.arcgis('Redlands, California')

print(g.latlng) # `latlng` is a tuple with a length of 2.
```


#### Expected Output

```
Space Needle is located at (47.6205, -122.3493)
Crater Lake is located at (42.8684, -122.1685)
Golden Gate Bridge is located at (37.8199, -122.4783)
Yosemite National Park is located at (37.8651, -119.5383)
Las Vegas, Nevada is located at (36.1699, -115.1398)
Grand Canyon National Park is located at (36.1070, -112.1130)
Aspen, Colorado is located at (39.1911, -106.8175)
Mount Rushmore is located at (43.8791, -103.4591)
Yellowstone National Park is located at (44.4280, -110.5885)
Sandpoint, Idaho is located at (48.2766, -116.5535)
Banff National Park is located at (51.4968, -115.9281)
Capilano Suspension Bridge is located at (49.3429, -123.1149)
```


> **Hint:** We're following the pattern in the `geonames` example in the [docs](https://geocoder.readthedocs.io/results.html), but replacing `geonames` with `arcgis`.

---

## Problem 2: Heather Weather

### Skill you're practicing: Calling an API.

Cody is satisfied by geolocating his landmarks, but Heather wants to take it one step further and get the current weather at each location. Help Heather with some code that calls an API to get current weather based on latitude-longitude coordinates. Take Cody's code from Problem 1 and add an API call to [Dark Sky API](https://darksky.net/dev/register).
> Note: You will need to register an email address to get an API key, but it is free to use.

#### Directions for Dark Sky API

When you first log in to the Dark Sky API site, you will see your personal API key, as well as an example of how to use that key to make a call to the API with latitude and longitude coordinates. You can click on this sample call to see what it returns.

The data is in a form called `JSON`, which is basically a big object. You can see in your web browser what that object looks like. Unless you have a [JSON prettify plug-in](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en), it will probably look like a huge mess of data and curly braces. That's OK! Most importantly, the data we are getting includes a field called `currently`, which includes subfields `summary` and `temperature`, which together give us a pretty good idea of how we should dress for the weather.

#### Calling an API

We'll be using the [requests module](http://docs.python-requests.org/en/master/api/#module-requests) to call the Dark Sky API. Make sure to `import requests` at the top of your program.

#### Starter Code

**Note:** This new code gets put into to your previous code from Problem 1!

```python
# Import the module (top of the file).
import requests


# Make sure to replace [YOUR_API_KEY_HERE] with your actual key, which
# will look like a bunch of letters and numbers! Alternatively, copy the sample
# API call from Dark Sky dashboard and just remove the coordinates.
API_BASE_URL = "https://api.darksky.net/forecast/[YOUR_API_KEY_HERE]/"

# Previous code still here.

for point in destinations:
    # Previous `geopy` code still here.

    # full_api_url = API_BASE_URL + latitude + "," + longitude
    result = requests.request('GET', full_api_url).json()

    # From the result, print out the summary and current temperature.
```

#### Expected Output

```
The Space Needle is located at (47.6199, -122.3487)
At The Space Needle right now, it's Partly Cloudy with a temperature of 65.63
Crater Lake is located at (42.9116, -122.1483)
At Crater Lake right now, it's Clear with a temperature of 63.52
The Golden Gate Bridge is located at (37.8183, -122.4784)
At The Golden Gate Bridge right now, it's Partly Cloudy with a temperature of 59.98
Yosemite National Park is located at (37.7490, -119.5885)
At Yosemite National Park right now, it's Clear with a temperature of 83.1
Las Vegas, Nevada is located at (36.1719, -115.1400)
At Las Vegas, Nevada right now, it's Clear with a temperature of 104.72
Grand Canyon National Park is located at (36.0573, -112.1096)
At Grand Canyon National Park right now, it's Clear with a temperature of 88.37
Aspen, Colorado is located at (39.1900, -106.8182)
At Aspen, Colorado right now, it's Clear with a temperature of 86.87
Mount Rushmore is located at (43.8803, -103.4588)
At Mount Rushmore right now, it's Partly Cloudy with a temperature of 77.62
Yellowstone National Park is located at (44.9775, -110.6983)
At Yellowstone National Park right now, it's Clear with a temperature of 72.09
Sandpoint, Idaho is located at (48.2730, -116.5478)
At Sandpoint, Idaho right now, it's Clear with a temperature of 68.81
Banff National Park is located at (51.1356, -115.4073)
At Banff National Park right now, it's Partly Cloudy with a temperature of 63.91
Capilano Suspension Bridge is located at (49.3432, -123.1133)
At Capilano Suspension Bridge right now, it's Mostly Cloudy with a temperature of 65.11
```

**Hint:** In the API results, you are accessing an object called `currently`, which has properties called `temperature` and `summary`. Therefore, you can access those fields like so: `result["currently"]["summary"]`.

---

## Bonus: Format for Matt

#### Skill you're practicing: String formatting.

Matt likes Heather's idea of getting the weather for each location they plan on visiting, but he thinks the data is unreadable. Modify your code to:

1. Add a newline after each location (`\n`).
2. Add an F.
3. Add a unicode degree character.
4. Display only one decimal place on the temperature (think about string formatting).


#### Sample Code: Decimal Places Display

```python
# prints 1.23456789
print("{0}".format(1.23456789))

# prints 1.23 (2 decimal places)
print("{0:.2f}".format(1.23456789))

# prints 1.2345 (4 decimal places)
print("{0:.4f}".format(1.23456789))
```

#### Expected Output

```
The Space Needle is located at (47.6199, -122.3487)
At The Space Needle right now, it's Partly Cloudy with a temperature of 65.6° F

Crater Lake is located at (42.9116, -122.1483)
At Crater Lake right now, it's Clear with a temperature of 63.5° F

The Golden Gate Bridge is located at (37.8183, -122.4784)
At The Golden Gate Bridge right now, it's Partly Cloudy with a temperature of 60.0° F

Yosemite National Park is located at (37.7490, -119.5885)
At Yosemite National Park right now, it's Clear with a temperature of 83.1° F

Las Vegas, Nevada is located at (36.1719, -115.1400)
At Las Vegas, Nevada right now, it's Clear with a temperature of 104.7° F

Grand Canyon National Park is located at (36.0573, -112.1096)
At Grand Canyon National Park right now, it's Clear with a temperature of 88.3° F

Aspen, Colorado is located at (39.1900, -106.8182)
At Aspen, Colorado right now, it's Clear with a temperature of 86.9° F

Mount Rushmore is located at (43.8803, -103.4588)
At Mount Rushmore right now, it's Partly Cloudy with a temperature of 77.6° F

Yellowstone National Park is located at (44.9775, -110.6983)
At Yellowstone National Park right now, it's Clear with a temperature of 72.0° F

Sandpoint, Idaho is located at (48.2730, -116.5478)
At Sandpoint, Idaho right now, it's Clear with a temperature of 68.8° F

Banff National Park is located at (51.1356, -115.4073)
At Banff National Park right now, it's Partly Cloudy with a temperature of 63.9° F

Capilano Suspension Bridge is located at (49.3432, -123.1133)
At Capilano Suspension Bridge right now, it's Mostly Cloudy with a temperature of 65.1° F
```

**Hint:** Here's a list of [unicode characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters). Refer to your class notes for how to use an escape character.
---

## Done and done!

![](https://media.giphy.com/media/PqwqtOLfG19Ti/giphy.gif)
