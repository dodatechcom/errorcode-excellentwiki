---
title: "[Solution] AZURE AKS Node Pool"
description: "AKSNodePoolError for node pools."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `AKS Node Pool` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Node pool exists with same name
- VM size unavailable
- Node pool at capacity

## How to Fix

### List pools

```bash
az aks nodepool list --cluster myAKS -g myRG
```

## Examples

- Example scenario: node pool exists with same name
- Example scenario: vm size unavailable
- Example scenario: node pool at capacity

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
