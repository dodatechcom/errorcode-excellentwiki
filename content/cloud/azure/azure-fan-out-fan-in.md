---
title: "[Solution] AZURE Fan-out/Fan-in"
description: "FanOutFanInError for parallel processing."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Fan-out/Fan-in` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Parallel task count exceeded
- Memory exhaustion in orchestrator
- Activity failed without retry

## How to Fix

### Check status

```bash
az functionapp show -n myFuncApp -g myRG
```

## Examples

- Example scenario: parallel task count exceeded
- Example scenario: memory exhaustion in orchestrator
- Example scenario: activity failed without retry

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
