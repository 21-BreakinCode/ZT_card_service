---
source: python
tags:
- programming/python
---

> [!abstract] Types of sequence in python
> - Types:
> 	- List
> 	- Tuple
> 	- String
> - Hacks: 
> 	- Concatenation --> `+`
> 	- Repetition --> `*`
> 	- Slicing --> `:`

## Types
#### List
-   Ordered: Elements in a list have a specific order
-   Mutable: Lists can be modified after creation
-   Can hold elements of different types
#### Tuples
-   Ordered: Elements in a tuple have a specific order
-   <mark style="background: #FF5582A6;">Immutable</mark>: Tuples <mark style="background: #FF5582A6;">CANNOT be modified</mark> after creation
-   Can hold elements of different types
#### Strings
- Ordered: Characters in a string have a specific order  
- <mark style="background: #FF5582A6;">Immutable</mark>: Strings cannot be modified after creation  
- Can <mark style="background: #FFF3A3A6;">ONLY hold characters</mark>

## Hacking sequences
### Concatenation: `+`
```python
fruits = ["apples", "bananas"]
vegetables = ["carrots", "broccoli"]
shopping_list = fruits + vegetables
```

```python
shopping_list = ["apples", "bananas", "carrots", "broccoli"]
```

### Repetition: `*`
```python
fruits = ["apples", "bananas"]
shopping_list = fruits * 3
```

```python
shopping_list = ["apples", "bananas", "apples", "bananas", "apples", "bananas"]
```

### Slicing: `[:]`
```python
shopping_list = ["apples", "bananas", "carrots", "broccoli"]
selected_items = shopping_list[1:3]
```

```python
selected_items = ["bananas", "carrots"]
```
