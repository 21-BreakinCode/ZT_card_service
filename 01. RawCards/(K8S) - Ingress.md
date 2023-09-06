---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
> Ref: 
> - [Ingress | Kubernetes](https://kubernetes.io/docs/concepts/services-networking/ingress/)
> - [Kubernetes 那些事 — Ingress 篇（一）. 前言 | by Andy Chen | Andy的技術分享blog | Medium](https://medium.com/andy-blog/kubernetes-%E9%82%A3%E4%BA%9B%E4%BA%8B-ingress-%E7%AF%87-%E4%B8%80-92944d4bf97d)


> [!abstract] Route to cluster
> 為了不要讓traffic直接進入內部服務 ⇒ 先藉由 ingress 再進入內部服務

- `Object kind` ⇒ Ingress
    - A good security practice

- YAML file “spec” part ⇒ Routing rules
    - tls → certificate of `https://`
    - rules
    - host → domain address (Valid domain name address)
    - path → the URL path to route to backend service
    - backends
        - serviceName
        - servicePort

- _**Ingress Controller**_ → implementation for ingress (Third party information)