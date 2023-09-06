---
source: python
tags:
- programming/python
---
> [!info]- Reference
> - [YT - Corey Schafer](https://www.youtube.com/watch?v=x3v9zMX1s4s)


- The phrase is based on the saying "<mark style="background: #FFF3A3A6;">If it walks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck</mark>". 
- A concept in <mark style="background: #FF5582A6;">dynamic programming</mark> languages, where the type of an <mark style="background: #FF5582A6;">object is determined by the methods and properties</mark> it has, rather than the class it belongs to. 
- In Python, this means that if an object **has the necessary methods and properties**, it can be used as if it **were an instance of a particular class**, even if it is actually an instance of a completely different class.

> [! abstract] Brief
> - As long as an object has the methods and properties that you need, you can **use it as if it were an instance** of a specific class.

```python
class Adder:
    def __init__(self, a):
        self.a = a
    
    def __add__(self, b):
        return self.a + b

result = add(Adder(1), 2) 
# returns 3, even though Adder is not a type of int
```
- In this example, we've created a custom `Adder` class with a `__add__` method. This allows instances of the `Adder` class to be used with the `+` operator, just like integers.
- When we pass an instance of `Adder` to the `add` function, it works just like it would with an integer, even though the class is completely different.