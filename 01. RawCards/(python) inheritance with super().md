---
source: python
tags:
- programming/python
---
> [!info]- Reference
> - [iT邦邦忙](https://ithelp.ithome.com.tw/articles/10222948)

- Parent class --> 最原始的 `Base clase`
- Child class --> 繼承 parent class 的 `Inheritance class`
- `__super__()` --> inherit parent class kewword <mark style="background: #FFF3A3A6;">function</mark>

```python
# Parent class
class BaseModel:
	def __init__(self, attribute1:str, attribute2:int):
		self.attribute1 = attribute1
		self.attribute2 = attribute2


# Child class
class Inheritance(BaseModel):
	def __init(self, attibute1, attribute2, new_attribute):
		super().__init(attribute1, attribute2)
		self.new_attribute = new_attribute

# Interitance class 會有 Base Model 的 2 個 instance attribute 
# + 自己新的 "new_attribute"
```