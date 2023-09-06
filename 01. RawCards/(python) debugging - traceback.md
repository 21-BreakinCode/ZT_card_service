---
source: python
tags:
- programming/python
- programming/debug
---
> [!info]- Reference
> - [Doc](https://docs.python.org/3/library/traceback.html)
> - [CSDN blog](https://blog.csdn.net/yuanfate/article/details/119916008)


- 可以清楚知道「哪個檔案 --> 哪一行」出問題
- A module for debugging with python to mimics the behavior of the Python interpreter when it <mark style="background: #FFF3A3A6;">prints a stack trace</mark>.
- msg comes from a name called <mark style="background: #FF5582A6;">traceback</mark> object which is reached by `sys.exc_info()`

### 常用 method
- `print_exc()`
	- 自動執行 `exc_info()` 來獲取 `exc_type`, `exc_value`, `exc_traceback`
	- print out all information
	- Last line will return back what error occurs
