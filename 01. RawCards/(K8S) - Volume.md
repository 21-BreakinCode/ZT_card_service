---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
> [!info] Reference
> - [Tech World NaNa](https://youtu.be/0swOh5C3OVM)

## Volume

- a directory accessible to containers running `within a Pod`
- Defined in `Pod level` (Pod yaml specification)

## PV - Persistent Volume

- `piece of storage` in k8s “cluster” provisioned by administrator
- once create can by bound to a `PVC - persitent volume claim` for pod to reference
- Defined at `cluster level`

## PVC - Persistent Volume Claim

- `interface` between pods and PVs - `a request for storage` made by user or application
- a claim to a specific amount and type of storage in the cluster
- defined in the `namespace`

