---
source: container
tags:
  - programming/container
  - programming/systemDesign
---

> [!info] Reference
> - [Service | Kubernetes](https://kubernetes.io/docs/concepts/services-networking/service/)
> - [Kubernetes Service 概念詳解 | Kubernetes (tachingchen.com)](https://tachingchen.com/tw/blog/kubernetes-service/)


- Route to cluster, load balancing
- permanent IP address
- ==Internal service==, loose coupling within & outside cluster

## Service type
### ClusterIP services
-   default service type
-   Identify via `selectors` in YAML file → key value pair
-   selector choose the `labels` of pod
-   `targetPort` must match the port that container is listening at

### Headless services
-   Communicate with a specific pod ⇒ not randomly select
-   Set YAML file **clusterIP to None** → (k8s will do DNS look up)

### LoadBalancer services → extension of NodePort
-   Becomes accessible externally through **cloud providers LoadBalancer**
-   Define in YAML file `type` attribute