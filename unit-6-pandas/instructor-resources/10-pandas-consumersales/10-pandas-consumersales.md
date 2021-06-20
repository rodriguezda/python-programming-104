<!--
---
title: Pandas Consumer Sales Lab
type: lab
duration: "1:00"
---
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Pandas Consumer Sales Lab</h1>

<!--

## Overview
This lab makes use of the datetime and joining capabilites of pandas. Make sure you review those topics first.

## Important Notes or Prerequisites

- There are **Class Questions** throughout the notebook. Use as much/little time on these as you see fit relative to how your class is pacing
- This lesson includes high level slides and a Notebook. To present this content, it is recommended you begin directly with the Jupyter Notebook. The student slides contain the wrap-up of the big ideas covered in the notebook.

---

## Learning Objectives
*After this lab, you will be able to:*

- Apply what you've learned in the datetime and joining lessons to a real dataset
- Apply your charting experience to visualize insights based off of your EDA'd data

## Duration
60 minutes.

---

## Suggested Agenda

|    Time     | Activity | Purpose |
|-------------|----------|---------|
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:55 | Exercise |
| 0:55 - 1:00 | Summary |

## Materials and Preparation
- Send out the link to the presentation slides, and help students download the Notebook.

## Differentiation and Extensions

- This lab/exercise may be difficult for some struggling students
- There is really no limit to the amount of work you can do here either - if students are struggling, encourage them to produce tabluar results on a subset of the tables given
- If students are excelling, push them to create more complex (and even interactive) visualizations
- A solution notebook is provided to show some examples of what can be done with pandas, .plot extension of pandas

-->

---

## Learning Objectives
*After this lesson, you will be able to:*

- Apply what you've learned in the datetime and joining lessons to a real dataset.
- Apply your charting experience to visualize insights based off of your EDA'd data.

---

## To the notebook!

We actually will commence this lesson directly in the Jupyter Notebook, `pandas-consumersales.ipynb`, to walkthrough the what, why, and how all at once.

Here we have slides reviewing the key concepts.

<aside class="notes">

**Teaching Tip**:

- This is an intro to the notebook - use it as an overview to cover the concepts. Budget time accordingly.

</aside>


---

## Exercise Overview

- First, this exercise can easily take more than 60 minutes.
- Think of this as an opportunity to dive into the topic and apply datetime and joining operations to a real dataset.
- Budget time _outside of class_ to continue work on this if you can:
  - Remember, the more comfortable you become with this, the more likely you'll use it in your day-to-day life!

<aside class="notes">

**Teaching Tip**:

- Refer to the lesson overview about time management here

</aside>

---

## Data Background

- This exercise uses a dataset originally used for [qlik](https://sense-demo.qlik.com/sense/app/372cbc85-f7fb-4db6-a620-9a5367845dce).
- If you want, try clicking (pun intended) around in their web-based solution to familiarize yourself with the data.
- This is a global food distribution company (canned goods, produce, meats, etc.).
- The data you have about their sales and inventory is distributed across multiple sheets, and even in different languages!
- This is an exercise _very_ similar to what you'd be doing with relational databases with a larger enterprise company.

<aside class="notes">

**Teaching Tips**:
- Talk to students telling them that this is effectively a small, star-schema transactional database dump.
- Pretty much exactly what you'd have as a sales data warehouse for a mid-size enterprise company.
- The dataset covers about 2 years of sales data.
- It's not too big, not too small.

</aside>

---

## What Are We Looking For?

- Your boss, Joanna, has requested a report on the following:
  - Product Sales
    - Margin analysis, by region, by product group.
  - Sales by product group
    - Sales, and budget, year over year
  - Sales Reps
    - Sales and sales quantity, by rep, by customer
  - Supply Chain
    - Inventory vs. Lead Time for all products

<aside class="notes">

**Teaching Tips**:

- Remind students that these questions are intentionally open-ended.
- The notebook is designed to help students step-by-step to make a fully joined dataset.
- After that, the training wheels come off and they are forced to navigate the joined set to answer these questions.
- Be sure to frame the exercise as something that likely will take them longer than 60 minutes to complete to their satisfaction - that's OK!

</aside>

---

## Additional Resources

- Pandas [documentation](https://pandas.pydata.org/pandas-docs/stable/)
- DataSchool [30-video series](http://www.dataschool.io/easier-data-analysis-with-pandas/) (by a former GA instructor!)
- Qlik [Consumer Sales Dataset](https://sense-demo.qlik.com/sense/app/372cbc85-f7fb-4db6-a620-9a5367845dce)
