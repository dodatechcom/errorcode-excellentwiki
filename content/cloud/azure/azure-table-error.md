---
title: "[Solution] AZURE Table Error"
description: "TableError for storage tables."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Table Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Table name invalid
- Table already exists
- Throughput exceeded

## How to Fix

### List tables

```bash
az storage table list
```

## Examples

- Example scenario: table name invalid
- Example scenario: table already exists
- Example scenario: throughput exceeded

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
