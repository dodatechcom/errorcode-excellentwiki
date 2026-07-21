---
title: "[Solution] AZURE Image Pull (AKS)"
description: "ImagePullError for AKS containers."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Image Pull (AKS)` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Image not in registry
- Pull secret missing
- Registry unreachable

## How to Fix

### Check pods

```bash
kubectl get pods
```

## Examples

- Example scenario: image not in registry
- Example scenario: pull secret missing
- Example scenario: registry unreachable

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
