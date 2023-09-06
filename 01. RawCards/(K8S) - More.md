---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
# Deployment patterns

- CICD integrations
- [GitOps](https://www.youtube.com/watch?v=PFLimPh5-wo)
- [Helm Charts](https://helm.sh/docs/topics/)
- [Canary deployments explain](https://www.youtube.com/watch?v=sCevTD_GtvU) → 分流
- [Blue Green Deployments](https://developer.harness.io/docs/continuous-delivery/deploy-srv-diff-platforms/kubernetes/kubernetes-executions/create-a-kubernetes-blue-green-deployment/) → 有 rollout, rollback 機制
- [Rolling updates rollbacks](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment)

# Advanced topics

- [Custom controllers](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#custom-controllers) → mgmt of resources that aren’t support by k8s
    - [custom schedulers extenders](https://developer.ibm.com/articles/creating-a-custom-kube-scheduler/)
- [CRD](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)s: custom resource definitions