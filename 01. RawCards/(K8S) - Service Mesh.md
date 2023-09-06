---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
> [!info] Explain
> Manages `communication` between micro-services

- A solution to manage micro-services interact logic app
	- communication config logic → the config network for internal service
	- security logic → security for internal network (inside the cluster)
	- retry logic → rebuilding the app
	- metrics & tracing logic → for monitoring