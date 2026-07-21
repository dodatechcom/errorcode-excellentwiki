---
title: "[Solution] AZURE CSI Driver"
description: "CSIDriverError for storage drivers."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `CSI Driver` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Driver not installed
- Disk/File creation failed
- Volume attachment timeout

## How to Fix

### Check CSI pods

```bash
kubectl get pods -n kube-system | grep csi
```

## Examples

- Example scenario: driver not installed
- Example scenario: disk/file creation failed
- Example scenario: volume attachment timeout

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
