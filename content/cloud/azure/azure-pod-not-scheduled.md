---
title: "[Solution] AZURE Pod Not Scheduled"
description: "PodSchedulingError for AKS pods."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Pod Not Scheduled` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Insufficient CPU/memory
- PV node affinity mismatch
- Taint/toleration mismatch

## How to Fix

### Describe pod

```bash
kubectl describe pod myPod
```

## Examples

- Example scenario: insufficient cpu/memory
- Example scenario: pv node affinity mismatch
- Example scenario: taint/toleration mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
