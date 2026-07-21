---
title: "[Solution] AZURE Durable Function"
description: "DurableFunctionError for orchestration."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Durable Function` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Orchestrator function not found
- Activity function failed
- Instance ID not found

## How to Fix

### Get status

```bash
az functionapp show -n myDFuncApp -g myRG
```

## Examples

- Example scenario: orchestrator function not found
- Example scenario: activity function failed
- Example scenario: instance id not found

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
