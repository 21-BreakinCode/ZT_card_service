---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
 
> [!info] Reference 
> - [StatefulSets | Kubernetes](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
> - [[Kubernetes] StatefulSet Overview | 小信豬的原始部落 (godleon.github.io)](https://godleon.github.io/blog/Kubernetes/k8s-StatefulSets-Overview/)

---

> Provides the guarantees about the ==ordering and uniqueness== of these Pods

StatefulSets are valuable for applications that require one or more of the following.
- Stable, unique network identifiers.
- Stable, persistent storage.
- Ordered, graceful deployment and scaling.
- Ordered, automated rolling updates.

- Stateful app deployed using **StatefulSet(replicate Pods)**
    - ==Scaling DB application== → MASTER (Read and Write) & SLAVE (only Read)
    - ==Pod identity== → (statefulset name) - (ordinal)

---
## vs. Deployment
| Like                                                        | Unlike                                                          |
| ----------------------------------------------------------- | --------------------------------------------------------------- |
| Manages Pods that are based on an identical container spec. | StatefulSet maintains a sticky identity for each of their Pods. |
|                                                             | 刪除順序不一樣，StatefulSet 先刪 Pod                            |
