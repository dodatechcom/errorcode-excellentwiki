---
title: "[Solution] AZURE Deployment Slot"
description: "DeploymentSlotError for slots."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Deployment Slot` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Slot name already exists
- Slot swap failed
- Slot settings mismatch

## How to Fix

### List slots

```bash
az webapp deployment slot list -g myRG -n myApp
```

## Examples

- Example scenario: slot name already exists
- Example scenario: slot swap failed
- Example scenario: slot settings mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
