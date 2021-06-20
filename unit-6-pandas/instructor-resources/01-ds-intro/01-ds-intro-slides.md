<!--
---
title: Intro to Data Sicence
type: lesson
duration: "1:00"
creator: Joseph Nelson
---
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Intro to Data Science</h1>


<!--

## Overview
This lesson introduces data science and its workflow, then jumps into a workflow exercise. It includes downloading Anaconda on student machines, so they're ready for the day's content.

## Important Notes or Prerequisites
When it comes to installing Anaconda, it's important to be prepared to handle Mac v Windows across student machines. It is a good idea to delegate one IA to be the "PC person" for debugging said issues.

There are significant **Talking Points** in the slide file's comments - read through them!

## Learning Objectives
In this lesson, students will:
- Apply the data science workflow.
- Have a set up data science development ecosystem, specific to Python


## Duration
60 minutes

## Suggested Agenda

| Time | Activity |
| --- | --- |

## Suggested Agenda

|    Time     | Activity | Purpose |
|-------------|----------|---------|
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:15 | Data Science |
| 0:15 - 0:40 | Data Science Workflow |
| 0:40 - 0:57 | Data Science Development Tools |
| 0:57 - 1:00 | Summary |

## Materials and Preparation
- Send out the link to the presentation slides to students.
- Install Anaconda on your own computer.
- Consider reading GA's definitions of data science [blog post](https://theindex.generalassemb.ly/why-we-need-to-redefine-data-science-7f05ab0286d4) in advance of defining data science roles. It is also linked in resources. While going through the roles in depth is non-essential, they provide useful context for students.

## Differentiation and Extensions

- If students are excelling in the first half, consider accelerating the flow or introducing your own (more complex) data science workflow problem, like breaking down (at a high level) the Netflix recommendation algorithm.
- If students are struggling, emphasize that many of the topics discussed will be reintroduced throughout the day's exercises. Lean on real world examples!

## In Class: Materials
- Projector
- Internet connection
- Python3
- Anaconda
-->


---

## Learning Objectives
*After this lesson, you will be able to:*

- Apply the data science workflow.
- Have a set up data science development ecosystem, specific to Python

<aside class="notes">
**Teaching Tips**:

- Introduce topic and learning objectives
- Pause after learning objectives and level-set for what students will get out of the lesson
</aside>

---

## What is Data Science?

- The Harvard Business review called the industry the 'sexiest job of the 21st century'.

- Glassdoor determined the profession to be among the most desirable in 2016 and 2017.

Sounds cool, right? But... what is it?

<aside class="notes">

**Teaching Tips**:
- Don't spend long on this slide. The idea here is to get them intrigued.
</aside>

---

## Data Science Examples

- Netflix recommendation engine.
- Apple FaceID determining if a photo contains your face.
- A bank approving a credit card.

Common thread:

- All leverage data to make decisions.

**Class Question:** What is an example of data science you have heard of? What about your stated example makes it be, well, data science?

<aside class="notes">
**Talking Points**:

- Discuss how data is leveraged to make decisions in one of the above examples
- Add in other examples if you have personal ones to share
- Encourage the class to participate and throw out examples of data science in the real world. The more comfortable the class feels making guesses and making the content relatable to their life at this point, the more engaged they will be throughout the lesson.

**Teaching Tips**:

- Encourage students to think about why a given example is or is not data science.
- Ask why, and what makes a given example data science?
</aside>

---

## Data Science Definition

Compliments of GA's Standard Board:

> Data science is the practice of: acquiring, organizing, and delivering complex data; discovering relationships and anomalies among variables; building and deploying machine learning models; and synthesizing data to influence decision-making.


**tl;dr:** Data scientists:

- Use data of all kinds (numbers, text, images).
- Make explanations and predictive decisions.


<aside class="notes">
**Teaching Tips**:
- This is a mouthful! Summarize it; don't read it!

**Talking Points**:
- Define data science and associated roles.
- Explain predictive decisions are broadly leveraging data about prior events to inform future strategy
- Encourage the class to participate and throw out examples of data science in the real world. The more comfortable the class feels making guesses and making the content relatable to their life at this point, the more engaged they will be throughout the lesson.
</aside>

---

## Conway Venn Diagram

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/Data_Science_VD.png)

<aside class="notes">
**Talking Points**:

- Note that data science lives at the intersection of computational skills ('hacking skills'), traditional statistics and mathematics skills, and subject matter expertise. A data scientist must be able to leverage maths/stats to develop models, computation skills to efficiently use those models, and subject matter competence to structure a problem and contextualize results.

**Teaching Tips**:

- Point out where data science sits compared to say, Machine Learning
- Pause to ask for questions here
</aside>

---

## Specific Data Scientist Roles

What does that break down to?

- Machine Learning Engineer
- Data Engineer
- Research Science
- Advanced Analyst

<aside class="notes">
**Teaching Tips**:

- Ask if students have any questions about what these roles might do?
- Let students know we will be covering these roles more in depth in the coming sections
</aside>

---

## Machine Learning Engineer

- Identify machine learning applications.
- Work in production code.
- Manage infrastructure and data pipelines
- “Straddle the line between knowing the mathematics and coding the mathematics.”
    - eBay VP of engineering Japjit Tulsi

<aside class="notes">
**Teaching Tips**:

- Define production code, infrastructure, and data pipelines
- Put emphasis on the quote especially on the, "between knowing the mathematics" and "coding the mathematics"
</aside>

---

## Data Engineer

- Create the architecture that allows data acquisition and machine learning problems to run at scale.

- Focus on the algorithm and the analysis.

- Don't work much on the software side.

<aside class="notes">
**Teaching Tips**:

- Ask students if they know what "at scale" might mean
- Explain algorithm and analysis
</aside>
---

## Research Scientist

- PhD-heavy field.
- Determines new algorithmic optimizations.
- Focused on driving scientific discovery.
- Less concerned with pursuing industrial applications.

**Applied research scientists**:

- Specialized research scientist.
- Backgrounds in both data science and computer science.
- Invaluable members of any AI team.
- “They can both pitch in on data science and write code. Finding a good applied research scientist is worth her weight in gold.
    - Japjit Tulsi

<aside class="notes">
**Teaching Tips**:

- Explain algorithmic optimizations
- Describe a problem a research scientist might be interested in
</aside>

---

## Advanced Analysts

- Quantitative-minded.
- Apply data descriptive and inferential exploratory data analysis and modeling.

<aside class="notes">
**Talking Points**:

- Explain that exploratory analysis is an approach to analyzing data sets to summarize their main characteristics.

**Teaching Tips**:

- Pause and ask if there are any questions about this role.
</aside>

---

## Quick Review


Data science is the practice of:

- Acquiring, organizing, and delivering complex data; discovering relationships and anomalies among variables.
- Building and deploying machine learning models.
- Synthesizing data to influence decision-making.

Specific Data Science Roles Include:

- Machine Learning Engineer
- Data Engineer
- Research Science
- Advanced Analyst


<aside class="notes">
**Teaching Tips**:

- Run through the definition again and pause in case there are any questions.

**Talking Points**:

- Just like after the rise of .com era where there was first just one "webmaster" that became a front-end developer, back-end developer, etc. Data science is going through a similar period of industry fragmentation where roles that were just "data scientist" are now broken up into specialities.
</aside>

---

## How Do We...


- Go through data science workflow?
- Solve a data science problem?
- Craft a data science problem statement?


<aside class="notes">
**Talking Points**:

- In today's lessons, we will focus on how to conduct exploratory data analysis for the purposes of structuring and solving a data science problem. With this in mind, let's transition to defining how to craft a data science problem statement.

</aside>

---

## The Data Science Workflow


![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/Data-Framework-White-BG.png)


**Class Discussion:** Which step do you believe will be most challenging?

- There's no objectively correct answer!

<aside class="notes">
**Teaching Tips**:

- Draw the workflow on the board to reference.
- Keep the example dataset open in a new tab.
- Focus on the importance of defining a question, especially following the first class discussion of which workflow component is most challenging
- Consider thinking through your own work, and anchoring the discussion of the workflow steps against that example to reduce abstraction
- Make the step-by-step exercise engaging at every component. Let the class guide the problem you want to solve. If you'd like, you can encourage them to converge on a single problem statement you feel most comfortable with discussing (like those below)
- You may consider running the whole exercise as unstructured time, or guiding step-by-step. Step-by-step is recommended to assure learners remain on task and do not get stuck.

**Talking Points**:

- While the data science workflow is presented as five sequential steps, reinforce data science is often recursive among these areas. When an analysis yields an unexpected result, you may revisit the preparation of data to assure the steps were handled properly.
- Defining a question and tying work against an objective is essential to emphasis because problems that progress without a hypothesis to prove or disprove ultimately become circular. There are a near infinite number of spurious correlations or "interesting" ideas to consider. Only those that further drive you towards on outcome are necessary.
- There are caveats to this process. Note the area labeled "_these steps are not hard-set rules._"

- **Frame:** Assure students first, identify what factors affect cost. Then, consider how those costs can be reduced. Finally, hypothesize a way to describe or predict if those given factors can be reduced.
- **Prepare:** Encourage learners to consider data integrity. A few easy points to call out: differing ways of reporting "No" (`N` and `No`) and missing values (`NA`). Reassure students that it is quite common to have datasets where the ground truth answers to questions like these are unknown.
- **Analyze:** Reinforce the importance of data preparation and connecting analyses to the initial question with analysis.
- **Interpret:** Restate the hypothesis you are aiming to prove or disprove. Identify if the limited dataset provides you with anecdotes to validate or invalidate that statement.
- **Communicate:** Provide your best communications tips, written and verbal alike. These persist when using data.

</aside>

---

## Notes on the Steps

- Not hard-set rules.
- Really, problem-solving guidelines.

Every problem's different!

- Some projects may not require every step.

- It's normal to repeat certain steps a few times.

- The process is cyclical with new findings!

<aside class="notes">

**Talking Points**:

A recommended problem is like the following:

- **Frame:** Let's presume the key cost driver for this HR function is twofold: employees turning over early (low total years of service) and a high time to fill (positions going unfilled, costing producitivity losses). We'll aim to minimize turnover. Let's hypothesize we can explain how long an employee stays with the company based on their university, previous employment, and how they found our retail store, Data Science Wearables (DSW).
- **Prepare:** We would want to create a consistent data standard for `Current Employee` -> `No` to `N` across the dataset. Moreover, we need to hypothesize why `NA` values exist. E.g. did the second candidate not have a previous employer, or was this data unavailable? (We do not know with the information given.)
- **Analyze:** While we will dive deeper into analysis using Python soon enough, anecdotal evidence based on three observations seems to imply that Candidate Source is a useful explanatory variable. Employees that had experience with DSW previously (`Internship` and `Referral`) stayed longer. The relationship between waiting to fill (`Time to Fill (Days)`) and employee tenure may make a U-shape: an employee either previously knows of DSW (short time to fill)  and stays for a while because they liked it or DSW waited for the perfect candidate (long time to fill) and stayed for a while. School does not seem to have useful signal for employee tenure.
- **Interpret:** It appears many of our explanatory factors helped, but not all, and not in ways we may have anticipated. `School` does not seem to yield valuable insight, but knowing an employee has been referred or had experience with DSW previously is a key signal. Perhaps DSW should expand their internship and employee referral programs.
- **Communicate:** Our driving thesis is: The best candidates for DSW are those that have connected with the store in a previous way (internship, referral). Investing in these programs is recommended. Visualizations of average employee tenure segmented by these factors are encouraged.


</aside>
---

## Step 1 is Always "Frame the Problem"

Solving data science task starts with a clearly defined problem.

- Poor results stem from no defined goal.

_“A problem well stated is half solved.”_ — Charles Kettering

From there, you can apply your steps.

<aside class="notes">
**Talking Points**:

- Even though all data science projects have different general flows, they start in the same place: with a problem. From this problem statement arises questions; questions we will ask the data in order to gain more information so we can attempt to find a solution to that problem.

- Let's restate that: **solving data science task starts with a clearly defined problem.** Too often, situations will lack a driving objective. Haplessly exploring data without a determined goal produces poor results.

</aside>

---

## The Data Science Workflow: Applied

You need to reduce the costs of staffing.

You have a table of DSW current retail sales associates across department stores.

The first three rows look like this:

| Job Level | Current Employee | Reason for Termination | Years of Service | Candidate Source | Previous Employer      |          School         | Time to Fill (Days) |
|---|---|---|---|---|---|:---:|---:|
| Associate | N                | New offer            | 1.5              | Referral         | Jake's Hawaiian Shirts | University of Minnesota |                  40 |
| Associate | Y                | N/A                   | 2.0              | Internship       | N/A                     | University of Iowa      |                  15 |
| Associate | No               | Tardiness            | 0.5              | Online           | Hats and Caps          |  University of Nebraska |                  25 |

<aside class="notes">

**Teaching Tips**:

- We'll be referring to this scenario a lot in the next few slides - keep this open or write it on the board.

**Talking Points**:

- Let's apply our workflow above to an interactive exercise. A given clothing retail company, Data Science Wearables (DSW), is interested in improving their human resource operations. Specifically, as a cost center in the business, this company wants to reduce their expenses associated with staffing the firm's in-store associates across the United States.


- **Job Level:** The role level. Our dataset is all current or former associates.
- **Current Employee:** If the individual is a current employee, this is a "Y" otherwise "N"
- **Reason for Termination:** If the employee no longer works at the retail store, this is why they left
- **Years of Service:** How long did the employee work at DSW?
- **Candidate Source:** Where did this employee learn of DSW?
- **Previous Employer:** Where did the employer previously work?
- **School:** Which university did the individual attend?
- **Time to Fill (Days):** How long did it take to fill this person's role? Typically minimizing time to fill is key to lower costs.
</aside>

---

## Step One: Frame

We know:

- We want to reduce costs associated with staffing.

We don't know:

- What drives up costs of staffing?
- Is there an underlying reason for those costs?
- What hypothesis can we test to reduce costs?

**Class Discussion:** What factors affect HR costs? How could we minimize these?

<aside class="notes">

**Teaching Tips**:

- Through each of these following slides, check for understanding. Point to the workflow on the board and remind students where we are; prompt a discussion and ask what they think the step should include.

</aside>

---

## Step Two: Prepare


**Class Question:** What questions do you have about the dataset?

| Job Level | Current Employee | Reason for Termination | Years of Service | Candidate Source | Previous Employer      |          School         | Time to Fill (Days) |
|---|---|---|---|---|---|:---:|---:|
| Associate | N                | New offer            | 1.5              | Referral         | Jake's Hawaiian Shirts | University of Minnesota |                  40 |
| Associate | Y                | N/A                   | 2.0              | Internship       | N/A                     | University of Iowa      |                  15 |
| Associate | No               | Tardiness            | 0.5              | Online           | Hats and Caps          |  University of Nebraska |                  25 |


<aside class="notes">
**Talking Points**:

- These inconsistencies, and `N/A` missing values are incredibly common. In fact, this dataset is comparatively clean and apt for the task at hand vis a vie many datasets that may otherwise be available. In future classes, we will discuss how to handle `N/A` missing values and the additional importance of checking data integrity.
</aside>

---

## Step Three: Analyze


We want to:

- Create meaning and conduct statistical description and inference.

For example, the average Years of Service is ~1.33 years.

  - Could we build a machine learning model to predict this?
  - The data could center on their background (school, previous employers, and application source).

For example, is the relationship between Time to Fill and Years of Service positive or negative?

  - Positive: when one increases, the other increases.
  - Negative: when one increases, the other decreases.


<aside class="notes">
**Talking Points**:

- For example, the average Years of Service in this given dataset is (1.5 + 2.0 + 0.5)/3 = 4/3 ≈ 1.33 years. In more complex situations, we may build a machine learning model to predict a given outcome. For example, we may want to predict how long a given candidate will stay in their role based on their background (school, previous employers, and application source).

- We may also be interested in visualizing relationships between our variables/columns. For example, do we anticipate that the relationship between Time to Fill and Years of Service is positive (when one increases, the other increases) or negative (when one increases, the other decreases)? Considering questions like this help us approach the true explaining factor.

- It is common for this step to reinforce and revisit the prior step as we discover anomalies or intriguing relationships.

</aside>

---

## Step Four: Interpret

How do our results compare to our initial hypothesis?

What concrete actions do we recommend?

**Class Question:** Even with an extremely limited dataset (`n=3`), can you identify hypothesis-validating or invalidating anecdotes?

At this stage, treat metrics and results like "check engine lights."

- Result summaries may point you in the right direction, but they do not necessarily explain the full context at hand.

<aside class="notes">

**Teaching Tips**:

- Encourage discussion. They likely don't know! Be encouraging and guide them.
- Remind them all that's been discussed on this up through now.

</aside>

---

## Step Five: Communicate


Results are only as convincing as they are conveyed to key stakeholders!

Back up your statement with evidence, including statistical tests, visualizations, and model results.


<aside class="notes">
**Talking Points**:

- Results may be only as convincing as they are conveyed to key stakeholders. The process of communication requires honing a cohesive narrative that establishes a thesis and includes evidence to back up said statement. Backing up the statement includes statistical tests, visualizations, and model results.

- The best practices you may have heard in prior written and verbal exercises equally apply to communicating with data. Rather than viewing data as a separate entity altogether ("I'm not a data person"), consider how data can aid your existing thesis.
</aside>


---


## Quick Review


The data science workflow:

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/Data-Framework-White-BG.png)

<aside class="notes">
**Teaching Tips**:

- Pause and check for understanding.

</aside>

---

## Why Python for Data Science

Easy to write

- Data science is inherently a cross-functional discipline!
- A language for all audiences is key.

Open source

- New techniques become available daily!
- Developers from around the world race to implement new libraries.
- This places Python in contrast to closed source, paid data analysis tools like SAS and SPSS.

Often used for data analysis, scripting, and rapid software development.


<aside class="notes">
**Talking Points**:

- For the first portion of this week, you've focused on learning the fundamentals of Python. Why do we (and the community) emphasize Python as a choice language for data science?

- For starters, let's return to a buzzword-heavy and unofficial Python definition

- Let's break down these definitional attributes and discuss their impact on Python being a common language for data:

- **High level:** Python is _"far from"_ our computer's RAM and CPU, meaning it is less like binary (`01101010`) and closer to plaintext English. This makes Python comparatively more intuitive as a first language. Because data science is inherently a cross-functional discipline, allowing it to be picked up by all audiences is key.

- **Open source:** Python's source code is free to use, and anyone can contribute to improve it. Being an open source language is a huge reason Python is a choice language for data science. As new techniques become available daily, developers from around the world race to implement said methods in Python libraries. (This places Python in contrast to closed source, paid data analysis tools like SAS and SPSS.)

- **Object-oriented:** You learned how to create objects and classes for reproducible use cases. Object-oriented languages are generally more familiar for introductory content, lending a helping hand to Python being approachable.

</aside>

---

## Getting Data Science Tools

- We can analyze data to determine what Python is most used for:

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/related_tags_over_time.png)

- Pandas?
  - A Python package for exploratory analysis.
  - Let's use it!

<aside class="notes">

**Teaching Tips**:

- Remind them that a package is a module - it's code we can use.
- Talk about how common Pandas is in data science.
- Get them excited to learn it!

</aside>

---


## You Do: Your Data Science Development Tools


Python packages in DS are ubiquitous:
-  Reading CSVs, linear algebra, linear regressions, matrices...

**Anaconda** ("Conda"):
- Package manager.
- Downloads everything for us!

Follow these steps:

1. Download [Anaconda](https://www.anaconda.com/download/): `https://www.anaconda.com/download/`. Select Python 3.6+ for your machine (macOS or PC)

2. Open the file. Follow the on-screen prompts. Don't hesitate to ask questions!

Please wait once you have successfully installed Anaconda.


<aside class="notes">
**Teaching Tips**:

- Emphasize that Python has _packages_ as the reason why we see it being a choice language for data science. Connect that packages are the result of Python being an open source technology.
- Work with your IAs to debug and assist students as complications (inevitably) pop up. Be sure everyone can successfully explain why we use packages, install Anaconda, and open a Jupyter Notebook.
- With the Notebook, go **step-by-step** with all students. Do not encourage them to skip ahead of where you want them to be. (e.g. when they finish download, clearly tell them when to click through all install instructions. Stop and wait for further instruction.)
- Delegate one IA to be the Windows or Mac person, and you take the other. Typically, Macs are more represented in these classes, so it makes most sense for the instructor to be the lead on Mac, and a IA to be the Windows person.

**Talking Points**:

- Notice that when we use Python for data science, we are heavily relying on a open source packages. Python packages are Python scripts that allow us to easily performance reproducible actions.

- For example, when we in data to analyze, we could handle input/output functions, parsing lines of a CSV, and correctly storing datatypes in memory. Or, we could (and will) use Pandas to simply say `pd.read_csv(data.csv)` to handle all of that work with a single line of code.

- Python libraries are collections of packages. We may install a library for linear algebra or separately a library for linear regressions.


So, the question becomes: **how do we install all of the necessary Python packages?**

**Anaconda** is a product that solves many of the headaches associated with Python packaging.

- Anaconda (maintained by Anaconda, Inc. and sometimes just called "Conda") is a Python package manager.
- It comes with many of the required tools and products we need to begin doing data science in Python.

**Download [Anaconda](https://www.anaconda.com/download/):** Select Python 3.6+ for your machine (macOS or PC)

Please: open the file once it finishes downloading, and proceed with the on-screen prompts. There is no need to deviate from the default installation. (If you believe you have a question for your instructor based on your machine, please do not hesitate to raise your hand.)
</aside>

---

## What Are We Downloading?

Pandas:

- The default tool for data exploration and manipulation in Python.

Jupyter Notebooks and Jupyter Lab:

- The preferred integrated development environments (IDEs) of data science.
- We'll write our code in this!

NumPy, SciPy, and [more](https://docs.anaconda.com/anaconda/packages/py3.6_osx-64):

- Other packages for statistical inference, visualization, and parallelizing operations.


<aside class="notes">
**Talking Points**:

-  While we wait for installations to finish, let's preview a few key items of what you're downloading:
- **Pandas:** The Pandas package is the default tool for data exploration and manipulation in Python
- **Jupyter Notebooks and Jupyter Lab:** These are the preferred integrated development environments (IDEs) of data science. They make it easy to write and debug code while conveying the work and results we're formulating.
- **NumPy, SciPy, and [more](https://docs.anaconda.com/anaconda/packages/py3.6_osx-64):** A host of additional packages for statistical inference, visualization, and parallelizing operations. (We will not explore all of these in our single day.)
</aside>

---

## You Do: Launching Jupyter Notebooks


- Use your computer's program search method (Spotlight on Mac) to search "Anaconda Navigator".
- Open Anaconda Navigator
- Click "Launch" on Jupyter Notebooks.

_wait..._

It opens in your browser!

You have a Jupyter Notebook!


<aside class="notes">
**Talking Points**:

- Development environments between Mac and Windows differ, and there are many ways to open Jupyter Notebooks. (Just like there are many ways to open any given file or program on your computer!)
- Emphasize that data science is not all about just writing code. (Hardly!) Discuss the importance of justifying methods. The text included in the lesson provides one example of this (mean vs median), copied here. Consider discussing your own experiences here as well.
- The methods we're applying -- which are typically far more subjective or indeterministic in contrast to straight software development -- are the other half. For example, pretend we're missing many values. Do you fill in missing values with the mean or the median? The code for doing either of these operations is far less significant than the justifying decision. Jupyter Notebooks make it easy to create code cells next to text cells.
- When it comes to markdown, tell students that no one spends time memorizing markdown syntax. Rather, we reference the markdown cheatsheet to remember how to make large headers, bulleted lists, tables, and more. An apt analogy is a mechanic does not spend time memorizing the pantones of cars, but when he/she needs to do a paint job, they will look up the necessary color codes.

**Teaching Tips**:

- Launch a Jupyter Notebook with students (using the Anaconda Navigator), explain code and markdown cells, and create examples of each.- Be patient with students as they launch their first Jupyter Notebook, and be cognizant of the differences in Mac vs Windows for this exercise.
- **Go slowly** when creating and filling in code cells and markdown cells

</aside>

---

## Why Jupyter Notebooks?


Data science is both code and methods

What if we're missing many values?

- Do you fill in missing values with the mean or the median?
- Easy to create code cells next to text cells.

Easy to connect to remote computers (datac enters).

- Thus, the Jupyter Notebook is in your browser!


<aside class="notes">
**Talking Points**:

- **Data science is both code and methods:** As data scientists, the code we write is only half the story. The methods we're applying -- which are typically far more subjective or indeterministic in contrast to straight software development -- are the other half. For example, pretend we're missing many values. Do you fill in missing values with the mean or the median? The code for doing either of these operations is far less significant than the justifying decision. Jupyter Notebooks make it easy to create code cells next to text cells.
- **Connect to remote computing resources:** While we will not be doing this in a today's content, Jupyter Notebooks make it easy to connect to remote computers (datacenters). This is why the Jupyter Notebook is in your browser. You've created a `localhost` server -- a website for one person: you. The brains for this operation are your computer. We could in swap the brains from your computer for stronger computers in a data center, but still write code in your own browser. Wow!

</aside>


---


## Quick Review

- Pandas
    - A Python package for exploratory analysis.

- Jupyter Notebooks and Jupyter Lab:
    - The preferred integrated development environments (IDEs) of data science.
    - We'll write our code in this!

Anaconda helps us download these. You only had to download it once!


<aside class="notes">
**Teaching Tips**:

- Pause and check for understanding.

</aside>

---


## We Do: Code Cells

Let's begin!

- Make a code cell: Click the **+** in the upper left corner.

- Inside the code cell, write:

    ```python
    print('hello world')
    ```

- Be sure your cursor is inside the cell. Press `"control" + Enter`.
  -  Always how you run cells!

Voila!

<aside class="notes">

**Teaching Tips**:

- Make sure they do this with you - walk around the room.
- Make sure everyone understands what's going on.

</aside>



---

## We Do: Markdown Cells

Write and format plain text.

- Make a code cell: Click the **+** in the upper left corner.
  - You're going to be doing this a lot!

- Change this cell to a markdown cell:
  - Click: `cell` > `cell Type` > `Markdown`.
  - *(You can also click the dropdown menu that says "Code" and change it to "Markdown")*

- Inside the markdown cell, write:

  ```md
  ## Hello world
  ```

Run the cell: `"control" + Enter` Bam! Pretty formatted text.

*Note*: We will not spend time learning markdown syntax! Instead, take a look at the cheatsheet and links in Additional Resources.


<aside class="notes">

**Teaching Tips**:

- Make sure they do this with you - walk around the room.
- Make sure everyone understands what's going on.

</aside>

---

## Closing Down

- Exit the tab in your browser.

- That doesn't quit the Notebook!

- Open your Terminal (or Anaconda Prompt on Windows).
- Hit `control + C`. This closes the running process.


<aside class="notes">

**Teaching Tips**:

- Make sure they do this with you - walk around the room.
- Make sure everyone understands what's going on.
- Talk about why (and stress that) exiting the tab doesn't close the notebook.

</aside>

---

## Summary:

Data scientists:

- Use data of all kinds (numbers, text, images).
- Make explanations and predictive decisions.

Data Science Workflow:

- Frame -> Prepare  -> Analyze  -> Interpret -> Communicate.

Jupyter Notebooks:

- The industry tool!
- Interactive with Python.

<aside class="notes">

**Teaching Tips**:

- Wrap up the learning and share additional resources and next steps.
</aside>

---


## Additional Resources

- What is data science from GA's Standards Board [blog post](https://theindex.generalassemb.ly/why-we-need-to-redefine-data-science-7f05ab0286d4)
- Stack Overflow [blog](stackoverflow.blog/2017/09/06/incredible-growth-python/) (1) [posts](https://stackoverflow.blog/2017/09/14/python-growing-quickly/) (2) on Python's growth
- Markdown cheatsheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Interactive markdown cheatsheet [here](http://markdownlivepreview.com/)
