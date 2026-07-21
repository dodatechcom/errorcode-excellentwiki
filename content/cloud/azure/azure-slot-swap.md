---
title: "[Solution] AZURE Slot Swap"
description: "SlotSwapError for swapping slots."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Slot Swap` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Swap in progress
- Warm-up request failing
- Slot setting difference conflict

## How to Fix

### Swap slots

```bash
az webapp deployment slot swap -g myRG -n myApp --slot staging --target prod
```

## Examples

- Example scenario: swap in progress
- Example scenario: warm-up request failing
- Example scenario: slot setting difference conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
