---
source: "Single"
tags:
- programming/principle
---

> [!abstract]- Reference
> - [What Is Object-Oriented Programming? 4 Basic Concepts of OOP | Indeed.com](https://www.indeed.com/career-advice/career-development/what-is-object-oriented-programming)
> - [OOP 物件導向的四個特性 (coreychen71.github.io)](https://coreychen71.github.io/posts/2019-10/oop/)

# Encapsulation
> Forming a <mark style="background: #FF5582A6;">protective barrier</mark>

- Implement
	- `public`, `private`, and `protected` attribute
# Abstraction
> Treat a system like a <mark style="background: #FF5582A6;">black box</mark>

- Setting --> `attributes`, `methods`
- Isolate the impact of changes made to the code.
- change will only affect the implementation details of a class and not the outside code.
# Inheritance
> Classes can be organized into <mark style="background: #FF5582A6;">hierarchies</mark>
- 「被」繼承類別
	- `Base class`
	- `Parent class`
- 「主動」繼承類別
	- `Derived class`
	- `Child class`
# Polymorphism
> Calling code only needs to be <mark style="background: #FF5582A6;">written to handle objects</mark> from the root of the hierarchy

- Any object instantiated by any child class in the hierarchy will be handled in the same way
- `__len__` defined in class can be called by `len()` to handle the object