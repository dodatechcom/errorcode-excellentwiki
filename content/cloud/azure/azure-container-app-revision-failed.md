---
title: "[Solution] Azure Container Apps Revision Failed"
description: "Fix Azure Container Apps revision creation failures that prevent application deployments."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Revision failures occur when Azure Container Apps cannot create or activate a new revision. This prevents new code versions from being deployed.

## Common Causes

- Container image is not accessible from the Container Apps environment
- Resource limits on the revision are too low for the application
- Environment vNet configuration blocks the container registry
- Active revision count has reached the maximum allowed limit

## How to Fix

### Check revision status

```bash
az containerapp revision list \
  --name myApp \
  --resource-group myRG \
  --query "[].{Name:name,State:properties.provisioningState,Active:properties.active}"
```

### Create a new revision

```bash
az containerapp update \
  --name myApp \
  --resource-group myRG \
  --image myregistry.azurecr.io/myapp:v2
```

### Set a revision as active

```bash
az containerapp revision activate \
  --name myApp \
  --resource-group myRG \
  --revision myApp--v2
```

### Check environment configuration

```bash
az containerapp env show \
  --name myEnv \
  --resource-group myRG \
  --query "properties.vnetConfiguration"
```

## Examples

- New revision fails to create because the image tag does not exist in ACR
- Revision deployment times out because the container needs more than 2 vCPUs
- All revisions are inactive and traffic is not routed to any version

## Related Errors

- [Azure Container App Not Found]({{< relref "/cloud/azure/azure-container-app-not-found" >}}) -- Missing app.
- [Azure Container Registry Error]({{< relref "/cloud/azure/azure-container-registry-error" >}}) -- ACR issues.
