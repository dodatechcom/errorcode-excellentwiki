---
title: "[Solution] AZURE Hybrid Worker"
description: "HybridWorkerError for hybrid workers."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Hybrid Worker` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Worker not registered
- Worker offline
- Extension version outdated

## How to Fix

### List workers

```bash
az automation hybrid-worker-group list -g myRG -a myAccount
```

## Examples

- Example scenario: worker not registered
- Example scenario: worker offline
- Example scenario: extension version outdated

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
