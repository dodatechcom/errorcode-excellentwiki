---
title: "[Solution] Azure Container Registry Image Not Found"
description: "Fix Azure Container Registry image and tag not found errors during container deployments."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Image not found errors occur when the requested image or tag does not exist in the registry. This is common when tags are overwritten or images are not pushed correctly.

## Common Causes

- Image was pushed with a different tag or repository name
- Image was deleted by an retention policy or manual cleanup
- Multi-architecture image does not have the correct platform variant
- Image was pushed to a different ACR instance than expected

## How to Fix

### List repositories in ACR

```bash
az acr repository list --name myACR --query "[*]"
```

### List tags for a repository

```bash
az acr repository show-tags \
  --name myACR \
  --repository myrepo \
  --query "[*]"
```

### Search for image across repositories

```bash
az acr repository list --name myACR --query "[?contains(@,'myapp')]"
```

### Pull a specific tag

```bash
az acr repository show \
  --name myACR \
  --repository myrepo \
  --image myrepo:v1.0.0
```

## Examples

- AKS pod fails with `ImagePullBackOff` because the image tag `v2.0.0` was never pushed
- ACR retention policy deleted the `latest` tag and replaced it with a new build
- Image was pushed to `myACR2` but the deployment references `myACR`

## Related Errors

- [Azure Container Registry Error]({{< relref "/cloud/azure/azure-container-registry-error" >}}) -- General ACR errors.
- [Azure AKS Error]({{< relref "/cloud/azure/azure-aks-error" >}}) -- AKS deployment errors.
