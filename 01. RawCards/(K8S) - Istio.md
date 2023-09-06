---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
> Ref:
> - [Istio / The Istio service mesh](https://istio.io/latest/about/service-mesh/)
> - [Youtube Intro](https://youtu.be/16fgzklcF7Y)

---

### Features

- A [[(K8S) - Service Mesh | service mesh]]
- Service Discovery/Traffic management
- Metrics & Tracing/Observability
- Security

### Function

- traffic routing → Virtual service YAML
- which services can communicate
- traffic split
- retry rules → Destination Rule YAML



- Have a `Control Plane` to communicate each service with `Proxy(data plane)` inside each micro-services → 類似 SDN 架構
- Configuration `separate` from application configuration → k8s YAML file (CRD, CustomerResourceDefinitions)

