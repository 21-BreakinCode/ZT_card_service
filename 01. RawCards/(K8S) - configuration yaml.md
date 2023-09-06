---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
> [!abstract] YAML use case
> - To create ==objects== in k8s cluster

# Object types
> Ref: https://kubernetes.io/docs/concepts/overview/working-with-objects/

- Pod
- Deployment
- StatefulSet
- Service
- Ingress
- ConfigMap
- Secret
- Volumes


# YAML block
> [!example]+ Example
> ```yaml
> # api version block
> apiVersion: apps/v1
> 
> # object type block
> kind: Deployment
> 
> # metadat block
> metadata:
>   name: nginx-deployment
>   spec:
>     selector:
>         matchLabels:
>               app: nginx
> 	replicas: 2 
> 	template:
> 		metadata:
> 			labels:
> 				app: nginx
> 		spec:
> 			containers:
> 				- name: nginx
> 				  image: nginx:1.14.2
> 				  ports:
> 					- containerPort: 80
>```

- metadata
    - name
    - labels
	- specification → configuration about this deployment
	    - template: config file inside the config file → blueprint for a Pod
	    - selector

- namespace: Virtual (logically) cluster inside a cluster
> [!info] namespace in minikube
> - kube-system → system process, Mater & kubectl processes
> - kube-public → publicely accessible data, a configmap with cluster information
> - kube-node-lease → determines the availability of a node
> - default → resource you create are located here


- status → Desired vs. Actual(holds in etcd) ⇒ (self-healing feature of k8s)

- (Extra): apiVersion, kind