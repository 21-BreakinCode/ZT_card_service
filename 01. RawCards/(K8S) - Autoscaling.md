---
source: container
tags:
  - programming/container
  - programming/systemDesign
---

# Horizontal Pod Autoscaler (HPA)

- scales the `number of replicas`
- monitors the CPU utilization or other metrics of the pod

# Vertical Pod Autoscaler (VPA)

- scales the `resources allocated` to the pod’s containers

# Cluster Autoscaling

- scales cluster based on node resource utilization
- ensure appropriate amount of resources are available to handle the workload while minimizing the cost