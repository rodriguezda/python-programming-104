<!---
This lesson was developed by Steven Peters for Python five-day course.

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack @steve.peters.
--->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Class Inheritance</h1>

<!--

## Overview
This lesson assumes knowledge of classes and dives straight into the concept of inheritance. After a We Do to build a child class, there's an I Do that walks through overwriting the parent variables and methods. If there's time, assign an exercise! It's in the `xx-additional-exercises` folder (it's too long for a slide). Otherwise, assign it for homework.

## Important Notes or Prerequisites
- Students have just learned about classes! Go slowly here. Make sure everyone's confident with classes.

## Learning Objectives
In this lesson, students will:

- Implement inheritance.
- Describe what has been inherited from one class to another.
- Overwrite variables and methods.


## Duration
20 minutes

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:10 | Creating a Child Class |
| 0:10 - 0:18 | Overwriting Variables and Methods |
| 0:18 - 0:20 | Summary |

## Differentiation and Extensions
- In the interest of time, this does not have a You Do for overwriting attributes or methods. It has a Knowledge Check question, but feel free to add exercises!
- If students get this easily, introduce multiple inheritance — perhaps an `iPhone 8` class, inheriting from `IPhone`.
- There is, in the `xx-additional-exercises` folder in the parent folder, an inheritance challenge that you should give in class if there's time. If not, give as homework. It's quite long.

## In Class: Materials
- Projector
- Internet connection
- Python 3
-->

---

## Learning Objectives

*After this lesson, you will be able to…*

- Implement inheritance.
- Describe what has been inherited from one class to another.
- Overwrite variables and methods.

---

## Discussion: Similar Classes

`Phone` is a class — there are hundreds of types of phones.

- What attributes and functions would a `Phone` have?

What about an `iPhone`? Or `android_phone`?

- `iPhone` and `android_phone` would be objects of the `Phone` class.
- But, there are different types of iPhones and Android phones.
- Should `IPhone` and `AndroidPhone` be classes themselves?

What would you do?

<aside class="notes">

**Teaching Tips:**

- Have students brainstorm what a `Phone` class would contain.

**Talking Points:**

You could go further:
- You could say `IPhone` is a class — there are many types of iPhones.
  - What specific attributes would an `IPhone` have apart from other phones?
- You could say `AndroidPhone` is a class — there are many types of Android phones.
  - What specific attributes would an `AndroidPhone` have apart from other phones?"
- `AndroidPhone` and `IPhone` are separate classes. However, they are both types of `Phone`.
</aside>

---

## Introduction: Inheritance

`AndroidPhone` and `IPhone` are separate classes *and* in the `Phone` class.

This is called **inheritance**: making classes that are subsets of other classes.

`Phone` is the **parent** class. It's a regular class! All phones:

- Have a phone number.
- Can place phone calls.
- Can send text messages.

`IPhone` is a **child** class. The child class **inherits** methods and properties from the parent class but can also define its own functionality. iPhones uniquely:

- Have an `unlock` method that accepts a fingerprint.
- Have a `set_fingerprint` method that accepts a fingerprint.


<aside class="notes">

**Teaching Tips:**

- Brainstorm the differences between the phone classes.
- This can be hard to wrap your head around in programming, so give real-world examples. Mystery novels are a type of book, but there are tons of those. Sofas are a type of couch, which are a type of chair.


**Talking Points:**

- Inheritance allows us to extend functionality defined in a `parent` class (`Phone`) and create `child` classes (e.g., `IPhone`, `AndroidPhone`) that extend and compartmentalize different pieces of functionality.
- When we define a class to represent a `Phone`, we can add the basic properties and functionality that all phones have.

</aside>

---

## We Do: Inheritance

All phones have a phone number, can place phone calls, and can send text messages.

Start a new file, `Phone.py`. In it, let's start and test the class:

```python
class Phone:
  def __init__(self, phone_number):
    self.number = phone_number

  def call(self, other_number):
    print("Calling from", self.number, "to", other_number)

  def text(self, other_number, msg):
    print("Sending text from", self.number, "to", other_number)
    print(msg)

test_phone = Phone(5214)
test_phone.call(515)
test_phone.text(51121, "Hi!")
```

<aside class="notes">

**Teaching Tips:**

- Have them start a new file and do this with you!
- Make sure students follow along, but don't discourage copying and pasting from the slide — it's a lot to type up!
- Classes are still pretty new — talk through each line as you write it.
</aside>

---

## We Do: `IPhone` Class

Underneath the `Phone` class definition, let's create the `IPhone` class.

```python
class IPhone(Phone):
  # Class definitions accept a parameter specifying what class they inherit from.
  def __init__(self, phone_number):
    # super()` calls the `init` defined in the parent class.
    super().__init__(phone_number)
    # Now self.number is set, because that's what happens in the parent Phone _init_.
```

<aside class="notes">

**Teaching Tips:**

- Walk through this line by line. When you get to super, scroll up to point out `Phone`'s super.

**Talking Points:**

- After we define `Phone`, we can create classes that *inherit* from the `Phone` class and add their own properties and functionality.
- Let's define two new classes that inherit from the `Phone` class.
- Notice how the `IPhone` class doesn't repeat the code that attaches the `phone_number` passed to the `__init__` method to the `self` reference.
- The `IPhone` class calls the parent constructor through the super method and allows the parent class to execute that default behavior.
</aside>

---

## We Do: `IPhone` Class

iPhones uniquely:

- Have an `unlock` method that accepts a fingerprint.
- Have a `set_fingerprint` method that accepts a fingerprint.


```python
class IPhone(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)

    # Under the call to super, we can define unique IPhone variables.
    # Regular Phone objects won't have this!
    self.fingerprint = None

  # Here are methods unique to IPhone objects:
  def set_fingerprint(self, fingerprint):
    self.fingerprint = fingerprint

  def unlock(self, fingerprint=None):
    if (fingerprint == self.fingerprint):
      print("Phone unlocked. Fingerprint matches.")
    else:
      print("Phone locked. Fingerprint doesn't match.")
```


<aside class="notes">

**Teaching Tips:**

- Make sure students are still following along, conceptually and in their file.  
- Walk through this carefully. Recap that methods are just class functions.
</aside>


---

## Side Discussion: Edge Cases

Look at:

```python
def unlock(self, fingerprint=None):
  if (fingerprint == self.fingerprint):
    print("Phone unlocked. Fingerprint matches.")
  else:
    print("Phone locked. Fingerprint doesn't match.")
```

What if `self.fingerprint` is currently `None`? We need to account for this!

```python
def unlock(self, fingerprint=None):
  if (self.fingerprint == None):
    print("Phone unlocked. No fingerprint needed.")
  elif (fingerprint == self.fingerprint):
    print("Phone unlocked. Fingerprint matches.")
  else:
    print("Phone locked. Fingerprint doesn't match.")
```

When programming, always watch for **edge cases**. This isn't specific to classes!


<aside class="notes">

**Teaching Tips:**

- Be very clear that this isn't specific to classes — it's something to always watch out for, in functions, `for` loops, and anything at all. Note that this is a reason why pseudocode is so important.
</aside>


---

## We Do: Testing `IPhone`

Add some test lines at the bottom:
```python
my_iphone = IPhone(151)
my_iphone.unlock()
my_iphone.set_fingerprint("Jory's Fingerprint")
my_iphone.unlock()
my_iphone.unlock("Jory's Fingerprint")

# And we can call the Phone methods:
my_iphone.call(515)
my_iphone.text(51121, "Hi!")
```

Try it! Then, try this. Why does it fail?

```python
# Let's try a Phone object on an iPhone method.
test_phone.unlock()
```

<aside class="notes">

**Talking Points:**

- We can create `IPhone`s, `AndroidPhone`s, and still regular `Phone`s. `Phone` is being used as a parent class, but it's still a class!
- Inheritance is an extremely powerful feature of classes.
- It allows us to create "generic" parent classes, such as the `Phone()` class, and then create child classes like `IPhone()` that represent subsets of the parent class.
- We change the characteristics of the object when we define the `IPhone()` class.
- Because it inherits from `Phone()`, we're still able to use the parent methods `call()` and `text()`.
  - We don't need to rewrite these methods in the child class.
- Using inheritance, you can easily create hierarchies of functionality. This keeps your code clean and intuitive.
</aside>

---

## Quick Recap: Inheritance

- A class can inherit from another class — a parent class and a child class.
- The child class can declare its own variables and methods, but it also has access to all the parents'.


```python
## Parent class: A regular class ##
class Phone:
  def __init__(self, phone_number):
    self.number = phone_number

  def call(self, other_number):
    print("Calling from", self.number, "to", other_number)

test_phone = Phone(5214) # It's a regular class!
test_phone.call(515)

## Child class: Pass in the parent class and call super() ##
class IPhone(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)

    # Under the call to super, define unique child class variables and methods.
    # Parent class objects won't have this!
    self.fingerprint = None

  def set_fingerprint(self, fingerprint):
    self.fingerprint = fingerprint

my_iphone = IPhone(151) # Create an object as usual.
my_iphone.set_fingerprint("Jory's Fingerprint") # Call a method.
my_iphone.call(515) # Call a method from the parent class.
```


---


## I Do: Overwriting Attributes

**Next up: Overwriting attributes!**

Let's switch to a new example. You don't need to follow along.

Here's a regular `Building` class:

```python
class Building(object):
 # Class variables
 avg_sqft = 12500
 avg_bedrooms = 3

 # No __init__ - there are no instance variables to declare!
 # This is possible in any class, not just inheritance. (Building is a normal class.)

 def describe_building(self):
  print('Avg. Beds:', self.avg_bedrooms)
  print('Avg. Sq. Ft.:', self.avg_sqft)

 def get_avg_price(self):
  price = self.avg_sqft * 5 + self.avg_bedrooms * 15000
  return price

my_building = Building()
my_building.describe_building()
```

<aside class="notes">

**Teaching Tips:**

- This is run as an I Do to save time and typing. Run it as a We Do if you think students need the practice typing everything out (and you have time). Because it introduces new concepts, don't run it as a You Do.
- There's no `init`! This is new. Note that this isn't unique to inheritance — right now, this is a regular class.
- Call out the order of operations for the price math.
- This is a regular class, but walk through each line.

**Talking Points:**

- Here's a new class.
- In it, we have some attributes for the average square feet, bedrooms, and bathrooms of a building. We also have two functions: one to print the attributes out in `describe_building()` and one to calculate the average price and return it based on those attributes in `get_avg_price()`.
-  *Note:* When we define our `Building()` class and specify `Building(object)` in the definition, we're indicating that the `Building()` class we're creating _inherits_ characteristics from the `object` class.
- The built-in `object` class in Python is the most basic "parent class" we could have.
</aside>

---

## I Do: Inheriting Building

Inheriting from `Building`, we can create a `Mansion` class.

```python
# Call in the parent, Building, to the class definition.
class Mansion(Building):
  # Our child class definition goes here.
  # Will have the same class variables, instance variables, and methods as Mansion objects.
```

---

## Overwriting Variables

What if we want the class variables to have different values? We can set new ones. Remember, child classes do not affect the parent class.

```python
class Mansion(Building):
   # Overwrite the class variables.
   avg_sqft = 6
   avg_bedrooms = 1

   # We don't have a call to super __init__. Why?
   # There's no __init__ in the parent to call!

### Now, let's try it out. ###
# This still has the old values.
my_building = Building()
my_building.describe_building()

# The mansion object has the new class variables!
avg_mansion = Mansion()
avg_mansion.describe_building()
```

<aside class="notes">

**Teaching Tips:**

- Run this!
- Do this in the same file so students can see the different class variables on the screen. Scroll up and point them out.
- Note that `Mansion` is an entire class! Classes don't need to be fancy.

**Talking Points:**

- In this class definition, the average square feet, bedrooms, and bathrooms have been changed, but nothing else has been done.
- Because the `Mansion()` class _inherits_ from the `Building()` parent class, it has access to the class methods we defined for `Building()`.
- It is important to note that child classes do not affect the functionality of the parent class. Below, we've added a function, `how_big()`, to the `Mansion()` class.
- We don't have super because there's no `init` in the parent!
</aside>

---

## Discussion: Child Class Methods

In the `Building` class, we have:

```python
def get_avg_price(self):
 price = self.avg_sqft * 5 + self.avg_bedrooms * 15000
 return price
```

What if a `Mansion`'s price calculation is different? What do you think we can do?

<aside class="notes">

**Teaching Tips:**

- Start a discussion. See if students can guess that, like overwriting class variables, we can overwrite methods.

</aside>

---

## Overwriting Methods

We know that we can overwrite variables. Turns out, we can also overwrite methods!

```python
class Mansion(Building):

 def get_avg_price(self):
  return 1000000

mans = Mansion()
bldg = Building()

bldg.get_avg_price()
# # returns `self.avg_sqft * 5 + self.avg_bedrooms * 15000`

mans.get_avg_price()
# Returns 1000000
```


<aside class="notes">

**Teaching Tips:**

- Run this!

</aside>

---

## Quick Review

When we make child classes, we can overwrite class variables and methods.

```python
class Building(object):
   # Class variables
   avg_sqft = 12500
   avg_bedrooms = 3

   def get_avg_price(self):
      price = self.avg_sqft * 5 + self.avg_bedrooms * 15000
      return price


class Mansion(Building):
   # Overwrite the class variables.
   avg_sqft = 6
   avg_bedrooms = 1

  def get_avg_price(self):
    return 1000000
```

<aside class="notes">

**Teaching Tips:**

- Do a quick check for understanding.

</aside>

---


## Knowledge Check

Consider the following classes:

```python
class Animal(object):
   def is_mammal(self):
      return True
   def is_alive(self):
      return True

class Grasshopper(Animal):
   def is_small(self):
      return True
```

You instantiate two objects: `bug = Grasshopper()` and `cat = Animal()`. Which of the following instance methods are available for each?

1. `bug.is_mammal()`
2. `bug.is_alive()`
3. `bug.is_small()`
4. `bug.is_animal()`

<aside class="notes">

**Teaching Tips:**

- Give them a few minutes to guess.
</aside>


---

## Summary and Q&A

Inheritance:

- Allows us to make classes using other classes as templates.
- Has a **parent** class (`Phone`) and a **child** class (`IPhone`).
  - The parent class is still a usable class!

Child classes:

- `inherit` methods and properties from a parent class.
- Have access to all of the functionality of its parent.
- Can have new attributes and methods.
  - They won't be available to the parent.
- Can overwrite values from the parent class.


<aside class="notes">

**Teaching Tips:**

- Do a quick check for understanding.
- If there's time, assign an exercise! It's in the `xx-additional-exercises` folder. Otherwise, assign it for homework.

</aside>
