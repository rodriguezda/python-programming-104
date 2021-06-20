<!--
title: Pandas Omdb Lab
type: lesson
duration: "01:30"
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Pandas Omdb Lab</h1>

<!--

## Overview
This lesson consists of a hands-on lab during which learners will independently create a working Python program. This lab builds on the previous lab, so starter code (which is the same solution code as the previous lab) is provided for them. You simply need to introduce the lab, make sure they have working starter code, make sure they can access the lab doc, and wait in case of questions; at the end, go over the solution. 

## Learning Objectives
In this lesson, students will:
- Apply what they've learned in Unit 6 (Pandas) to create a working Python program.


## Duration
90 minutes

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:05 | Welcome / Set up |
| 0:05 - 1:20 | Work Time |
| 1:20 - 1:30 | Q&A + Close |

## Before Class: Preparation
- Before class, complete the lab yourself to ensure you’re familiar with the solution, as well as the various challenges learners might encounter.

## In Class: Materials
- Projector
- Internet connection
- Python 3.0
- Lab directions

-->

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

## Lesson Objectives

- Apply what you’ve learned in the Pandas unit to create a working Python program.
- Wrap up the Pandas unit.
- Q&A and transition.


<aside class="notes">
**Talking Points**:

- Congratulate them on finishing unit 6!

</aside>

---

## You Do: Unit Lab - Pandas

You already have an app that prompts a user for a movie and then, looking up that movie in the OMDB API, either prints search results or finds the Rotten Tomatoes rating.

In today’s lab, you will add data analysis to that - what other information can you get? What conclusions can you make?

**Note!** This lab has two options in it:

- Option 1:
  - Use the included data set

- Option 2 (tha' danger zone):
  - Call the API yourself!
  - You must obtain an [API key](http://www.omdbapi.com/apikey.aspx) to do this!

**Open the Jupyter Notebook {`Pandas-Unit-Lab.ipynb`} see the lab and its instructions. Follow the instructions there.**

Try your best! Raise your hand if you really need help.


<aside class="notes">

75 MINUTES

**Teaching Tips**:

- Make sure that students know to start with the included dataset
  - _If there's time_, let them try to call the API themselves
  - The included Omdb.py file is a class that allows them to call the API without having to write the call themselves
  - If they feel frisky, they are welcome to modify this API call and figure out how it all works
- Stay on this slide until everyone's done or time's up!

**Talking Points**:

- Remember, throughout the course, there is a lab at the end of each unit. Each lab builds upon the last.

- Does anyone need help with the starter code?

- Right now, let's set up the functions and control flow to print out the values of our variables.

</aside>

--

## Debrief: Unit Lab - Pandas

How did it go?

Let's go over it.

Make sure you understand and your code works.

<aside class="notes">

**Talking Points**:

- Bring up the solution (in the `solution-code` directory) and walk them through it. Be sure everyone understands - and be sure everyone's code is accurate or knows that it isn't.
- The next lab builds off of this one, but provides starter code if needed.

</aside>

---

## Unit Wrap Up

What can you do?

- Apply the data science workflow.
- Use Pandas to:
    - Read in a dataset.
    - Investigate a dataset's integrity.
    - Filter, sort, and manipulate DataFrame series.
- Identify when you would use a bar chart, pie chart, scatter plot, and histogram.
    - Implement different types of graphs on a given dataset.
- Identify and handle missing values with Pandas.
- Implement `groupby` statements for specific segmented analysis.
- Use `apply` functions to clean data with Pandas.

Questions?

<aside class="notes">

5 MINUTES

**Teaching Tips**:
- Briefly review the high-level learning objectives for Unit 3.
- As you read each bullet aloud, ask students to give you a "fist to five". See **Talking Points** below.
- Observe student votes for each item, and make a mental note to follow up with individuals who are not feeling confident, or find time to reteach topics that the majority of the class is uncomfortable with.
- Take time to go over questions (but remember the parking lot).

**Talking Points**:
- Wow, we've covered a lot, and we're just getting started! Let's take a minute to review what we've learned so far.
- I'm going to read through the learning objectives for Unit 1. As I do so, I want you to tell me how confident you feel that you've mastered each one, on a scale of 0 to 5.
-- Hold up your fist to indicate 0 - you don't feel confident at all that you mastered this objective.
-- Hold up all five fingers to indicate 5 - you feel super confident. You're an expert!

</aside>
