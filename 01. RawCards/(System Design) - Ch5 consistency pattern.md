---
source: System Design
tags:
- programming/systemDesign
---
> [!example]+ Resource
> - [consistency pattern](https://github.com/donnemartin/system-design-primer/blob/2d8231663fd0800720d25b9ac82dec3cda7e5a89/README.md#consistency-patterns)

- **Weak consistency**
	- After write, read *may or may not* see it
	- seen such as *memcached*
	- VoIP, video chat, and realtime multiplayer game
- **Eventual consistency**
	- After write, reads will *eventually* see it
	- data replicated asynchronously
	- DNS, email, and HA system
- **Strong consistency**
	- After write, reads *will see* it
	- data is replicated *synchronously*
	- RDBMSes