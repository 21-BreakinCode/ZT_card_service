---
source: python
tags:
- programming/python
---
> [!abstract]
> - A way to capture state from enclosing scope in a function
> - capture state

# Global vs. Local 
- Python var 有分 global & local 
- function 內外為區分標準

```python
b = 9
def test():
	print(b)
	b = 10
```
`>>>` error
- 因為 global b(=9) 無法 access 進去 function 裏面，要用 `global` key word 叫

```python
b = 9
def test2():
	global b  # call the global var b
	print(f'{b= }')
	b = 19
```
`>>>` b = 9

# Capture state
- Keyword: `nonlocal`
```python
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

counter1 = counter()
print(counter1()) # 1
print(counter1()) # 2

counter2 = counter()
print(counter2()) # 1
```