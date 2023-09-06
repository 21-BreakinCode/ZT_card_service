---
source: System Design
tags:
- programming/systemDesign
---
> [!example]+ Resource
> - [latency vs. throughput](https://github.com/donnemartin/system-design-primer/blob/2d8231663fd0800720d25b9ac82dec3cda7e5a89/README.md#latency-vs-throughput)
> - [Understanding Latency versus Throughput](https://community.cadence.com/cadence_blogs_8/b/fv/posts/understanding-latency-vs-throughput)

> Aim for **max throughput** with **acceptable latency**

- **Latency**: *time* to perform some action or some result
	→ 做一件事要多久

- **Throughput**: *number* of such actions per unit of time
	→ 單位時間內，那件事可以做幾次

Example:
- An assembly line is manufacturing cars. It takes eight hours to manufacture a car and that the factory produces one hundred and twenty cars per day.

	- The latency is: 8 hours.

	- The throughput is: 120 cars / day or 5 cars / hour.
