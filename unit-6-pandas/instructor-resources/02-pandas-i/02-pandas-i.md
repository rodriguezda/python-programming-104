<!--
---
title: Pandas I
type: lesson
duration: "1:00"
creator: [Joseph Nelson](https://twitter.com/josephofiowa)
---
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Pandas I</h1>


<!--

## Overview
This lesson introduces the Pandas library and the beginnings of Exploratory Data Analysis. The majority of the lesson should be spent going through code -- whether that is via Jupyter Slides or a Jupyter Notebook demonstration.

## Learning Objectives
In this lesson, students will:
- Use Pandas to read in a dataset.
- Investigate a dataset's integrity.
- Filter, sort, and manipulate DataFrame series.


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
| 0:17 - 0:25 | Basic Pandas |
| 0:25 - 0:35 | Columns |
| 0:35 - 0:44 | Filtering and Sorting |
| 0:44 - 0:58 | Independent Exercise |
| 0:58 - 1:00 | Summary |

## Materials and Preparation
- Send out the presentation link.
- Students will need the data sets and notebook. Consider having a zip file of all notebooks and data sets for the rest of the unit that you hand out at the beginning of this lesson. Alternatively, link them directly in GitHub - remember that they haven't learned GitHub, so you'll need to help them download the files.
- The presentation is also at the top of the Notebook, so students can later reference in one place. Jump down to `Importing Pandas`.

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

## Learning Objectives
*After this lesson, you will be able to:*

- Use Pandas to read in a dataset.
- Investigate a dataset's integrity.
- Filter, sort, and manipulate DataFrame series.

<aside class="notes">
**Talking Points**:
This lesson introduces the Pandas library and the beginnings of Exploratory Data Analysis. The majority of the lesson should be spent going through code -- whether that is via Jupyter Slides or a Jupyter Notebook demonstration.

To present this content, begin with `intro-to-pandas-i.ipynb` to introduce Pandas as a library and data integrity. Transition to the Jupyter Notebook to introduce reading in data, column manipulation, filtering and sorting; conclude with exercises.

**Teaching Tips**:
- There are **Class Questions** littered throughout the notebook. Use as much/little time on these as you see fit relative to how your class is pacing
- There is an **Independent Exercise** at the end of this lesson. It is aspirational to have time to let students work entirely independently on this time-wise, so consider doing a guided code-along or paired programming. Answers are included.
- Pause after learning objectives and level-set for what students will get out of the lesson
</aside>

---

## What is Pandas?

- A group of adorable bears 🐼﻿🐼﻿🐼﻿
- A Python library for data manipulation.

<iframe src="https://giphy.com/embed/EatwJZRUIv41G" width="480" height="270" frameborder="0" class="giphy-embed" allowfullscreen=""></iframe>

<aside class="notes">
**Teaching Tips**:

- Get them excited to learn this.
- The iframe is just this gif:![](https://media.giphy.com/media/EatwJZRUIv41G/giphy.gif)
- Show your favorite Pandas gifs [Seriously](https://media.giphy.com/media/z6xE1olZ5YP4I/giphy.gif)
- Describe exploratory data analysis as an **ongoing** process, and cite an example from your experience.

**Talking Points**:

- As we learned, Python libraries are collections of functions and methods that allow us to perform lots of actions without writing as much of our own code.
- The pandas library is written specifically for data manipulation and analysis in Python
</aside>

---

## So, Pandas the Library


The Swiss Army Knife of data manipulation!

Pandas:

- Is *the* library for exploratory data analysis (EDA).
- Formats, wrangles, cleans, and prepares our data.

Quick Backstory from 2009:

- A humble open source project for Panel Data (hence "Pandas") from Wes McKinney.
- A 'panel' is the name of the object (in pandas) holding an n-dimensional numpy array
- Don't let the term fool you, a panel is effectively the same thing as an excel workbook (a collection of sheets)
- A 2-dimensional panel is a Dataframe (rows and columns)
- A 1-dimensional panel is a Series (column)

<aside class="notes">
**Teaching Tips**:

- Explain what you mean by Swiss Army knife as not all students may understand that metaphor
- Remind students of the meaning of exploratory data analysis (EDA)

**Talking Points**:

"Pandas is the most prominent Python library for exploratory data analysis (EDA). The functions Pandas supports are integral to understanding, formatting, and preparing our data. Formally, we use Pandas to investigate, wrangle, munge, and clean our data. Pandas is the Swiss Army Knife of data manipulation!"
"Pandas began as a humble open source project for Panel Data (hence "Pandas") in 2009 by Wes McKinney. It has grown to be the most use Python-related tag on Stack Overflow."
- Pandas is one of the most useful data manipulation libraries. Its utilities, on the outset, replace many things we know how to do in Excel. However, we also produce a script for creating reproducible steps **and** Excel is limited to 1.3M rows. Pandas is not.
</aside>

---

## Exploratory Data Analysis (EDA)


The process of understanding our dataset and producing our first level of insights.

This includes:

- Reading in data: "Import cat population."
- Checking data types. "Is the population count in integers?"
- Renaming columns: "`cat_breed` is more helpful than `Biological Family`"
- Joining together data: "Join the cat population data with the cat population data."
- Looking for missing data: "It doesn't mention corgis."
- And more!

Today, we will focus on the most 'mission critical' elements of EDA.


<aside class="notes">
**Teaching Tips**:

- Point out from the bulleted list what is mission critical
- Time permitting, ask students to share a similar example of a dataset

**Talking Points**:

- "Exploratory Data Analysis (EDA) is the process of understanding our dataset, and producing our first level of insights. This includes reading in the data, understanding our data dictionary, checking data types, assessing descriptive statistics, renaming columns, joining together data, looking for missing data, and so much more. That sounds like a lot, but today, we will just focus on the most 'mission critical' elements of EDA."
- It's common to get later in the data science workflow, only to realize unclean data or a feature could be engineered earlier in the process.
- Hypothesis-driven EDA is essential to productive EDA -- otherwise we will ceaselessly torture our data for answers.
</aside>

---

## Quick Review

- Exploratory Data Analysis (EDA) is the process of understanding our dataset, and producing our first level of insights.What does this include?
- Pandas is a prominent Python library used for exploratory data analysis


<aside class="notes">
**Teaching Tips**:

- Pause to gather students' answers about what EDA includes.
- Answer any clarification questions!
</aside>

---

## What dataset are we exploring?


- Adventure Works Cycles!

- We will be using a dataset developed by Microsoft for training purposes in SQL server, known the Adventureworks Cycles 2014OLTP Database. 
- It is based on a fictitious company called Adventure Works Cycles (AWC), a multinational manufacturer and seller of bicycles and accessories. 
- The company is based in Bothell, Washington, USA and has regional sales offices in several countries. 
- We will be looking at a single table from this database, the Production.Product table, which outlines some of the products this company sells.

<aside class="notes">

**Teaching Tips**:

- Open this page in a new window.

**Talking Points**:

Let's take a closer look at the data dictionary, or what is included:

ProductID - Primary key for Product records.
Name - Name of the product.
ProductNumber - Unique product identification number.
MakeFlag - 0 = Product is purchased, 1 = Product is manufactured in-house.
FinishedGoodsFlag - 0 = Product is not a salable item. 1 = Product is salable.
Color - Product color.
SafetyStockLevel - Minimum inventory quantity.
ReorderPoint - Inventory level that triggers a purchase order or work order.
StandardCost - Standard cost of the product.
ListPrice - Selling price.
Size - Product size.
SizeUnitMeasureCode - Unit of measure for the Size column.
WeightUnitMeasureCode - Unit of measure for the Weight column.
DaysToManufacture - Number of days required to manufacture the product.
ProductLine - R = Road, M = Mountain, T = Touring, S = Standard
Class - H = High, M = Medium, L = Low
Style - W = Womens, M = Mens, U = Universal
ProductSubcategoryID - Product is a member of this product subcategory. Foreign key to ProductSubCategory.ProductSubCategoryID.
ProductModelID - Product is a member of this product model. Foreign key to ProductModel.ProductModelID.
SellStartDate - Date the product was available for sale.
SellEndDate - Date the product was no longer available for sale.
DiscontinuedDate - Date the product was discontinued.
rowguid - ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.
ModifiedDate - Date and time the record was last updated.
</aside>


---

## Discussion: What Could We Examine?

- What are some potential insights you'd like to uncover given the data?

- What if you are examining it from the standpoint of a the business?

- What if you are a potential distributor of their products?

<aside class="notes">
**Teaching Tips**:

- Walk through these questions one by one. Encourage discussion - there's no wrong answer!
- For the standpoint of the business and distributor, ask why?

</aside>
---

## Our Modified Adventure Works Dataset


The full dataset is actually a large, star-schema relational databse.

We will work with a modified dataset.

Key changes:

- Only a single table from this database 
- Contains information on products the company makes
    - Such as the product names
    - The product weights, measures
    - And the product prices


<aside class="notes">

**Teaching Tips**:
- Make sure that students know this is part of a cycle company's live database, very similar to what you'd see in the real world

**Talking Points**:
- We'll be working with this, and other tables in the future
- As we join more tables together, we'll uncover more information about this business
- Encourage students to think about their work experience and how this might apply to them

</aside>

---

## Data Integrity


The first thing we check! Assuring our data can be trusted to produce meaningful insights.

Correctly formatted datatypes.

- "Decimals are floats, not strings."

Missing Data

- i.e. "Why do we only have even days of the month?"



<aside class="notes">
**Talking Points**:

- Ask how you might keep data integrity top of mind to maintain a clean data set
- Give examples here.

**Teaching Tips**:

- Pause here to ask if students have any questions
</aside>

---

## Clean Truth about Dirty Data

- Assessing data integrity isn't a one-stop step.

- Much like EDA itself, it's an ongoing process!

- We uncover additional potential problems and anomalies to remedy along the way.

<aside class="notes">
**Talking Points**:

- Ask how you might keep data integrity top of mind to maintain a clean data set
- Give examples here.

**Teaching Tips**:

- Give examples here.

</aside>

---

## Launch our notebook

We'll work in the Notebook
- We're fledgling data scientists!

The `.ipynb` file you will open is called " `intro-to-pandas-i.ipynb` ".


Open it up!

Jump down to `Import`.


<aside class="notes">
**Teaching Tips**:

- Make sure everyone gets to the notebook successfully.
- Have students assist one another and walk around the room to ensure everyone gets to the notebook successfully
- Make sure all students can open and run their Notebooks. It's only the second time they've done so!
- The presentation is also at the top of the Notebook, so students can later reference in one place. Jump down to `Importing Pandas`.
</aside>

---

## Additional Resources

- Pandas [documentation](https://pandas.pydata.org/pandas-docs/stable/)
- DataSchool [30-video series](http://www.dataschool.io/easier-data-analysis-with-pandas/) (by a former GA instructor!)
