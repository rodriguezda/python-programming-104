### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Brandi

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack at @brandib.
--->

# Python Modules, Packages, and APIs: Practice Problems, Part 1

In this homework, you're going to write code for a challenge problem.

You will practice these programming concepts we've covered in class:

* Including and using modules and packages

**Note:** This homework is Part 1 of a two-part assignment. Save your solution code — the next homework will build off of it!

---

## Deliverables

This homework will be a two-part code challenge with a bonus. It will be a little different than the other homework because Part 2 will build on the code from Part 1. You can put all of your code in one file called `solution.py`. Right now, just make that one file.

*Reminder: On your laptop, you can run the file from your command line with the following:*

```python
python solution.py
```

> **Hint:** Make sure you are printing something out with the `print` statement. Otherwise, you won't see any output from running your program!


## Requirements:

By the end of this, you should have:
* A file called `solution.py` with your code from this challenge.

---

# Code Challenges

## Problem 1: Geo Cody

### Skill you're practicing: Importing and using modules/packages.

Cody and his friends Heather and Matt are going on a road trip across the Western United States and Canada. They want to visit several landmarks, national parks, and big cities. Here's their agenda:

```
Space Needle
Crater Lake
Golden Gate Bridge
Yosemite National Park
Las Vegas, Nevada
Grand Canyon National Park
Aspen, Colorado
Mount Rushmore
Yellowstone National Park
Sandpoint, Idaho
Banff National Park
Capilano Suspension Bridge
```

Your job is to put these destinations into a list of strings called `destinations`. Then, import the [geocoder module](https://geocoder.readthedocs.io/providers/ArcGIS.html#geocoding) and use it to translate each of the landmarks into latitude-longitude coordinates. You'll need to loop through the list and print each location's latitude and longitude. We will be using `arcgis` to translate the places to coordinates. Visit the [docs](https://geocoder.readthedocs.io/results.html) for more sample code.

#### Sample Code (`geocoder`/`arcgis`)

```python
import geocoder

g = geocoder.arcgis('Redlands, CA')

print(g.latlng) # latlng is a tuple with a length of 2.
```

#### Starter Code

```python
import geocoder

# Declare destinations list here.

# Loop through each destination.
for point in destinations:
#   Get the lat-long coordinates from `geocoder.arcgis`.
#   Print out the place name and the coordinates.
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


> **Hint:** We're following the pattern in the `geonames` example in the [docs](https://geocoder.readthedocs.io/results.html), only replacing `geonames` with `arcgis`.

---

## Done and Done!

![](https://media.giphy.com/media/PqwqtOLfG19Ti/giphy.gif)
