---
source: python
tags:
- programming/python
---
> [!abstract]
> Allow to extend or modify behavior of functions/methods

- 參考：
	- [[(python) classmethod decorator]]

- Takes **function** as argument
```python
# Using decorator
@decorate
def print_out(*args):
	print(*args)

if __init__ == '__main__':
	print_out("Hello World")

# Same as this one
decorate(print_out("Hello World"))

############ inside decorator ############
def decorator(func):
	def inner():
		"""
		Do something in this function
		"""
		result = ''
		return result
	return inner
#########################################
```

- multi-decorators: the innermost decorator run first
```python
@dec1  # Run 2nd
@dec2  # Run 1st
def add(a, b):
	return a + b
```