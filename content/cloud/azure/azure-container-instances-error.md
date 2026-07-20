---
title: "[Solution] Azure Container Instances Error — container group, restart, and log failures"
description: "Fix Azure Container Instances error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 111
---

Container Instances errors appear as failed container starts, OOMKilled restarts, or image pull failures when deploying containers to ACI.

## Common Causes
- Container image not accessible in registry or incorrect tag specified
- Insufficient CPU/memory allocation causing OOMKilled events
- Environment variables referencing non-existent Key Vault secrets
- Resource provider not registered for Microsoft.ContainerInstance
- Network profile misconfiguration blocking container internet access

## How to Fix
### Check container group status
```bash
az container list \
  --resource-group myResourceGroup \
  --query "[].{name:name, state:instanceView.currentState.state, restartCount:instanceView.restartCount}"
```

### View container logs
```bash
az container logs \
  --resource-group myResourceGroup \
  --name myContainerGroup \
  --container-name myContainer
```

### Redeploy with increased memory
```bash
az container create \
  --resource-group myResourceGroup \
  --name myContainerGroup \
  --image myregistry.azurecr.io/myimage:latest \
  --memory 4 \
  --cpu 2 \
  --registry-login-server myregistry.azurecr.io \
  --registry-username myuser \
  --registry-password mypassword
```

### Enable diagnostic logging
```bash
az container attach \
  --resource-group myResourceGroup \
  --name myContainerGroup \
  --container-name myContainer
```

## Examples
### Deploy container with Key Vault secrets
```bash
az container create \
  --resource-group myResourceGroup \
  --name myContainerGroup \
  --image myregistry.azurecr.io/myimage:latest \
  --secrets "dbpassword=SecretValue123" \
  --environment-variables "DB_PASSWORD=dbpassword"
```

### Update container environment variables
```bash
az container delete \
  --resource-group myResourceGroup \
  --name myContainerGroup --yes && \
az container create \
  --resource-group myResourceGroup \
  --name myContainerGroup \
  --image myregistry.azurecr.io/myimage:latest \
  --environment-variables "NEW_VAR=value"
```

## Related Errors
- {{< relref "/cloud/azure/azure-container-registry-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
- {{< relref "/cloud/azure/azure-vnet-error" >}}
