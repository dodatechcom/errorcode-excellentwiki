---
title: "[Solution] AZURE AKS Cluster Not Found"
description: "AKSNotFound for AKS clusters."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `AKS Cluster Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Cluster name incorrect
- Deleted by admin
- Subscription mismatch

## How to Fix

### List clusters

```bash
az aks list -g myRG
```

## Examples

- Example scenario: cluster name incorrect
- Example scenario: deleted by admin
- Example scenario: subscription mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
