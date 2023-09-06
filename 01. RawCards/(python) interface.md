---
source: python
tags:
- programming/python
---
- Defines a <mark style="background: #FFF3A3A6;">protocol</mark> or a <mark style="background: #FFF3A3A6;">set of method</mark>
- A **file-like object** must behaves certain methods
	- The `FileLikeObject` class is an <mark style="background: #FF5582A6;">Abstract Base Class (ABC)</mark> that defines the protocol for a file-like object.
- If an object does not implement these methods, it will raise a `NotImplementedError` when they are called.

```python
import io

# Parent class -> Interface
class FileLikeObject(io.IOBase):
    def read(self, size=-1):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

# Child class -> implement method
def read_data(file_like_object):
    data = file_like_object.read()
    return data
```