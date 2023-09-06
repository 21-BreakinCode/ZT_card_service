---
source: python
tags:
- programming/python
---
> [!info]- Ref
> - [Python Merge Dictionaries - Combine Dictionaries (7 Ways) • datagy](https://datagy.io/python-merge-dictionaries/)
# Merge action
## 3 ways
> [!abstract] `**` or `.update()` or `|`, `|=`
- `**`
	- use to <mark style="background: #FF5582A6;">unpack</mark> the dictionary to **'key: value'**
	- get the `key`: `value` in this dictionary
- `dict1.update(dict2)`
	- merge dict2 to dict1 --> merge to <mark style="background: #FF5582A6;">previous object</mark>
- `|` or `|=` (python v3.9+)
	- For `|`:
		- merge the dictionary to <mark style="background: #FF5582A6;">new object</mark>
	- For `|=`: 
		- merge the dictionary to <mark style="background: #FF5582A6;">previous object</mark>
- <mark style="background: #FFF3A3A6;">Keys existed</mark> cases
	- Will overwrite the previous one（後面 dict 為主)
## examples
```python

dict1 = {'a': 1, 'b': 2} 
dict2 = {'c': 3, 'd': 4} 

dict3 = dict1 | dict2 
# dict3 = {'a':1, 'b': 2, 'c': 3, 'd': 4}
  
dict1 |= dict2
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict3 = {**dict1, **dict2}
# dict3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

####### Keys existed cases #########
dict_share_key = {'e':7, 'a': 100}

dict4 = dict1 | dict_share_key
# dict4 = {'a': 100, 'b': 2, 'c': 3, 'd': 4}

dict5 = dict_share_key | dict1
# dict5 = {'a':1, 'b': 2, 'c': 3, 'd': 4}
```