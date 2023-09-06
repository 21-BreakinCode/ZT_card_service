---
source: System Design
tags:
- programming/systemDesign
---
> [!example]+ Resource
> - [Availability vs. consistency](https://github.com/donnemartin/system-design-primer/blob/2d8231663fd0800720d25b9ac82dec3cda7e5a89/README.md#availability-vs-consistency)
> - [CAP Theorem: Revisited (robertgreiner.com)](https://robertgreiner.com/cap-theorem-revisited/)

- [[(System Design) - CAP Thm]]
- CP
	- consistency + partition tolerance
	- good for *atomic reads & writes*
- AP
	- availability + partition tolerance
	- allow *eventual consistency* 
	- system needs to *continue working despite external errors*