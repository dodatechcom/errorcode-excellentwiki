---
title: "[Solution] AZURE VMSS Scale"
description: "VMSSScaleError for Virtual Machine Scale Set."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VMSS Scale` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Capacity quota insufficient
- Orchestration mode conflict
- Scale set in single placement group

## How to Fix

### Check capacity

```bash
az vmss show -n myVMSS -g myRG
```

## Examples

- Example scenario: capacity quota insufficient
- Example scenario: orchestration mode conflict
- Example scenario: scale set in single placement group

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
