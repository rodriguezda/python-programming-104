<!--
---
title: Pandas Datetime
type: lesson
duration: "0:45"
---
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Pandas Datetime</h1>

<!--

## Overview
This is an intro to the notebook - use it as an overview to cover the concepts. Budget time accordingly.

## Important Notes or Prerequisites

- There are **Class Questions** littered throughout the notebook. Use as much/little time on these as you see fit relative to how your class is pacing
- This lesson includes high level slides and a Notebook. To present this content, it is recommended you begin directly with the Jupyter Notebook. The student slides contain the wrap-up of the big ideas covered in the notebook.


---

## Learning Objectives
*After this lesson, you will be able to:*

- Handle timeseries data in pandas
- Convert dates and times into a Timestamp object using to_datetime
- Specify input and output format arguments
- Extract components, such as year and day, from a Timestamp object
- Create DatetimeIndex objects, and understand their advantages
- Implement groupby statements for specific segmented analysis
- Use apply functions to clean data with Pandas

## Duration
45 minutes.

---

## Suggested Agenda

|    Time     | Activity | Purpose |
|-------------|----------|---------|
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:08 | Datetime Objects |
| 0:08 - 0:11 | Timestamp and Period Objects |
| 0:11 - 0:25 | Converting Datetime Objects |
| 0:25 - 0:30 | Handling Nulls |
| 0:30 - 0:40 | Exercise |
| 0:40 - 0:45 | Summary |

## Materials and Preparation
- Send out the link to the presentation slides, and help students download the Notebook.

## Differentiation and Extensions

- If students are excelling in the first half, consider deeper discussions.
- If students are struggling, hone the conceptual elements of each portion heavily - the **why**. Note that the order of these lessons is in order of importance, so even if the latter half is rushed, students will still be covering the major points.

-->

---

## Learning Objectives
*After this lesson, you will be able to:*

- Handle timeseries data in Pandas
- Convert dates and times into a Timestamp object using `to_datetime`
- Specify input and output format arguments
- Extract components, such as year and day, from a `Timestamp` object
- Create `DatetimeIndex` objects, and understand their advantages
- Implement `groupby` statements for specific segmented analysis
- Use apply functions to clean data with Pandas

---

## To the Notebook!

We will actually commence this lesson directly in the Jupyter Notebook, `pandas-datetime.ipynb`, to walk through the what, why, and how all at once.

Here we have slides reviewing the key concepts.

<aside class="notes">

**Teaching Tip**:

- This is an intro to the notebook - use it as an overview to cover the concepts. Budget time accordingly.

</aside>

---

## How Do We Handle Timeseries Data (Dates and Times)?

To handle timeseries data, we must:

- Import the data (usually as a string)
- Convert the data into a `Timestamp` object
- Handle missing values (sometimes)
- Understand how to slice and handle this `Timestamp` object

**Pro tip:** Timeseries information is very common in the financial industry (fintech/trading, etc).

<aside class="notes">

**Teaching Tip**:

- Do a quick recap and check for understanding.

</aside>

---

## A Note on Delivery

- This unit's lessons will occur in [jupyter notebooks](http://jupyter.org/)
  - The slides will be an introduction to the lesson (no code, just overview)
  - Then, we'll open a notebook and start coding!

<aside class="notes">
**Teaching Tip**:
- We could have made this into a speaker note, but it's helpful to get it out there so everybody's on the same page
- No repl.it for this unit as we'll be in notebooks

</aside>

---

## Why use Timeseries Data?

**Timestamp** objects in pandas allow us to conduct analysis on _chronological data_.

![](http://pandas.pydata.org/pandas-docs/version/0.13/_images/series_plot_basic.png)

- What's the X axis unit of this chart?
- What's the ordering of the data?

<aside class="notes">

**Teaching Tips**:

- Reinforce that chronological data has an inherent order
- This is intuitive to a human, but a computer needs more help
- Timestamp objects handle things like leap years, working days, holidays, etc

</aside>

---

## Key Pandas Function for Converting to Timestamp Objects:

```python
Signature: pd.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, box=True, format=None, exact=True, unit=None, infer_datetime_format=False, origin='unix', cache=False)
Docstring:
Convert argument to datetime.
```

1. Read in the dataset using `pd.read_csv()`
2. Use `pd.to_datetime(df['myColumn'])`
3. The returned `pd.Series` object will be converted to a Timestamp object!

<aside class="notes">

**Teaching Tip**:

- Do a quick recap and check for understanding.

</aside>

---

## Things to Look Out For

**`to_datetime`** allows us to convert from string values to datetime values.

- Most of the time, it works very nicely
- At the end of the day, it's just a string parser
- Keep this in mind - always check the output column for `NaT` values
  - These are values that `pd.to_datetime` isn't able to convert
  - Make sure you have elegant, automated ways of handling/flagging these scenarios
  - One example may be a separate column flag, and a backfill/forwardfill strategy

<aside class="notes">

**Teaching Tip**:

- Do a quick recap and check for understanding.

</aside>

---

## Why Does This Matter?

![](http://gazetemege.com/wp-content/uploads/2015/11/Database-Normalization.jpg)

- Storing datetime information in a database (dataframe) as a string:
  - is very space inefficient
  - doesn't allow us to easily _extract_ information from it (see 3NF image above)
  - doesn't allow us to use linear algebra library (numpy!) advantages
    - _Note_: Timestamp (datetime) pandas objects are numpy objects!

<aside class="notes">

**Teaching Tips**:

- Don't get too hung up on this diagram
- Focus on reduction in redundancy in databases, and how a single Timestamp object allows _derivation_ of all other types (workdays, years, weeks, etc) - from a single object

</aside>

---

## Additional Resources

- Pandas [documentation](https://pandas.pydata.org/pandas-docs/stable/)
- DataSchool [30-video series](http://www.dataschool.io/easier-data-analysis-with-pandas/) (by a former GA instructor!)
