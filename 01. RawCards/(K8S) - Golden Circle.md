---
source: container
tags:
  - programming/container
  - programming/systemDesign
---

# Why

> [!info] 可以彈性化擴充不同功能之 container，並管理

- Trend of micro-services → Need a proper way to manage
- When you need to run many different containers with different images
- DB needs a volume to access → Volumes
- easy scalability, high resilience, application portability
- reduce complexity & workload for operation
- Service discovery & load balancing
- Storage orchestration
- automated rollouts & rollback
- bin packing → resource limitation
- self-healing
- secrets and configuration management

## Solution of: 

- High Availability → no downtime
- Scalability → high performance
- Disaster Recovery → backup and restore

# What

> [!info] Container orchestration tool ⇒ Manages Container applications
> - Kubernetes: open-source container orchestration platform
> - Applications mgmt: **scale**, **flexibility**, **portability**


## Architecture

- k8s Node → Individual machines that run containers
- Master Node → VMs with a set of programs to manage nodes (下指令地方)
- K8S cluster → A group of nodes，execute containers application
- k8s Development env setup
    - minikube cmd → CLI tool to manage VM itself
    - kubectl cmd → managing containers in the node, interact with Master

## Component (Objects)
- ==Pod==: 
	- k8s 最小單位，通常代表一個 container
- ==Service==: 
	- 對內固定 IP => 解決每當 rebuild Pod 都會有新的 IP 產生
- ==Ingress==: 
	- 對外接口 => 傳內部端口，讓外界可以連進來
- ==ConfigMap==: 
	- Key value pair
	- 儲存一些設定數據
- ==Secret==: 
	- Key value pair
	- 儲存重要隱私資訊
- ==Volumes==: 
	- 外接儲存空間
	- 解決 stateless container 無法存資料問題
- ==Deployment==:
	- 管理多種 Pods 的部署
	- FOR stateless service, 實現 HA 的管理部署
- ==StatefulSet==:
	- 管理多種 Pods 的部署
	- FOR stateful service, 實現 HA 的管理部署


# How
> [!example]- install k8s locally
> 1. `brew install minikube`
> 2. `minikube start --driver=docker`
> 3. `which minikube`
> 4. `minikube start`
> 5. `minikube status`
> 6. `kubectl cluster-info`

> [!info] 

## Cluster mgmt
- Cluster mgmt
    
> [!note] 💡 `namespace` - virtual cluster inside a cluster
> - kube-system → system process, Master & kubectl processes
> - kube-public → publicey accessible data, a configmap with cluster information
> - kube-node-lease → determines the availability of a node
> - default → resource you create are located here 


- Declarative state
    
- Network
    
- Storage