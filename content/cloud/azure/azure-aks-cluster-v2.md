---
title: "[Solution] AZURE AKS Cluster"
description: "AKSClusterError for AKS cluster."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `AKS Cluster` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Cluster already exists
- Region quota exhausted
- Service principal invalid

## How to Fix

### List clusters

```bash
az aks list
```

## Examples

- Example scenario: cluster already exists
- Example scenario: region quota exhausted
- Example scenario: service principal invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
