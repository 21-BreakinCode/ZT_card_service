---
source: python
tags:
- programming/python
- programming/principle
---
> [!info] References
> - [freeCodeCamp](https://www.youtube.com/watch?v=Ej_02ICOIgs)

> [!abstract]- 其他參考
> - [[(python) classmethod decorator]]
> - [[(python) property decorator]]
> - [[(python) inheritance with super()]]


- `Methods`: represent of functions in the class
- Args explain:
	- **_self_** : the self <mark style="background: #FFF3A3A6;">represent the class instance</mark> that has be created & use as a argument to pass into the method
	- **_instance level attributes_**: `def __init__()`, one of the _magic method_ that can <mark style="background: #FFF3A3A6;">use for creating the instance</mark> with predefined instance attributes in the class attribute
	- **_class level attribute_**: belong to <mark style="background: #FFF3A3A6;">class itself</mark>, but can also access from instance level
```python
class Item:
	# class level attributes -> UPPER CASE
	CLASS_ATTRIBUTES = ''

	# instance level attributes -> init() method
	def __init__(self, name: str, price: float, quantity=0): 
		# Run validations & return specific output
		assert price > 0, f"{price=} is not greater than zero!"
		assert quantity >= 0, f"{quantity=} is smaller than zero!"

		# Assign to self object
		self.name = name
		self.price = price
		self.quantity = quantity

	# create method
	def example_method(self):
		# call instance attribute by using "self" key word
		total = self.quantity * self.price

		# call class attribute by using "self" key word
		example = f"Calling class attr: {self.CLASS_ATTRIBUTES}"
		return total


# Create instance via class and assign specific instance attributes
item1 = Item(name="Phone", price=300, quantity=3)
# Overwrite the class attribute via instance level
item1.CLASS_ATTRIBUTES = "Class Attributes"
```

