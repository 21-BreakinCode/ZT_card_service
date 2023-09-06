---
source: python
tags:
- programming/python
- programming/debug
---
> [!info] Reference
> - [Python: 簡易除錯模組 pdb @ hoamon's sandbox](http://www.hoamon.info/blog/2007/02/01/pythonpdb.html)
> - [使用Python內建的pdb和breakpoint()進行程式debug](https://yanwei-liu.medium.com/debug-python-program-with-pdb-and-breakpoint-3a8834d8081)

- A module for debugging with python to <mark style="background: #FF5582A6;">set break point in run time</mark>
- `pdb.set_trace()` --> setting break point

- Useful cmd in pdb runtime
	- `p`: print out the var
	- `c`: continue till next break point
	- `n`: next step
	- `q`: quit pdb