---
title: "[Solution] AZURE VMSS Scale Set"
description: "ScaleSetError for VMSS operations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VMSS Scale Set` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Instance count exceeds max
- Upgrade policy prevented scale
- Fault domain count mismatch

## How to Fix

### Scale VMSS

```bash
az vmss scale -n myVMSS -g myRG --new-capacity 10
```

## Examples

- Example scenario: instance count exceeds max
- Example scenario: upgrade policy prevented scale
- Example scenario: fault domain count mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
