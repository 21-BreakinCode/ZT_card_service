---
source: System Design
tags:
- programming/systemDesign
---

> [!example]+ Reference
> - [system design topics](https://github.com/donnemartin/system-design-primer/blob/2d8231663fd0800720d25b9ac82dec3cda7e5a89/README.md#system-design-topics-start-here)
> - [CS75 (Summer 2012)-Scalability](https://www.youtube.com/watch?v=-W9F__D3oY4)
> - [Scalability Article](http://www.lecloud.net/tagged/scalability/chrono)

> [!info] Everything is a TRADE-OFF
# CS75
- Vertical scaling
	- Adding/Upgrading more **resources** to current working machine (CPU/RAM/DISK) 
	- Bottleneck - financial, real-world technology...
- Horizontal scaling
	- Adding **additional nodes** (multiple servers)
	- Can buy with cheaper hardware
- Caching
	- **Contribute to a disproportionate amount of load** on certain servers
		1. MySQL Query Cache
		2. memcached (RAM)
		3. ...
- Load balancing
	- **Allocate request** to the backend server, based on own different policy
		1. *Round-robin*: server1, server2, ... → server1, ...
			#### bottleneck
			- one of client may request heavy resources using
			- can't store the aggregate information
		2. *Software* (ELB, HAProxy, LVS...)
		3. *Hardware* (Barracuda, Cisco, Citrix, F5...)
- Database replication
	- **Automatic copy** of something: *Master-Slave*
	- Read replica - balance read request
	- active:active - two master
	- active:passive - one for standby when failure
- Database partitioning
	- split to different **cluster**
	- redundancy, balance load based on high level user info
	- *vertical partition*: split with column
	- *horizontal partition*: split with row
# Article
- Clones
	- **Same state of server**: every server contains exactly the same codebase & doesn't store any user-related data
	- **External database/persistent cache**: sessions need to be stored in a centralized data store which is accessible to all application servers
	- **Update**: snapshot current state and deploy new instances (e.g. AWS AMI)
- Database
	- **Denormalize**: 
		- *No more joins*, done in the application layer
		- Stay with MySQL, use like NoSQL
		- Use NoSQL(MongoDB, CouchDB...)
- Caches
	- **in-memory caches**
		- *key-value store*: Holds every dataset in RAM
		- Memcached, Redis
	- **Cached Databases Queries**
		- Store *query result* in cache
		- Problems:
			1. hard to *delete cached* result when it's complex query
			2. *data set changes*, need to delete all cache
	- **Cached Objects**
		- see *data as an object* (classes, instances, etc.)
		- make *asynchronous processing* possible
		- easily delete object whenever something did change
- Asynchronism
	- Solve the "pls wait for a while" situation
	- 2 Ways:
		1. **Pre-run**: doing time-consuming work in advance and serving the finished work
		2. **Parallel**: Run in parallel action, and wait for the done signal (e.g. *RabbitMQ*)

# High level trade-offs
- [[(System Design) - Ch2 Performance vs. Scalability]]
- [[(System Design) - Ch3 latency vs. throughput]]
- [[(System Design) - Ch4  availability vs. consistency]]