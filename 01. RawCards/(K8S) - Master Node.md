---
source: container
tags:
  - programming/container
  - programming/systemDesign
---

> [!info] Control cluster state and worker nodes
> - API Server, Scheduler, Controller manager, etcd
   
- API server
    - cluster gateway
    - authentication
- Scheduler
    - Decide `Node`/`Pod` schedule
    - execute by Kubelet
- Controller manager
    - detect **state** of clusters
- etcd
    - **key-value** of cluster ==state==