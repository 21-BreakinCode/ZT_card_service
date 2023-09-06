---
source: System Design
tags:
- programming/systemDesign
---
> [!example]+ Resource
> - [availability patterns](https://github.com/donnemartin/system-design-primer/blob/2d8231663fd0800720d25b9ac82dec3cda7e5a89/README.md#availability-patterns)

- Availability in numbers (3 9s, 4 9s...)
> quantified by uptime (or downtime) as a percentage of time the service is available.

| Duration  | 3'9s         | 4'9s        |
| --------- | ------------ | ----------- |
| per year  | 8h 45min 57s | 52min 35.7s |
| per month | 43m 49.7s    | 4m 23s      |
| per week  | 10m 4.8s     | 1m 5s       |
| per day   | 1m 26.4s     | 8.6s        | 

# Fail-over
> potential for loss of data if the active system fails before any newly written data can be replicated to the passive.


- **Active-passive**
	- master-slave failover
	- *heartbeats* send between active/passive server
	- *heartbeats is interrupted*, passive take over
	- downtime depends on: 
		- cold standby
		- hot standby
- **Active-Active**
	- master-master failover
	- all server spreading the load 
# Replication
- **Master-slave replication**
- **Master-master replication**