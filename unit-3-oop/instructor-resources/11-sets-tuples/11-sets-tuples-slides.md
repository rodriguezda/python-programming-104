<!--
title: Further Data Structures
type: lesson
duration: 00:40
creator: Steve Peters
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Sets and Tuples</h1>

<!--

## Overview
This lesson focuses on sets and tuples. It starts with sets, encompassing  We Dos as new functions are introduced, then goes into tuples. It ends with the `type` function and a You Do. If there's time, after the "Additional Reading" slides, there is a sets exercise. This exercises are also in the `xx-additional-exercises` folder, if you don't get to it.

## Important Notes or Prerequisites
- The students will be asked to build upon their knowledge of the `list`, so a solid understanding of this concept will be vital.
- The "why" of each datatype is essential to impart to students and your checks for understanding may keep circling back around to the "why".
- Much of this lesson contrasts the three data types (tuples, sets, lists) to each other, so that students can see them side by side and start to internalize the differences.

## Learning Objectives
In this lesson, students will:

- Perform common actions with sets.
- Perform common actions with tuples.
- Know when to use each of the different collection structures.


## Duration
40 minutes

### Timing note:
- If there's time remaining at the end, giving exercises involving multiple contrasting sets, tuples, and lists would be great.
- There is, in the `xx-additional-exercises` folder in the parent folder, a set equals challenge that you should give in class if there's time, and if not, give as homework.

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:02 | Welcome |
| 0:02 - 0:20 | Sets |
| 0:20 - 0:37 | Tuples |
| 0:37 - 0:40  | Summary |

## In Class: Materials
- Projector
- Internet connection
- Python3
-->

---

## Learning Objectives

*After this lesson, you will be able to:*

- Perform common actions with sets.
- Perform common actions with tuples.
- Know when to use different data structures.

<aside class="notes">

**Teaching Tip**:

- Quickly overview these; perhaps write them on the board.

</aside>

---

## Discussion: Lists

Here are some lists:

```python
unique_colors = ["red", "yellow", "red", "green", "red", "yellow"]
subscribed_emails = ["mary@gmail.com", "opal@gmail.com", "mary@gmail.com", "sayed@gmail.com"]
```

What could be a problem here?

<aside class="notes">

**Talking Points**:

- "Why, in the `subscribed_emails` list, would duplicate entries be a problem? Or unique colors having duplicates?"

**Teaching Tip**:

- You can guide students to think about deduplication and the need to ensure unique values, thus dovetailing into sets

</aside>

---

## Introducing Sets


Lists:
```python
unique_colors_list = ["red", "yellow", "red", "green", "red", "yellow"]
subscribed_emails_list = ["mary@gmail.com", "opal@gmail.com", "mary@gmail.com", "sayed@gmail.com"]
```

Sets: an unordered collection of unique elements. These are powerful because set theory operations can be applied to them in O(1) time.
```python
unique_colors_set = {"green", "yellow", "red"}
subscribed_emails_set = {"mary@gmail.com", "opal@gmail.com", "sayed@gmail.com"}
```

- Notice the `{}` versus the `[]`.

<aside class="notes">

**Talking Points**:

- Refresh memories that a *list* is a collection of *elements*, contained within square brackets `[]`.

- Common use cases for sets include membership testing (is element a member of the set?), removing duplicates (de-duping), and computing operations such as union (elements within either of the two sets), intersection (elements common to the two sets), difference (in the first set, but not the second set), and the symmetric difference (ins either set, but not in both... the union minus the intersection).

</aside>


---


## How Can We Make a Set?

If we explicitly cast a set from a list, Python removes duplicates automatically.

```python
my_set = set(a_list_to_convert)

# In action:
unique_colors_list = ["red", "yellow", "red", "green", "red", "yellow"]
unique_colors_set = set(unique_colors_list)
# => {"green", "yellow", "red"}

# In action:
unique_colors_set_2 = set(["red", "yellow", "red", "green", "red", "yellow"])
# => {"green", "yellow", "red"}
```

We can make a set directly using curly braces:

```python
colors = {"red", "orange", "yellow", "green", "blue", "indigo", "violet"}
```

<aside class="notes">

**Talking Points**:

- "Creating a *set* is easy; we just need to use the `set()` built-in function like this."

- "Because we had two `red`s, Python removed the extra one for us."

**Teaching Tip**:

- Point out the difference between parentheses, brackets, and curly braces.

</aside>


</aside>

---

## Important Note: Sets

Lists are always in the same order:

- `my_list = ["green", "yellow", "red"]` is always going to be`["green", "yellow", "red"]`
- `my_list[0]` is always  `"green"`; `my_list[1]` is always `"yellow"`; `my_list[2]` is always `"red"`.

Sets are not like this! Similar to dictionaries, they're not ordered.

- `my_set = {"green", "yellow", "red"}` could later be `{"red", "yellow", "green"}`!
- Note that python defaults to displaying an ascending sort of a set. Although this is displayed to the user when the variable is called via the interpreter, _the order cannot be relied upon_.

We **cannot** do:  `my_set[0]` - sets are unordered, and a `TypeError`
exception will be thrown.

---

## We Do: Creating a Set from a List

Let's pull up a new `set_practice.py` file and make some sets!

- Make a list `clothing_list` containing the main color of your classmates' clothing.
- Using `clothing_list`, make a set named `clothing_set`.
- Use a `for` loop to print out both `clothing_list` and `clothing_set`.
- Try to print an index!

<aside class="notes">

**Teaching Tips**:

- Run through this with them - make sure they are following along to practice typing the syntax.
- Be prepared to refresh memories on `for` loops.
- Try to print an index - reinforce that sets are in any order.

</aside>

---

## We Do: Adding to a Set

How do we add more to a set?

```python
# In a list:
clothing_list.append("red")

# In a set
clothing_set.add("red")
```

`add` vs `append` - this is because we can't guarantee it's going at the end!

Let's add a few colors to `clothing_list` and `clothing_set` and then print them.

- What happens if you add a duplicate?

<aside class="notes">

**Talking Points**:

- Continue locally with the list and set they created previously - do this with them!
- Try to add a duplicate, then print. Call out that it just doesn't appear, since sets can't have duplicates.

</aside>

---

## We Do: Removing from a List and a Set

Remember, lists are always the same order and sets are not!

- With the set `{"green", "yellow", "red"}`, `my_set[0]` could be `green`, `red`, or `yellow`.

So thus, we need to be careful about removal:

```python
# In a list:
clothing_list.pop() # Removes and returns the last item in the list.
clothing_list.pop(0) # Removes and returns a specific (here, the first) item in the list.

# In a set
clothing_set.pop() # Removes and returns an arbitrary element. This is probably not what you want to do in most cases.
clothing_set.pop(0) # Python throws a TypeError error (pop takes no arguments)
clothing_set.remove('red') # This removes an element from the set directly, and raises KeyError if the element is not present. This is the most common use.
clothing_set.discard('red') # This removes an element from the set directly, but does NOT throw a KeyError if the element is not present in the set.
```

<aside class="notes">

**Teaching point**:

- Walk through these. `pop` from the set to show that it's unreliable.

**Talking Points**:

- Address that for lists, the order matters. For sets, it's irrelevant, so `pop` returns an arbitrary element.
- Discuss the difference between `remove`, `pop`, and `discard`

</aside>
---

## We Do: Set Intersection

- One thing that sets are _really_ good at is _relational algebra_ (set theory). This is a fancy word for a SQL join, or comparing elements between two sets.
- Sets are really good at this because they use the same [hashing trick](https://en.wikipedia.org/wiki/Hash_table) under the hood that dictionaries use and makes them so fast.

Let's start by making two sets:
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
```

<aside class="notes">

**Teaching points**:

- Take this opportunity to talk about how Pandas and SQL both use this trick under the hood and abstract it from the user.
- We'll be working with set differences in just a second, so curb any questions on that.

</aside>
---

## We Do: Set Intersection


Now let's use the `.intersection()` set method to find out _what elements these two sets have in common_:
```python
set1.intersection(set2)
```

Yields the result:
```python
{4, 5}
```

- This makes sense, the two sets share the elements `4` and `5`.
- Note that this is commutative, meaning we could also write `set2.intersection(set1)` and receive the same result.

<aside class="notes">

**Teaching point**:

- We'll be doing set differences in the next exercise, so curb any questions on that.

</aside>

---

## We Do: Set Differences

- Instead of finding _elements in common_ between two sets, we can also find _their differences_.
- To do this, we use `.difference()`.
- Note that this method _is not commutative_, meaning _order matters_.
- The difference is what is contained in the _first_ set, _but not in the second set_.

```python
set1.difference(set2)
```

Yields the result:
```python
{1, 2, 3}
```

```python
set2.difference(set1)
```

Yields the result:
```python
{6, 7, 8}
```

<aside class="notes">

Teaching points:

- Ask students to think of an example of when they've had to use this in the past.
- A good topic of conversation is how you might perform this action in excel - can the students come up with a way?

</aside>

---

## Quick Review: Sets vs. Lists

**Lists**:

- The original, normal object.
- Created with `[]`.
- `append()`, `insert(index)`, `pop()`, `pop(index)`.
- Duplicates and mutable.

**Sets**:

- Lists without duplicates.
- Created with `{}` or with `set(my_list)`.
- `add()` and `remove(element)`.

<aside class="notes">

**Teaching Tips**:

- A code review for all of these are on the next slide.
- Review these - on this slide, do a check for conceptual understanding.
</aside>

## Quick Review: Sets vs. Lists

```python
### Creation ###
# List
my_list = ["red",  "yellow", "green", "red"]
# Sets
my_set = {"red",  "yellow", "green"}
my_set2 = set(my_list)
my_set = set(a_list_to_convert)

### Appending a New Value ###
my_list.append("blue")
my_set.add("blue")

### Appending a Duplicate ###
my_list.append("blue")
# => my_list = ["red",  "yellow", "green", "red", "blue",  "blue"]
my_set.add("blue")
# => my_set = {"red",  "yellow", "green", "blue"}

### Removing items: ###
my_list.pop(1)
my_set.remove("red")
```

<aside class="notes">

**Teaching Tips**:

- Do a quick check for understanding.
- Go through each example.

**Talking Points**:

- Point out again the difference in syntax, especially with curly braces.
- Reinforce `pop` being unreliable.

</aside>

---

## Discussion: Immutability Thoughts

A set is a type of list which doesn't allow duplicates.

What if, instead, we have a list we don't want to change?

```python
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
```

We **don't** want:
```python
rainbow_colors[0] = "gray"
## Gray's not in the rainbow!
rainbow_colors.pop()
## We can't lose violet!
rainbow_colors.append("pink")
# Pink's not in the rainbow!
```

We want `rainbow_colors` to be **immutable** - the list _cannot_ be changed.

How we do that in Python?

<aside class="notes">

**Talking Points**:

- We do it with sets.
- Immutable means "unchangeable".

</aside>

---

## Introducing: Tuples

**Sets** have the following properties:

- No duplicates
- Mutable

**Tuples** are similar to a list with the following differences:

- Allows duplicates (same as a list)
- Once assigned, the tuple _cannot be changed_

```python
rainbow_colors_tuple = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
```

When should you use a tuple?

- When you need data protection through immutability (note: all Python variables are public).
- When you never want to change the list.
- Tuples are sometimes wrapped in a class namespace to simulate what would be done with a [const structure](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/how-to-define-constants) in a C-based language.
- This is a way of holding appconstants, or constants your program will use (like the API endpoint of a server, credentials, etc.)

<aside class="notes">

**Talking Points**:

- Point out that with tuples, duplicates are fine! Be clear that tuples are another kind of list, NOT a kind of set.
* Python offers a data structure that provides more secure usage than the wide power of a fully mutable list.
* The **tuple** is a kind of data structure that provides immutable values in a list.
* Once a tuple is created and assigned its elements, no changes can be made to the tuple.
* "Why? Isn't it more useful to work with a list that allows us to change elements when necessary? Doesn't this inflexibility make our code easier to break?
- "We will frequently need the power to create and edit lists, adding and removing items from them. In these instances, use a list."
</aside>

---

## Tuple Syntax

- Created with parentheses `()`.
- Access values via indices (like regular lists, but *not* like sets).

```python
rainbow_colors_tuple = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
print(rainbow_colors[1])
# Prints "orange"
```

- Tuples can be printed with a `for` loop (just like a set or list!).

```python
rainbow_colors_tuple = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")

for color in rainbow_colors_tuple:
  print(color)
```

<aside class="notes">
**Talking Points**:

- Tuples work exactly like lists, except that, when you create a tuple, you use parentheses instead of square brackets.
- You can include anything you want, but, for now, we'll add strings.

</aside>

---

## We Do: Tuples

Let's declare a tuple named `seasons` and set it to have the values `fall`, `winter`, `spring`, and `summer`. We'll print the tuple and each value. Then we'll try to reassign them (we can't)!

<iframe height="400px" width="100%" src="https://repl.it/@GAcoding/blank-repl?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

**Teaching Tips**:

- Make sure they're doing this with you.
- Print out each value directly with indexes. Then, use a `for` loop.
- Try to change values - pop, append, and direct reassignment.

Talking point:

- Remind them of the syntax - perhaps make sets and lists as well, so students can see them compared again.

</aside>

---

## Quick Review: Sets, Tuples, Lists

**List**:

- The original, normal object: `["red", "red", "yellow", "green"]`.
- Has duplicates; mutable: `append()`, `insert(index)`, `pop()`, `pop(index)`

**Set**:

- List without duplicates: `{"red", "yellow", "green"}`.
- Mutable: `add()` and `remove(element)`

**Tuple**:

- Has duplicates, but immutable: You can't change it!
- `("red", "red", "yellow", "green")` will *always* be `("red", "red", "yellow", "green")`.

<aside class="notes">

**Teaching Tips**:

- A code review for all of these are on the next slide.
- Remind them about `add` vs `append` - this is because we can't guarantee it's going at the end!
- Review these - on this slide, do a check for conceptual understanding.
- Always reinforce the `[]` vs `{}` vs `()`
- Recap immutability.
</aside>

---

## Quick Review: Sets, Tuples, Lists

```python
### Creation ###
# List
my_list = ["red",  "yellow", "green", "red"]
# Sets
my_set = {"red",  "yellow", "green"}
my_set2 = set(my_list))
my_set = set(a_list_to_convert)
# Tuples
my_tuple = ("red",  "yellow", "green")

### Appending a New Value ###
my_list.append("blue")
my_set.add("blue")
# Tuples -> You can't!

### Removing items: ###
my_list.pop(1)
my_set.remove("red")
# Tuples -> You can't!
```

<aside class="notes">

**Teaching Tips**:

- Do a check for understanding of the code syntax.
- Go through each example.

**Talking Points**:

- Recap the types of braces to create each; remove vs pop; append vs add.
- Remind students that they aren't expected to be syntax experts - they can always look this up. Working programmers look things up every day on the job, but students have to know what things are and what to expect.

</aside>

---

## Introducing Types

Variables certainly can hold a lot!

- Sets, tuples, and lists are easily confused.
- `type()` tells us what a variable is: set, tuple, list, dictionary, integer, string - anything!

Try it:

<iframe height="300px" width="100%" src="https://repl.it/@GAcoding/python-programming-types?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">

**Talking Points**:

- It's useful to know what datatype a variable is and how to use it. This will work on anything.

**Teaching Tips**:

- Walk through each of these. It will recap the syntax as well as re-inforce using `type`. You might want to open the repl.it in a new window, as it's a bit long.


**Repl.it Note**: This replit has:
```python
unique_colors = set(["red", "yellow", "green", "red"])
print("unique_colors is", type(unique_colors))
# --
unique_colors_2 = ["red", "yellow", "green", "red"]
print("unique_colors_2 is", type(unique_colors_2))
# --
unique_colors_3 = ("red", "yellow", "green", "red")
print("unique_colors_3 is", type(unique_colors_3))
# --
my_number = 2
print("my_number is", type(my_number))
# --
my_string = "Hello!"
print("my_string is", type(my_string))
```

</aside>

---

## You Do: List Types Practice

Create a local file, `sets_tuples.py`. In it:

- Create a list (`[]`), set (`{}`), and tuple (`()`) of some of your favorite foods.
- Create a second set from the list.

Next, in every list type that you can:

- Add `"pizza"` anywhere; append `"eggs"` to the end.
- Remove `"pizza"`.
- Re-assign the element at index `1` to be `"popcorn"`.
- Remove the element at index `2` and re-insert it at index `0`.
- Print the element at index `0`.

Print your final lists using a loop, then print their types. Don't throw an error!

<aside class="notes">

10 minutes

**Teaching Tips**:

- Give students time to do this - it's a lot of syntax to go back through and find.
- Walk around the room to check for questions and offer help when needed.
- Once most of them have it, go over the answer. Make sure you remove pizza in the list, too.

</aside>


---

## Summary and Q&A

We've learned two new types of lists:

Sets:

- A mutable list without duplicates.
- Handy for storing emails, usernames, and other unique elements.

```python
email_set = {'my_email@gmail.com', 'second_email@yahoo.com', "third_email@hotmail.com"}
 ```

Tuples:

- An immutable list that allows duplicates.
- Handy for storing anything that won't change.

```python
rainbow_tuple = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
```

---

## Additional Reading

- [Repl.it that recaps Tuples](https://repl.it/@GAcoding/python-programming-tuple-practice?lite=true)
- [Python Count Occurrences of Letters, Words and Numbers in Strings and Lists-Video](https://www.youtube.com/watch?v=szIFFw_Xl_M)
- [Storing Multiple Values in Lists](https://swcarpentry.github.io/python-novice-inflammation/03-lists/)
- [Sets and Frozen Sets](https://www.python-course.eu/sets_frozensets.php)
- [Sets](https://www.learnpython.org/en/Sets)
- [Python Tuple](https://www.programiz.com/python-programming/tuple)
- [Tuples](http://openbookproject.net/thinkcs/python/english3e/tuples.html)
- [Strings, Lists, Tuples, and Dictionaries Video](https://www.youtube.com/watch?v=19EfbO5D_8s)
- [Python Data Structures: Lists, Tuples, Sets, and Dictionaries Video](https://www.youtube.com/watch?v=R-HLU9Fl5ug)
