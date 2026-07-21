---
title: "[Solution] AZURE Queue Error"
description: "QueueError for storage queues."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Queue Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Queue already exists
- Queue name invalid
- Metadata too large

## How to Fix

### List queues

```bash
az storage queue list
```

## Examples

- Example scenario: queue already exists
- Example scenario: queue name invalid
- Example scenario: metadata too large

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
