---
title: "[Solution] AZURE Table Storage Error"
description: "TableStorageError for tables."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Table Storage Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Entity size > 1 MB
- Property count > 255
- Batch operation > 100 entities

## How to Fix

### Query table

```bash
az storage entity query -t myTable
```

## Examples

- Example scenario: entity size > 1 mb
- Example scenario: property count > 255
- Example scenario: batch operation > 100 entities

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
