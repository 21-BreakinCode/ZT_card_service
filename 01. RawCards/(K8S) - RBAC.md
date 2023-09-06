---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
### RBAC

> [!info] Based on roles assigned to users or groups to access k8s resource

- Reference: [Understand Role Based Access Control in Kubernetes](https://youtu.be/G3R24JSlGjY)

- creating & binding roles assigned to users or groups
- Implementing by → RESTful, namespace, cluster…
    - RESTful
        - verb: `get`, `list`, ...
        - nouns: `pods`, `volumes`, …
    - namespace to assign resource and privilege
    - cluster to limit nodes