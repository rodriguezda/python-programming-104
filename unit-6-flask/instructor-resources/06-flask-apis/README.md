<!---
Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack at @Kevin.Coyle.
--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) APIs and Requests in Flask

## Overview
This is a lesson on creating an API in Flask. It starts by recapping web terms like HTTP, then has students create a JSON list in their Flask app. They `GET` the list with one route, then `POST` to it with another.


## Important Notes or Prerequisites
There are a few notes on calling the OMDb API, but it's agnostic enough that it can be spun as an example, if you're teaching standalone.

## Learning Objectives
In this lesson, students will:
- Create an API that makes a `GET` request with Flask.
- Create an API that makes a `POST` request with Flask.

---

## Duration
30 minutes

---

## Suggested Agenda


| Time | Activity | Purpose |
| --- | --- | --- |
| 0:00 - 0:02 | [Welcome](#activity-welcome-2-min) | Introduce the lesson’s objectives and agenda.|
| 0:02 - 0:10 | [APIs and HTTP](#activity-apis-and-http-8-min) | Recap the main terminology involved in APIs. |
| 0:10 - 0:19 | [Creating a GET Request](#activity-creating-a-get-request-9-min)| Create an API that makes a `GET` request with Flask. |
| 0:19 - 0:27 |  [Creating a POST Request](#activity-creating-a-post-request-8-min)| Create an API that makes a `POST` request with Flask. |
| 0:27 - 0:30  | [Summary](#activity-summary-3-min) | Wrap up the learning and share next steps. |
---

## Differentiation and Extensions
- More advanced students may work on adding authentication into their Flask app.
- Struggling students should review the lesson on APIs from Unit 5.
- Students may also wish to explore their `POST`/`GET` requests in the Chrome extension Postman.
  - This is a GUI-friendly version of the command line version taught in the lesson.

---
---

## Lesson Procedure
<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection. --->

---

### Activity: Welcome (2 min)
> Introduce the lesson objectives and agenda.

---

### Activity: APIs and HTTP (8 min)
> Recap the main terminology involved in APIs.

> **Teaching Tips:**

> - APIs are the vehicle that drive most of the modern web.
> - Knowing how to create and consume APIs is important for a variety of coding tasks, regardless of job title.
> - Flask provides an incredibly lightweight module for our purposes.

>  **Talking Points:**

> - Ask students if they have any familiarity interacting with APIs outside of the last unit's materials.
> - It's **important** to explain to students that in Unit 5 we *called* an API. Today we are *creating* an API.
>  - This can be explained with an example like, "In Unit 5 we were reading a book, and today, we're writing a book that others can read."
>  - Calling an API allows you to retrieve data, while creating an API makes some data that you want to publish accessible.


---

### Activity: Creating a `GET` Request (9 min)
> Create an API that makes a `GET` request with Flask.

> **Teaching Tips:**

- Explain how this differs from just returning a variable. What makes this an API?
- This is a code-along/We Do. Have students open code editors and terminal, then follow along.
- We are actually doing two things at once here: We're creating data, and then we're creating an API where one could obtain that data. We're focusing more on the latter task, so as to emphasize creating the API.

---

### Activity: Creating a `POST` Request (8 min)
> Create an API that makes a `POST` request with Flask.

>  **Teaching Tips:**

> - This is a code-along/We Do. Students will extend the app they have been creating since the `hello_world` app.
> - Similar to the `GET` activity, we're creating the data that we will append to the list with a `POST` request.

> **Talking Points:**

> - This `POST` request is using a simple example.
> - Explain why we would do this! The example is very simple. This can extend to Create/Update data into a number of other applications: search bars, adding data into databases, and so on.


---

### Activity: Summary (3 min)
> Wrap up the learning and share next steps.
