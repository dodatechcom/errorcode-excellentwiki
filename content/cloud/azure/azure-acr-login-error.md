---
title: "[Solution] Azure Container Registry Login Error"
description: "Fix Azure Container Registry authentication failures preventing image push and pull operations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

ACR login errors prevent developers and CI/CD pipelines from authenticating to the container registry. This blocks image push and pull operations.

## Common Causes

- Service principal credentials have expired or been revoked
- ACR admin user is disabled and no alternative authentication method is configured
- Managed identity does not have the AcrPull or AcrPush role
- Network rules block the connection from the client network

## How to Fix

### Login with admin credentials

```bash
az acr login --name myACR
```

### Enable admin user

```bash
az acr update --name myACR --admin-enabled true
```

### Assign AcrPush role to a service principal

```bash
az role assignment create \
  --assignee "appId" \
  --role "AcrPush" \
  --scope /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.ContainerRegistry/registries/myACR
```

### Create a service connection token

```bash
az acr credential show \
  --name myACR \
  --query "passwords[0].value"
```

## Examples

- Docker push fails with `unauthorized: authentication required` despite valid Azure CLI session
- ACR admin user is disabled and the service principal token has expired
- Managed identity can pull images but cannot push because it only has AcrPull role

## Related Errors

- [Azure Container Registry Error]({{< relref "/cloud/azure/azure-container-registry-error" >}}) -- General ACR errors.
- [Azure Managed Identity Error]({{< relref "/cloud/azure/azure-managed-identity-error" >}}) -- Identity issues.
