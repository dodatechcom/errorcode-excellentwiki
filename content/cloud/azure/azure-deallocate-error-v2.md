---
title: "[Solution] AZURE Deallocate Error"
description: "DeallocateError when deallocate fails."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Deallocate Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- VM with vTPM enabled limitations
- Reserved instance restriction
- Azure Policy blocks deallocation

## How to Fix

### Deallocate

```bash
az vm deallocate -n myVM -g myRG
```

## Examples

- Example scenario: vm with vtpm enabled limitations
- Example scenario: reserved instance restriction
- Example scenario: azure policy blocks deallocation

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
