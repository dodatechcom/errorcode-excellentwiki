---
title: "[Solution] AZURE Queue Storage Error"
description: "QueueStorageError for queues."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Queue Storage Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Message size > 64 KB
- Visibility timeout too long
- Queue metadata invalid

## How to Fix

### Add message

```bash
az storage message put --queue-name myQueue --content hello
```

## Examples

- Example scenario: message size > 64 kb
- Example scenario: visibility timeout too long
- Example scenario: queue metadata invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
