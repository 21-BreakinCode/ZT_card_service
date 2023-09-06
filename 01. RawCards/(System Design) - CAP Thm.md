---
source: System Design
tags:
- programming/systemDesign
---
- Brewer's thm
- For **distributed system** (collection of interconnected nodes that share data), you can *ONLY have 2* out of the following three guarantees across: 
	- **Consistency**
		- when read, return *most recent write*
	- **Availability**
		- non-failing node will return *non-error response*
	- **Partition Tolerance (P0) **
		- system will *continue to function* when network partitions occur
		- a MUST in distributed system
- Due to Partition Tolerance is must in distributed system:

| CP                                           | AP                       |
| -------------------------------------------- | ------------------------ |
| consistency model                            | availability model       |
| could return error                           | could return old version |
| *requirements*: atomic read and writes | *requirement*: allow for eventually consistency                         |
