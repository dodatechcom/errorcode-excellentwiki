---
title: "[Solution] AZURE PVC Not Bound"
description: "PVCNotBound for persistent volume claims."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `PVC Not Bound` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Storage class not found
- PV creation failed
- Available capacity issues

## How to Fix

### Get PVCs

```bash
kubectl get pvc
```

## Examples

- Example scenario: storage class not found
- Example scenario: pv creation failed
- Example scenario: available capacity issues

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
