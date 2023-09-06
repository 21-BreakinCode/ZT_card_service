---
source: python
tags:
- programming/python
---
- `@property`: A type of ***decorator***
	- define a method as a <mark style="background: #FF5582A6;">getter</mark> for class attribute
	- useful when you want to add some logic or validation when getting an `private` or `protected` attribute's value.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # asign private attr

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius * self._radius

# Creating an instance of Circle
circle = Circle(5)

# Accessing the radius attribute using the property
print(circle.radius)  # Output: 5

# Using the setter method through the property
circle.radius = 7

# Accessing the area attribute using the property
print(circle.area)    # Output: 153.93791499999999

```