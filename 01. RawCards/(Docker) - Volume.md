---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
- Storage can’t depend on the pod lifecycle
- Storage must be available by all nodes
- Can survive even if cluster crashes

### Persistent Volume (pv)
-   Like a cluster resource
-   created via YAML file
-   take storage from ==actual physical storage (local or cloud)==

### Persistent Volume Claim (pvc)
-   Created via YAML file
-   Claims a volume & Access mode
-   Also need to claim in pods configuration → mount into Pod

### Storage Class (sc)
-   Persistent volume ==dynamically==
-   Created via YAML file → via **“provision”** attribute