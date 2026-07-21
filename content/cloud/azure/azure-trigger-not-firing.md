---
title: "[Solution] AZURE Trigger Not Firing"
description: "TriggerNotFiring for functions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Trigger Not Firing` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Trigger binding config wrong
- Event source disconnected
- Blob/queue trigger not processed

## How to Fix

### Check logs

```bash
az functionapp log tail -n myFuncApp -g myRG
```

## Examples

- Example scenario: trigger binding config wrong
- Example scenario: event source disconnected
- Example scenario: blob/queue trigger not processed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
