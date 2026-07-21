---
title: "[Solution] AZURE Disk Attach"
description: "DiskAttachError when attaching a managed disk."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Disk Attach` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Disk already attached
- Disk in wrong region
- VM and disk zone mismatch

## How to Fix

### Attach disk

```bash
az vm disk attach -g myRG --vm-name myVM --disk myDisk
```

## Examples

- Example scenario: disk already attached
- Example scenario: disk in wrong region
- Example scenario: vm and disk zone mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
