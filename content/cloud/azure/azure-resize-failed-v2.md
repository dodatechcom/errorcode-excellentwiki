---
title: "[Solution] AZURE Resize Failed"
description: "ResizeDiskError when VM resize fails."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Resize Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Disk SKU not supported for target size
- VM is in a stopped state
- Ephemeral OS disk cannot be resized

## How to Fix

### Check size

```bash
az vm show -n myVM -g myRG --query hardwareProfile.vmSize
```

## Examples

- Example scenario: disk sku not supported for target size
- Example scenario: vm is in a stopped state
- Example scenario: ephemeral os disk cannot be resized

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
