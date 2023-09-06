---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
> Ref:
> - [Secrets | Kubernetes](https://kubernetes.io/docs/concepts/configuration/secret/)
> - [[Day 12] 敏感的資料怎麼存在k8s?! - Secrets - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天 (ithome.com.tw)](https://ithelp.ithome.com.tw/articles/10195094)
---
- External config like ConfigMap
- base64 encoded
- Store <mark style="background: #FF5582A6;">credential info</mark> (volume mount)
- can be managed using K8S RBAC