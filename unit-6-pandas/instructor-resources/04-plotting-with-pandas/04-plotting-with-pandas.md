<!--
---
title: Plotting with Pandas
type: lesson
duration: "1:00"
---
-->

## ![](http://nagale.com/ga-python/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Plotting with Pandas</h1>


<!--

## Overview
This lesson covers plotting with pandas, which serves as a wrapper for matplotlib.

## Learning Objectives
In this lesson, students will:
- Use pandas to plot from three different datasets

## Duration
60 minutes

## Suggested Agenda

| Time | Activity |
| --- | --- |

## Suggested Agenda

|    Time     | Activity | Purpose |
|-------------|----------|---------|
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:15 | Slides |
| 0:15 - 0:17 | NOTE: Switch to Notebook |
| 0:17 - 0:25 | Line Plots |
| 0:25 - 0:35 | Bar Plots and Histograms |
| 0:35 - 0:44 | Scatter Plots |
| 0:44 - 0:58 | Independent Exercises |
| 0:58 - 1:00 | Summary |

## Materials and Preparation
- Send out the presentation link.
- Students will need the data sets and notebook. Consider having a zip file of all notebooks and data sets for the rest of the unit that you hand out at the beginning of this lesson. Alternatively, link them directly in GitHub - remember that they haven't learned GitHub, so you'll need to help them download the files.

## Differentiation and Extensions

- If students are excelling in the first half, consider deeper discussions surrounding five number summaries, data integrity, off-the-cuff filters and sorts
- If students are struggling, work on the code more heavily than the **Class Questions** portions. Make the Independent Exercises be Collective Exercises (as a class)

## In Class: Materials
- Projector
- Internet connection
- Jupyter Notebooks
- Python3
-->


---


<aside class="notes">
**Talking Points**:
This lesson introduces the Pandas library and the beginnings of Exploratory Data Analysis. The majority of the lesson should be spent going through code -- whether that is via Jupyter Slides or a Jupyter Notebook demonstration.

To present this content, begin with `04-plotting-with-pandas.ipynb` to introduce Pandas as a library and data integrity. Transition to the Jupyter Notebook to introduce reading in data, column manipulation, filtering and sorting; conclude with exercises.

**Teaching Tips**:
- There are **Class Questions** littered throughout the notebook. Use as much/little time on these as you see fit relative to how your class is pacing
- There is no **Independent Exercise** at the end of this lesson. It is aspirational to have time to let students work entirely independently on this time-wise, so consider doing a guided code-along or paired programming. Use this time to have students set their own challenges.
- Pause after learning objectives and level-set for what students will get out of the lesson
</aside>

---

## A Note on Delivery

- This unit's lessons will occur in [jupyter notebooks](http://jupyter.org/)
  - Slides will be an introduction to the lesson (no code, just overview)
  - Then, we'll open a notebook and start coding!

<aside class="notes">
**Teaching Tips**:
- We could have made this into a speaker note, but it's helpful to get it out there so everybody's on the same page
- No repl.it for this unit as we'll be in notebooks

</aside>

---

## Plotting with Pandas

- Pandas `.plot()` functionality is effectively a wrapper for [matplotlib](https://matplotlib.org/)
- Matplotlib is a charting library for python and scientific computing
- It's considered the de-facto standard for charting locally
  - It's best for scientific papers, EDA, and general introspection of data
  - It's not so great for production level charts that are embedded in applications (check out [d3.js](https://d3js.org/)

<aside class="notes">
**Talking Points**:

- Talk briefly about where charts are interpreted, and why different tools may be advantageous
</aside>

---

## So, Pandas and Matplotlib


Whats a wrapper?

- A program that _abstracts_ another program to modify its interface

???

- Pandas `.plot()` functionality references matplotlib behind the scenes
- Matplotlib has a reputation for being fairly complex
  - Even for fairly simple charts, you will frequently write loops
  - A fairly plain chart can be 20-30 lines of code
- Pandas helps us here and most charts can be produced with 1-2 lines of code
  - Some functionality is reduced, but _effort is minimized in most cases_

<aside class="notes">
**Talking Points**:

- Encourage students to learn matplotlib on their own time if they wish
- Many data science shops use matplotlib as a standard
  - It's a bit older and a little hokey, but it's well supported, open source, and generally gets the job done
- Take some time to talk about the balance between package complexity and utility overall - sometimes a good answer delivered on time beats a perfect answer delivered late

</aside>

---

## Talk Data to Me


We'll be using three data sets for this lesson:

- Football Records: International football results from 1872 to 2018
- Avocado Prices: Historical data on avocado prices and sales volume in multiple US markets
- Chocolate Bar Ratings: Expert ratings of over 1,700 chocolate bars

All datasets have been graciously downloaded from Kaggle.com, and we'll discover that the right visualization can often replace a bit of fancy machine learning, if done properly.

<aside class="notes">
**Talking Points**:

- We'll be walking through the data sets during the lesson, feel free to refer to the links there if you wish.

</aside>

---

## Chart Types

We'll be covering the following chart types during this lesson:

- Time series line charts
- Categorical bar charts
- Histograms of single columns
- Histograms of entire data frames
- Scatter plots (continuous vs continuous)
- Scatter matricies (multiple scatter plots in a grid)
- Scatter plots with class colors for data points

<aside class="notes">
**Teaching Tips**:

- This is the tip of the iceberg for plots, that's okay
- Assure students that the above charts have been selected specifically to cover the majority of cases you'll encounter
- Take a minute to talk about the common use cases for each of these, as well as the data types they all prefer

</aside>

---

## Let's Go!


- Open up your dataset!

<aside class="notes">
**Teaching Tips**:

- Make sure everyone gets to the notebook successfully.
- Have students assist one another and walk around the room to ensure everyone gets to the notebook successfully
- Make sure all students can open and run their Notebooks. It's only the second time they've done so!
- The presentation is also at the top of the Notebook, so students can later reference in one place. Jump down to `Importing Pandas`.
</aside>

---
