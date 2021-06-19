<!---
This guide was developed by Susi Remondi and heavily updated by Diego Rodriguez for PYTHON-621 / June 21-26, 2021 / VIRTUAL.

--->

![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

# Python Programming

----

> This course introduces beginners to the Python programming language, with a brief working intro to a special topic: Data Science (Pandas).
> Instructor: [Diego Rodriguez](https://generalassemb.ly/instructors/diego-rodriguez/16908)

## Overview
In this one-week Python Programming course, students will walk away with a foundation in Python programming. Students will also get an 8 hour dive into the Python library for data analysis, Pandas, and walk away with a project of their choosing they've built using that library, thus, being able to confidently manage data collection, data manipulation, data analysis, data visualization, and data presentation using Python and Pandas.

## Quick Links
- [About This Guide](#about-this-guide)
- [Course Details](#course-details)
- [Suggested Pacing Guide](#suggested-pacing-guide)
- [Appendix: Materials and Resources](#appendix-materials-and-resources)
- [Notes for Teaching This Course](python-specific-course.md)
- [Instructions on Slide Delivery](presenting-and-creating-materials)
- Note: All of the decks for this course can be found [here](https://s3.amazonaws.com/python-ga/v1.4.1/index.html).

## About This Guide

This guide contains links to a standard set of high quality resources for your use in teaching this course. But our goal is not to provide you with a script to follow; we hire practitioners at GA because we value what you bring to the classroom and want to encourage you to make adaptations.
Think of this guide as a cookbook. You, as the chef, will use the guidelines provided to craft an amazing meal for your students. But of course, you’ll want to think ahead about the various “dietary restrictions” and preferences of your “diners” as well as the type of “ambience” best suited to the type of experience you want to create.
Adaptations we encourage you to make:
- **Swapping out our generic examples for real-life examples from your industry experience.** The more you can speak to your own experience, the more the content will resonate with students.
- **Adapting suggested projects and activities to better challenge your students,** based on their level of prior knowledge and their interests.
- **Moving faster or slower as needed through the lessons based on the needs of your class.**


Adaptations we encourage you not to make without speaking with your manager first, especially during your first cohort:
- **Skipping over or cutting learning objectives.** Our curriculum is designed specifically to prepare students to a career in your industry. We’ve made a promise to them to get them job ready; when you skip content you’re putting their job readiness at risk.
- **Changing the scope of the course.** Try not to add new topics that distract from the core learning.
- **Radically altering the sequence of the course.** It’s okay to skip around sometimes, but try to follow the order of the units suggesting, especially during your first cohort.

>NOTE: If you haven’t already done so, be sure to complete the Instructor Course on myGA. The self-paced course provides a basic background in key concepts necessary for success leading a GA class.

When in doubt, discuss any planned changes to the curriculum you’d like to make with your manager, your fellow instructors, or a Global team member. Chances are, someone else can learn from or be inspired by your improvements!


## Course Details
Python Programming is a 40-hour course, delivered in either 5 day full-time or 10 week part time (two 2-hour sessions a week) format. There is no admittance requirement - this course is open to and encouraged for absolute beginners.

Once enrolled, students complete 3.5 hours of pre-work on the myGA platform.

>NOTE: As an instructor, you should familiarize yourself with this pre-work so you can incorporate it in to your first lesson.

Your role as an instructor is to facilitate each student’s journey to mastery of the concepts outlined below. This guide will provide you with a suggested pacing guide you can use to ensure you hit all of the required objectives in a sequence that makes sense. **We recommend you follow the suggested pacing guide during your first instance.** Later on, as you become more familiar with the content and your own teaching style, you can remix and extend the lessons provided. Just be sure to cover all of the required topics that follow.

In order to graduate and earn a course completion certificate, every student must complete a final project that meets or exceeds the minimum standards outlined in the project rubric. Your manager will help you track other graduation requirements and make decisions about graduation.

### Learning Objectives
The high-level learning objectives for this course are:

- Create a basic Python app, using control flow, classes, and try/catch statements.
- Incorporate APIs, modules, and user input into a Python app.
- Use Pandas to create a visualization of a dataset **or** use Flask to create and run a Python application (depending on the special topic track).

Students cannot graduate unless they demonstrate mastery of the above learning objectives before the end of the course. Mastery is measured through assessment: homeworks, in-class activities and final projects.

The official course syllabus, available [here](https://drive.google.com/file/d/1G5MxiLnVah4YAoJTzdIYK-8guTYC-Q7u/view), outlines what must be covered in the course.

Optional topics you may consider adding on to extend learning (provided your students are ready) include:
- More intermediate programming, such as decorators, logging, and unit tests.
- More interesting or specialized libraries, such as PyGame, NumPy, or Django.

### Course Format
This course may be taught online or in-person, in a [10-week](#10-week-pacing) or [1-week format](#1-week-pacing).

### Homework
You will not have time to personally review each homework assignment. A group of instructors has [put together boilerplate responses](https://git.generalassemb.ly/ed-product-library/python-programming/tree/master/boilerplate_feedback) covering both strengths and weaknesses for the major topics.

## Suggested Pacing Guide
The schedules below are provided as examples only. Feel free to create the right pace of lessons and activities for your students in order to ensure the required learning objectives are met. **Note:** These links will be live when the markdown files are available on Sept. 7

#### 1 Week Pacing
It is recommended that 1-week students complete both learning paths assigned to them prior to the first day of class. 
1) Welcome to Python Programming
2) Addition Python Lessons

Day 1                                        | Day 2                               | Day 3                                 | Day 4                                        | Day 5: Data Option                       | Day 5: Web Dev Option                    | Day 6 (Select the option for your track)             |
-----------------------------------          | ----------------------------------- | ------------------------------------- | -------------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------------------- |
[:30] [Course Introductions][1-1A]           | [:30] Day 2 Kickoff                 | [:30] Day 3 Kickoff                   | [:30] Day 4 Kickoff                          | [:30] Day 5: Data Kickoff                | [:30] Day 5: Web Dev Kickoff             | [:30] [Summary Kickoff, Data][6-1A]                  |
[1:00] [Defining Variables][1-1B]            | [1:30] [Functions][2-1B]            | [:30] [Inheritance][3-1B]             | [:15] [Intermediate Python Discussion][4-1B] | [1:00] [Pandas 2][5-1F]                  | [:30] [Intro to Web Dev in Python][5-2B] | [:30] [Summary Kickoff, Web][6-1B]                   |
[:30] [Python Installations][1-1C]           | [:15] Break                         | [:15] Break                           | [:15] Break                                  | [:15] Break                              | [:30] [Intro to Flask][5-2C]             | [2:00] [In-Class: Final Project Workshop, Web][6-1C] |
[:15] Break                                  | [:45] [Advanced Arguments][2-1C]    | [1:30] [Lab #3: OOP][3-1C]            | [:30] [Intro to Python for Data][5-1B]       | [1:00] [Plots and Charts][5-1E]          | [:15] Break                              | [2:00] [In-Class: Final Project Workshop, Web][6-1D] |
[1:00] [Lab #1: Fundamentals][1-1D]          | [1:00] Lunch                        | [:15] Mid-Week Check-in               | [:30] [Modules & Libraries][4-1E]            | [1:00] Lunch                             | [1:15] [Styling Flask][5-2D]             | [1:00] Lunch                                         |
[1:00] Lunch                                 | [1:30] [Lab #2: Control Flow][2-1D] | [1:00] Lunch                          | [1:00] Lunch                                 | [:45] [Pandas Datetime][5-1I]            | [1:00] Lunch                             | [2:00] [Project Presentations, Data][6-1E]           |
[1:00] [Conditionals][1-1E]                  | [:30] [Dictionaries][2-1E]          | [:30] [Variable Scope][3-1D]          | [1:00] [Pandas 1][5-1C]                      | [1:00] [Pandas Joins][5-1J]              | [1:00] [Flask Variables][5-2E]           | [2:00] [Project Presentations, Web][6-1F]            |
[:15] Break                                  | [:45] [Sets & Tuples][2-1F]         | [:15] Break                           | [:15] Break                                  | [1:15] [Lab #6: Weather Forecast][5-1G]  | [:15] Break                              | [:30] [Wrap-up & Celebrations, Data][6-1G]           |
[:30] [Loops][1-1G]                          | [:45] [Classes][2-1G]               | [:45] [Debugging Principles][3-1F]    | [1:15] [Lab #5: Intermediate Python][4-1G]   | [:30] [End-of-Day Recap][5-1H]           | [:30] [APIs and Requests][5-2G]          | [:30] [Wrap-up & Celebrations, Web][6-1H]            |
[:30] [Lists][1-1F]                          | [:15] End-of-Day Recap              | [1:00] [Lab #4: Debugging][3-1G]      | [:15] Final Project Discussion               | --                                       | [1:15] Review and Practice       | --                                                   |
[:30] End-of-Day Recap                       |  --                                 | [:30] In-class HW/Review Time         | [:30] End-of-Day Recap                       | --                                       | [:30] [End-of-Day Recap][5-2H]           | --                                                   |
 --                                          |  --                                 | [:30] End-of-Day Recap                |  --                                          | --                                       | --                                       | --                                                   |

[1-1A]: unit-1-variables/instructor-resources/01-welcome
[1-1B]: unit-1-variables/instructor-resources/02-variables
[1-1D]: unit-1-variables/instructor-resources/03-unit-lab-1
[1-1E]: unit-2-control-flow/instructor-resources/04-conditionals
[1-1F]: unit-2-control-flow/instructor-resources/05-lists
[1-1G]: unit-2-control-flow/instructor-resources/06-loops

[2-1B]: unit-2-control-flow/instructor-resources/07-functions
[2-1C]: unit-2-control-flow/instructor-resources/08-args
[2-1D]: unit-2-control-flow/instructor-resources/09-unit-lab-2
[2-1E]: unit-3-oop/instructor-resources/10-dictionaries
[2-1F]: unit-3-oop/instructor-resources/11-sets-tuples
[2-1G]: unit-3-oop/instructor-resources/12-classes

[3-1B]: unit-3-oop/instructor-resources/13-inheritance
[3-1C]: unit-3-oop/instructor-resources/14-unit-lab-3
[3-1D]: unit-4-troubleshooting/instructor-resources/15-variable-scope
[3-1E]: unit-4-troubleshooting/instructor-resources/16-intermediate-variables
[3-1F]: unit-4-troubleshooting/instructor-resources/17-debugging
[3-1G]: unit-4-troubleshooting/instructor-resources/18-unit-lab-4

[4-1B]: unit-5-intermediate/instructor-resources/19-intermediate-intro
[4-1C]: unit-5-intermediate/instructor-resources/20-scripting
[4-1E]: unit-5-intermediate/instructor-resources/22-modules
[4-1F]: unit-5-intermediate/instructor-resources/23-apis
[4-1G]: unit-5-intermediate/instructor-resources/24-unit-lab-5

[5-1B]: unit-6-pandas/instructor-resources/01-ds-intro
[5-1C]: unit-6-pandas/instructor-resources/02-pandas-i
[5-1D]: unit-6-pandas/instructor-resources/03-data-viz
[5-1E]: unit-6-pandas/instructor-resources/04-plotting-with-pandas
[5-1F]: unit-6-pandas/instructor-resources/05-pandas-ii
[5-1G]: unit-6-pandas/instructor-resources/06-pandas-unit-lab
[5-1H]: unit-6-pandas/instructor-resources/07-next-steps
[5-1I]: unit-6-pandas/instructor-resources/08-pandas-datetime
[5-1J]: unit-6-pandas/instructor-resources/09-pandas-join

[5-2B]: unit-6-flask/instructor-resources/01-web-dev-intro
[5-2C]: unit-6-flask/instructor-resources/02-flask
[5-2D]: unit-6-flask/instructor-resources/03-styling-flask
[5-2E]: unit-6-flask/instructor-resources/04-flask-routing
[5-2F]: unit-6-flask/instructor-resources/05-flask-templates
[5-2G]: unit-6-flask/instructor-resources/06-flask-apis
[5-2H]: unit-6-flask/instructor-resources/08-next-steps

[6-1A]: unit-7-data-wrap-up/instructor-resources/01-review
[6-1B]: unit-7-web-dev-wrap-up/instructor-resources/01-review
[6-1C]: unit-7-data-wrap-up/instructor-resources/02-project
[6-1D]: unit-7-web-dev-wrap-up/instructor-resources/02-project
[6-1E]: unit-7-data-wrap-up/instructor-resources/02-project
[6-1F]: unit-7-web-dev-wrap-up/instructor-resources/02-project
[6-1G]: unit-7-data-wrap-up/instructor-resources/03-summary
[6-1H]: unit-7-web-dev-wrap-up/instructor-resources/03-summary

Day      | Suggested Homework
-------- | ---------
1        | [Lists, `if/elif/else`, and `for/while`][7-1A]
2        | [Functions, Dictionaries, *Bonus: Kwargs*][7-1B]
3        | [Inheritance, Debugging ][7-1C]
4        | [Scripting, APIs][7-1D]
5, Data  | [Pandas EDA, Pandas Visualizations][7-1E], [Consumer Sales Exercise][7-1G], [OMDB Pandas Exercise][7-1H]
5, Web   | [Rendering Templates, Creating APIs, GET/POST Requests][7-1F]

[7-1A]: unit-1-variables/instructor-resources/hw-5day-day1
[7-1B]: unit-2-control-flow/instructor-resources/hw-5day-day2
[7-1C]: unit-5-intermediate/instructor-resources/hw-5day-day3
[7-1D]: X
[7-1E]: unit-6-pandas/instructor-resources/hw-5day-4pandas
[7-1F]: unit-6-flask/instructor-resources/hw-5day-4flask
[7-1G]: unit-6-pandas/instructor-resources/10-pandas-consumersales
[7-1H]: unit-6-pandas/instructor-resources/11-pandas-omdb-exercise


#### 10 Week Pacing

Students are to complete the **Welcome to Python Programming** learning path on myGA prior to the first day of class.

| Lesson # (Week:Day) | In Class                                                                                                                                                                                                                                                                                                                                              |   | Homework                                                                                                                                                                              |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lesson 1 (w1:d1)    | [Confirm Python 3 Installation](unit-0-prework/instructor-resources/01-local-python),[Welcome](unit-1-variables/instructor-resources/01-welcome) and [Variables](unit-1-variables/instructor-resources/02-variables)                                                                                                                                  |   | [Homework: Declaring variables in a local file.](unit-1-variables/instructor-resources/hw-10wk-class-1) AND two myGA Lessons: Control Flow in Python and Functions in Python                 |                                                               |
| Lesson 2 (w1:d2)    | [Unit Lab 1: Variables](unit-1-variables/instructor-resources/03-unit-lab-1), [Conditionals](unit-2-control-flow/instructor-resources/04-conditionals), [Lists](unit-2-control-flow/instructor-resources/05-lists)                                                                                                                                    |   | [Homework: Using `if` and `else`](unit-2-control-flow/instructor-resources/hw-10wk-class-2)                                                                                           |
| Lesson 3 (w2:d1)    | [Loops](unit-2-control-flow/instructor-resources/06-loops), [Functions](unit-2-control-flow/instructor-resources/07-functions)                                                                                                                                                                                                                        |   | [Homework: Using lists, `if/elif/else`, and `for/while`](unit-2-control-flow/instructor-resources/hw-10wk-class-3)                                                                   |
|                     Lesson 4 (w2:d2)    | [Advanced Function Arguments](unit-2-control-flow/instructor-resources/08-args), [Unit Lab 2: Control Flow](unit-2-control-flow/instructor-resources/09-unit-lab-2)                                                                                                                                                                |   | [Homework: `if`, `for`, and list functions](unit-2-control-flow/instructor-resources/hw-5day-day-1) AND one myGA Lesson: Objects and Classes                                                                                   |
| Lesson 5 (w3:d1)    | [Dictionaries](unit-3-oop/instructor-resources/10-dictionaries), [Sets and Tuples](unit-3-oop/instructor-resources/11-sets-tuples)                                                                                                                                                                                                                    |   | [Homework: Dictionaries, tuples, sets](unit-3-oop/instructor-resources/hw-10wk-class-5)                                                                                               |
| Lesson 6 (w3:d2)    | [Classes](unit-3-oop/instructor-resources/12-classes), [Inheritance](unit-3-oop/instructor-resources/13-inheritance), [Unit Lab 3: Object Oriented Programming](unit-3-oop/instructor-resources/14-unit-lab-3)                                                                                                                                        |   | [Homework: Functions, dictionaries, inheritance, kwargs](unit-3-oop/instructor-resources/hw-10wk-class-5) AND one myGA Lesson: Error Handling in Python                                                                             |
| Lesson 7 (w4:d1)    | [Variable Scope](unit-4-troubleshooting/instructor-resources/15-variable-scope), [Intermediate Variables](unit-4-troubleshooting/instructor-resources/16-intermediate-variables), [Debugging Principles and Techniques](unit-4-troubleshooting/instructor-resources/17-debugging)                                                                     |   | [Homework: Type Conversion, String Formatting, Debugging, Scope](unit-4-troubleshooting/instructor-resources/hw-10wk-class-7)                                                         |
| Lesson 8 (w4:d2)    | [Unit Lab 4: Troubleshooting](unit-4-troubleshooting/instructor-resources/18-unit-lab-4), [Introduction to Intermediate Python](unit-5-intermediate/instructor-resources/19-intermediate-intro), [Scripting](unit-5-intermediate/instructor-resources/20-scripting) |   | [Homework: Scripting, File I/O, and Lists](unit-5-intermediate/instructor-resources/hw-10wk-class-8)                                                                                  |
| Lesson 9 (w5:d1)    | [Modules and Libraries](unit-5-intermediate/instructor-resources/22-modules)                                                                                                                                                                             |   | [Homework: Modules and Libraries](unit-5-intermediate/instructor-resources/hw-10wk-class-9)                                                                                           |
| Lesson 10 (w5:d2)   | [APIs](unit-5-intermediate/instructor-resources/23-apis), Review                                                                                                                                                                                                                                                                                      |   | [Homework: APIs and String Formatting](unit-5-intermediate/instructor-resources/hw-10wk-class-10)                                                                                     |
| Lesson 11 (w6:d1)   | [Unit Lab 5: Intermediate Python](unit-5-intermediate/instructor-resources/24-unit-lab-5)                                                                                                                                                                                                                                                             |   | [Homework: APIs, Debugging, Scripting](unit-5-intermediate/instructor-resources/hw-5day-day3)                                                                       |
| Lesson 12d (w6:d2)  | *Data Track*: [Introduction to Data Science](unit-6-pandas/instructor-resources/01-ds-intro), [Pandas I](unit-6-pandas/instructor-resources/02-pandas-i)                                                                                                                                                                                              |   | [Homework: Reading datasets into Pandas,  Filtering, manipulating, and sorting datasets, Basic exploratory data analysis with Pandas](unit-6-pandas/instructor-resources/hw-10wk-12d) |
| Lesson 12w (w6:d2)  | *Web Dev Track*: [Introduction to Web Dev](unit-6-flask/instructor-resources/01-web-dev-intro), [Flask Introduction](unit-6-flask/instructor-resources/02-flask), [HTML, CSS, and Styling Flask](unit-6-flask/instructor-resources/03-styling-flask)                                                                                                  |   | [Homework: Writing a basic Flask app](unit-6-flask/instructor-resources/hw-10wk-11)                                                                                                   |
| Lesson 13d (w7:d1)  | *Data Track*: [Data Visualization](unit-6-pandas/instructor-resources/03-data-viz), [Plotting with Pandas and Matplotlib](unit-6-pandas/instructor-resources/04-plotting-with-pandas)                                                                                                                                                                 |   | [Homework: Plotting with Pandas, Determining the best plot, given a dataset](unit-6-pandas/instructor-resources/hw-10wk-13d)                                                          |
| Lesson 13w (w7:d1)  | *Web Dev Track*: [Variables and Routing](unit-6-flask/instructor-resources/04-flask-routing), [Templates](unit-6-flask/instructor-resources/05-flask-templates), [APIs and Requests](unit-6-flask/instructor-resources/06-flask-apis)                                                                                                                 |   | [Homework: Variables, Routing, Templates](unit-6-flask/instructor-resources/hw-10wk-12)                                                                                               |
| Lesson 14d (w7:d2)  | *Data Track*: [Pandas II](unit-6-pandas/instructor-resources/05-pandas-ii), [Unit Lab 6: Pandas](unit-6-pandas/instructor-resources/06-pandas-unit-lab)                                                                                                                                                                                               |   | [Homework: Basic EDA with Pandas, Visualization with Pandas](unit-6-pandas/instructor-resources/hw-5day-4pandas)                                                                      |
| Lesson 14w (w7:d2)  | *Web Dev Track*: Instructor or Student Choice                                                                                                                                                                                                                                                             |   | [Homework: Rendering templates, Creating an API, Making GET/POST requests](unit-6-flask/instructor-resources/hw-5day-4flask)                                                          |
| Lesson 15d (w8:d1)  | *Data Track*: Lab Review, [Next Steps with Data Science](unit-6-pandas/instructor-resources/07-next-steps)                                                                                                                                                                                                                                            |   | < None >                                                                                                                                                                              |
| Lesson 15w (w8:d1)  | *Web Dev Track*: Lab Review, [Next Steps with Web Dev](unit-6-flask/instructor-resources/08-next-steps)                                                                                                                                                                                                                                               |   | < None >                                                                                                                                                                              |
| Lesson 16d (w8:d2)  | *Data Track*: [Overall Review and Q&A](unit-7-data-wrap-up/instructor-resources/01-review), [Introduce Project](unit-7-data-wrap-up/instructor-resources/02-project)                                                                                                                                                                                  |   | < None >                                                                                                                                                                              |
| Lesson 16w (w8:d2)  | *Web Dev Track*: [Overall Review and Q&A](unit-7-web-dev-wrap-up/instructor-resources/01-review), [Introduce Project](unit-7-web-dev-wrap-up/instructor-resources/02-project)                                                                                                                                                                         |   | < None >                                                                                                                                                                              |
| Lesson 17 (w9:d1)   | Work on Project                                                                                                                                                                                                                                                                                                                                       |   | < None >                                                                                                                                                                              |
| Lesson 18 (w9:d2)   | Work on Project                                                                                                                                                                                                                                                                                                                                       |   | < None >                                                                                                                                                                              |
| Lesson 19 (w10:d1)  | Project Presentations                                                                                                                                                                                                                                                                                                                                 |   | < None >                                                                                                                                                                              |
| Lesson 20d (w10:d2) | *Data Track*: Project Presentations, [Class Summary](unit-7-data-wrap-up/instructor-resources/03-summary)                                                                                                                                                                                                                                             |   | < None >                                                                                                                                                                              |
| Lesson 20w (w10:d2) | *Web Dev Track*: Project Presentations, [Class                                                                                                                                                                                                                                                                                                        |   |                                                                                                                                                                                       |
---

## Appendix: Materials and Resources
- Please read through the [specific course details](python-specific-course.md) for information on the structure of the repos, how to run the unit labs, the projects, and more.
- See the [presenting and creating materials](presenting-and-creating-materials/README.md) directory for instructions on presenting the materials on GA Brand or creating your own.
- All lesson materials, homeworks and projects outlined on the Suggested Pacing Guide are in this repo.
- Standard GA-produced pre-work materials can be accessed on myGA. The pre-work lessons details can be found [here.](https://git.generalassemb.ly/python-programming/python-programming/blob/revisions_v2.1/unit-0-prework/instructor-resources/README.md)
- Tips and templates for instructors are available on the [GA Instructor Blog](http://assemblyrequired.ga.co).
- For help and support, join the GA Instructors Slack Community and post your questions in #SLACKCHANNEL.


*Copyright 2018, General Assembly Space. Licensed under [CC-BY-NC-SA, 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)*
