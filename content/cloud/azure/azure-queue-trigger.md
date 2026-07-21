---
title: "[Solution] AZURE Queue Trigger"
description: "QueueTriggerError for queue triggers."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Queue Trigger` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Queue not found
- Queue message format invalid
- Poison message handling

## How to Fix

### Create queue

```bash
az storage queue create -n myqueue
```

## Examples

- Example scenario: queue not found
- Example scenario: queue message format invalid
- Example scenario: poison message handling

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
