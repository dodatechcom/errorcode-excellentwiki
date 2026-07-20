---
title: "[Solution] Azure Container Registry Error — push, pull, auth, and replication failures"
description: "Fix Azure Container Registry error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 112
---

Container Registry errors involve failed image pushes/pulls, authentication failures, or geo-replication sync issues that prevent container deployments.

## Common Causes
- ACR admin account disabled or RBAC permissions insufficient
- Firewall rules blocking access from developer machine or CI/CD agent
- Image tag already exists with immutable tag policy enforced
- Geo-replication not synced or target region capacity issues
- Token exchange failures with service connections

## How to Fix
### Check registry login status
```bash
az acr login --name myRegistry
```

### Enable admin account
```bash
az acr update \
  --resource-group myResourceGroup \
  --name myRegistry \
  --admin-enabled true
```

### Grant pull access to registry
```bash
az role assignment create \
  --assignee myServicePrincipal \
  --role AcrPull \
  --scope /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.ContainerRegistry/registries/myRegistry
```

### Check replication status
```bash
az acr replication list \
  --registry myRegistry \
  --query "[].{name:name, status:provisioningState, region:location}"
```

## Examples
### Push image to registry
```bash
az acr build \
  --registry myRegistry \
  --image myapp:v1.0 \
  --file Dockerfile .
```

### Import image from Docker Hub
```bash
az acr import \
  --name myRegistry \
  --source docker.io/library/nginx:latest \
  --image nginx:latest
```

## Related Errors
- {{< relref "/cloud/azure/azure-container-instances-error" >}}
- {{< relref "/cloud/azure/azure-aks-error" >}}
- {{< relref "/cloud/azure/auth-failed" >}}
