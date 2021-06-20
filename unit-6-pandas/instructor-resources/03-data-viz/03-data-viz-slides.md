<!--
title: Intro to Visualization
type: lesson
duration: "00:40"
creator: Emma Freeman [originating from David Yerrington's python-data-viz-principles lesson]
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Intro to Visualization</h1>

<!--


## Overview
This lesson introduces students to the concept of data visualization - what it is, why it's important, the components of a great data visualization. Near the end, there's a section to help students understand when they would use a bar chart, pie chart, scatter plot, or histogram.

## Important Notes or Prerequisites

The next lesson is on Pandas and actually building these graphs. This lesson is all about understanding the different types of graphs and their use cases.


## Learning Objectives
*After this lesson, students will be able to...*

- Describe why data visualization is important.
- Identify the characteristics of a great data visualization.
- Identify when you would use a bar chart, pie chart, scatter plot, and histogram.

## Duration
45 minutes.

---

## Suggested Agenda

| Time | Activity | Purpose |
| --- | --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:08  | Data Visualization |
| 0:08 - 0:30  | Types of Plots |
| 0:30 - 0:42  | Visualization Tips |
| 0:42 - 0:45  | Summary |

## Materials and Preparation
- Send out the link to the presentation slides to students.
- No out of the ordinary prep needed

## Differentiation and Extensions
- There is a lot to say about best practices for data visualization! Feel free to add slides of your own.

## In Class: Materials
- Projector
- Internet connection
- Jupyter Notebooks
- Python3
-->


---

## Lesson Objectives
*After this lesson, you will be able to...*

* Describe why data visualization is important for communicating results.
* Identify how to select the correct visualization to use based on the data being presented.
* Identify characteristics to clearly communicate through data visualizations.

<aside class="notes">
Teaching Tips:

- Introduce topic and learning objectives
- Pause to take any student questions after reading through the learning objectives
</aside>

---

## How Do we Make Sense of a Data Set?

We're only looking at 1/3 of this data set! While all the data we need is here, it is difficult to make sense of and draw any meaning from.

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/flight-data-set.png)


<aside class="notes">
Teaching tips:
- Note how much more difficult it is to read and make sense out of
- Raw data contains a lot of information but isn't digestible or understandable until it is presented in a synthesized way.
- The first chart allowed us to compare, draw inferences, and have a clear take-away
</aside>


---

## So What Is Data Visualization?

- A quick, easy way to convey concepts that from from large data sets.
- We can use these charts, graphs, or illustrations to visualize large amounts of complex data.

<!--VISUALS: create venn diagram similar to this one (http://www.bethkanter.org/data-viz-2/) but simplified-->

<aside class="notes">
Teaching Tips:

- Encourage discussion here by asking learners what differs between "charts" and "data visualization"? Where have you seen helpful charts, graphs, or other visualizations? Where could this be useful?
- Ask participants to share examples of data visualization they found captivating and why.

**Teaching Tips**:

- "Because of the way the human brain processes information, charts or graphs that visualize large amounts of complex data are easier to understand than spreadsheets or reports.  Data visualization is a quick, easy way to convey concepts in a universal  manner — and you can experiment with different scenarios by making slight adjustments."
</aside>

---

## Criteria for Crafting a Good Visualization

Visualizations should follow three (plus one) rules. They should be:

1. Simplified
2. Easy to Interpret
3. Clearly Labeled
4. (Bonus) Interactive

<aside class="notes">
**Teaching Tips**:
- Provide an example of for one of these bullets as to why they are important.
- Discuss why interactive is a bonus
- Explain how these three roles combine.  
</aside>

---

## How Do you Choose the Right Chart Type?

With so many chart types, it can be difficult to know how best to display your data.

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/chart_types.png)

When creating a visualization first think about the variables you are showing (words, categories, numbers, etc., the volume of data, and the central point you are hoping to communicate through your visualization.

<aside class="notes">
Teaching tips:

- Explain that we'll go over many of these in detail throughout the slides
- Do frequent checks for understanding by asking students for examples of cases where they would use each type of plot, and example of good or bad things they've seen with the plots.
- As you introduce new chart types, contrast it with the previous ones - give examples of when you'd use one vs the other.
- Bring up good (or bad!) practices as you see them in the examples.
</aside>

---


## The Bar Chart in Action

Looking at this bar chart, what do you notice about this visualization?

<img src="https://espnfivethirtyeight.files.wordpress.com/2016/08/koeze-olympics-age-3.png" style="width:70%; height: auto" />


<aside class="notes">
Teaching Tips:
- Ask what is happening with the ordering of the bars here? Why would the designer make that choice?
- How about the coloring? What do you notice about that?
- Finally, what can you tell about this chart from the title?

**Teaching Tips**:

- Bar charts are one of the most common ways of visualizing data. Why? Because they make it easy to compare information, revealing highs and lows quickly. Bar charts are most effective when you have numerical data that splits neatly into different categories.
</aside>

---

## When to Use a Bar Chart
Bar charts are one of the most simple and frequently used chart types. They are useful for illustrating either one string or one numeric variable, quickly comparing information, or for show exact values.

When thinking about using a bar chart consider:
- Will you use vertical or horizontal bars?
- How will you number your axis (it is always best to start at zero)?
- How will you order your bars?

<aside class="notes">
**Teaching Tips**:
- Before moving to the next slide ask, when would you use a bar chart?
</aside>

---


## The Pie Chart in Action

As you can see from this example pie charts can be effective for proportions or percentages.

![](https://www.csisun.com/wp-content/uploads/2012/07/solarhotwaterpiechart.jpg)


<aside class="notes">
**Teaching Tips**:

- Pie charts are the most commonly misused chart type.
- Pie charts show the relationship of parts out of whole.
- Why do they work well with proportions or percentages? Because those two types of information show the relationship of parts to a whole.
</aside>

---

## When to Use the Pie Chart Type

Pie charts are commonly misused. They show a part-to-whole relationship when the total amount is one of your variable and you'd like to show the subdivision of variables.

When thinking about using a pie chart consider:
- The more variables you have, as in the more slices of your pie you'll have, the harder it is to read.
- Area is _very_ difficult for the eye to read, so if any of your wedges are similarly sized think about a different chart type.
- If you want to compare data, leave it to bars or stacked bars. If your viewer has to work to translate pie wedges into relevant data or compare pie charts to one another, the key points you're trying to convey might go unnoticed.

<aside class="notes">
**Teaching Tips**:

- Before moving to the next slide ask, when would you use a pie chart?
</aside>

---

## The Scatter Plot in Action

This scatter plot uses a combination of text, coloring, and labelling to describe the data. What is clear or unclear from this chart about the data set?

<img src="http://kbroman.files.wordpress.com/2013/02/science_scores.png" style="width: 70%; height: auto" />

<aside class="notes">
**Teaching Tips**:

- Start a discussion around how clear or legible this chart type is.
- Ask, what the midline is doing here? How about the legend?
</aside>

---

## When to Use a Scatter Plot

Scatterplots are great for data dense visualizations and clusters. They are most effective for trends, concentrations, and outliers. They can be especially useful to see what you want to investigate further.


When thinking about using a scatter plot consider:
- This chart type is not as common so can me more difficult for an audience to read.
- If dots are covering up each other, consider a different chart type.
- A bubble chart is one variation on the scatter plot.

<aside class="notes">
**Teaching Tips**:

- Scatter plots are a great way to give you a sense of trends, concentrations, and outliers, and are great to use while exploring your data. This will provide a clear idea of what you may want to investigate further.
</aside>

---

## Knowledge Check: Choosing a Chart


Annual sales in each state for a grocery store chain?

- Bar chart.
- Pie chart.
- Scatterplot.

<aside class="notes">
**Teaching Tips**:

- Which type of chart do you think we should use in the following cases?
(bar)
</aside>

---

## When to Use a Histogram


- Effective for distribution across groups.

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/histogram.png)

<aside class="notes">
**Teaching Tips**:

- Histograms are useful when you want to see how your data are distributed across groups. Important: histograms are not the same thing as a bar chart! Histograms look similar to bar charts, but with bar charts, each column represents a group defined by a categorical variable; and with histograms, each column represents a group defined by a continuous, quantitative variable.
- One implication of this distinction: with a histogram, it can be appropriate to talk about the the tendency of the observations to fall more on the low end or the high end of the X axis.
- With bar charts, however, the X axis does not have a low end or a high end; because the labels on the X axis are categorical - not quantitative.
</aside>

---

## Bar Chart vs Histogram

The main difference between a bar chart and histogram is that histograms are used to show distributions of variables while bar charts are used to _compare_ variables.

![](https://qph.fs.quoracdn.net/main-qimg-237e649130e7ae0245e003a6a1949b91.webp)

<aside class="notes">
**Teaching Tips**:
- Pause here to make sure the difference is clear as these two chart types are very similar.
- When would you use a histogram? What about a bar chart?
</aside>

---

## Which type of chart?

Relationship of average income to education level?


- Bar chart.
- Pie chart.
- Scatterplot.
- Histogram.


<aside class="notes">
**Teaching Tips**:

- Which type of chart do you think we should use in the following cases?
(scatter)
</aside>

---

## A Line Chart in Action

Line graphs are an excellent way to show change over time. While bar charts can also show time, they don't show it in a continuous way like a line chart.

![](https://static.guim.co.uk/sys-images/Guardian/Pix/maps_and_graphs/2012/4/25/1335374489202/Recession-and-recovery-ch-001.gif)

<aside class="notes">
**Teaching Tips**:
- Ask, how could time  be represented differently with this chart type?

</aside>

---

## When to Use a Line Chart

Line charts are particularly good at showing how a variable change over time. They work best if you have one date variable and one number variable.

When thinking about using a line chart consider:
- How many lines you'll need on your graph, the more overlapping lines there are, the harder your chart will be to read.
- Consider how many colors you need to use for your lines. Giving each line its own color forces the viewer to scan back and forth from the key to the graph.
- Individual data points can be hard to read, but line charts are good for showing overall trends.
- Similar to bar charts, try and start at 0 on your x axis.

<aside class="notes">
**Teaching Tips**:
- Explain what is meant by overall trends.
</aside>

---

## Knowledge Check: Which type of chart?

Change in average income since 1960 for American adults?

- Bar chart.
- Pie chart.
- Scatterplot.
- Line chart.
- Histogram.


<aside class="notes">
**Teaching Tips**:

- Which type of chart do you think we should use in the following cases?
(line or scatter)
</aside>

---

## Returning to How to Choose the Right Chart


Check out [this series of charts](https://i.redd.it/e7alp8yrnb711.png): `https://i.redd.it/e7alp8yrnb711.png`

- Which is easiest to view the data?

<p class="fragment">
It's subjective! There are pros and cons to each. Choosing a chart type depends firstly on the data you have. Secondly, it depends on the clearest way to convey your message. The alignment of these two aspects will help you decide what type of visualization to use.
</p>


<aside class="notes">
**Teaching Tips**:

- The choice of visualization should depend what you are trying to show. Here is a helpful flowchart that you can use to determine the best type of visualizations.
</aside>

---

## Charts & Code

There is an increasing array of libraries and tools to allow us to use code to create visualize data in compelling and approachable ways.

Check out this complex chart that was made using Python!

<img src="https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/flight-chart.jpg" style="width: 70%; height: auto;"  />

*Source: u/dx034 on Reddit*

<aside class="notes">
Teaching tips:
- Note that it seems intricate but was created with code.
- Discuss how an understanding of chart types can help us become better at working with and displaying data using code.
</aside>

---

## Group Activity: Exploring Good Visualizations

Get in small groups of 2-3.

Go to [https://www.reddit.com/r/dataisbeautiful/top/](https://www.reddit.com/r/dataisbeautiful/top/). These are all data visualizations created by people like you!

Pick one that you think is particularly good and one that is particular bad. Why? What are the characteristics?

<aside class="notes">
**Teaching tip**:

- Give them time to think about this, then have learners present to the class.
</aside>


---

## Visual Attributes of Good Data Visualization

Some attributes affect our brain more strongly.

In order of focus:

- Position
- Color
- Size

<aside class="notes">
**Teaching Tips**:

- What are some attributes you think are important for data visualizations to have? Some have more of an effect on our brains than others. The ones we tend to focus on most are position, then color, then size.
- Let's take a look at what Jeffrey Shaffer, who teaches data visualization at the University of Cincinnati, thinks:
</aside>

---

## Summary

- The chart type you select should accurately represent the variables you are pulling from data in a way that is clearly readable for your audience.
- Visual considerations include: position, color, order, size. What else?
- With data visualizations becoming increasingly popular, a clean and clear chart goes a long way in conveying a message from a data set.

<aside class="notes">
Teaching Tips:
- Wrap up the learning and share additional resources and next steps.
- If you have extra time at the end, head to the Data is Beautiful reddit page and pull up various visualizations; discuss what makes each one good or bad.
</aside>

---

## Additional Resources

- A great short article on [when pie charts are better?](http://annkemery.com/pie-chart-guidelines/)
- [A gallery of charts](https://github.com/mbostock/d3/wiki/Gallery)
- [A Stats Video](https://www.youtube.com/watch?v=hVimVzgtD6w)
- [SAS: Data Viz](http://www.sas.com/en_us/insights/big-data/data-visualization.html)
- [A guide to when to use each chart](https://drive.google.com/file/d/0Bx2SHQGVqWasT1l4NWtLclJJcWM/view)
- [44 Types of Graphs](http://blog.visme.co/types-of-graphs/)
- [Advice on making good visualizations](https://www.gooddata.com/blog/8-ways-turn-good-data-great-visualizations)
- [Reddit's Data Visualization forum](http://reddit.com/r/dataisbeautiful)
