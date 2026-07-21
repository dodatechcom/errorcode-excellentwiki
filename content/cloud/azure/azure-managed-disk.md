---
title: "[Solution] AZURE Managed Disk"
description: "ManagedDiskError for managed disk operations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Managed Disk` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Disk size not supported
- Disk SKU not available in region
- Disk in creating state

## How to Fix

### List disks

```bash
az disk list -g myRG
```

## Examples

- Example scenario: disk size not supported
- Example scenario: disk sku not available in region
- Example scenario: disk in creating state

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
