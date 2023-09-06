---
source: container
tags:
  - programming/container
  - programming/systemDesign
---
> Ref:
> 
> - [Helm | Installing Helm](https://helm.sh/docs/intro/install/)

---

#### 📝 Package manager for k8s, templating engine → to package YAML files

- Templating format ⇒ Reference to `values.yaml` file  
	→ {{ .Values.name }}  
    → {{ .Values.container.name }}  
    → {{ .Values.container.image }}

## Helm chart

> Bundle of YAML files

- Advantage ⇒ reuse the configuration that is already made up
    
- `helm search <keyword>`
    
- Helm Website: [Helm](https://helm.sh/)
    
- Hub Website: [Helm Hub](https://artifacthub.io/)
    
- Directory structure:
    
    - Chart.yaml → meta info about chart
    - values.yaml → values for template files
    - charts/ → char dependencies
    - templates/ → actual template files
