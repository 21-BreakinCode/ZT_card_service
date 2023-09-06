---
source: python
tags:
- programming/python
---

> [!info]- Easier ask for forgiveness than permissions
> Video: [Duck Typing and EAFP](https://www.youtube.com/watch?v=x3v9zMX1s4s)
- <mark style="background: #FFF3A3A6;">"Easier to ask forgiveness than permission"</mark> (EAFP) is a coding philosophy that encourages you to **assume that things are valid until an exception is raised**, rather than checking for validity beforehand. 
- This is often more concise, faster, and easier to read than using explicit if-statements to validate input. 
- In Python, this is achieved by using **exceptions to control the flow of execution**. For example, instead of checking if a key exists in a dictionary before trying to access it, you can <mark style="background: #FF5582A6;">simply use a try/except block</mark> to catch the KeyError exception that will be raised if the key does not exist.

> [! abstract] Brief
> - Using `try/except` statement than `if/else` statement

```python
# complete person
person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}
# un-complete person
person = {'name': 'Jess', 'age': 23}

# EAFP way (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}.".format(**person))
except KeyError as e:
    print(f"Missing {e} key")

# Non-Pythonic way
if 'name' in person and 'age' in person and 'job' in person:
	print("I'm {name}. I'm {age} years old and I am a {job}.".format(**person))
else:
	print("Missing some keys")
```