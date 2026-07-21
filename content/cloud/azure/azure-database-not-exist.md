---
title: "[Solution] AZURE Database Not Exist"
description: "DatabaseNotFound for SQL database."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Database Not Exist` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Database name incorrect
- Deleted by admin
- Elastic pool mismatch

## How to Fix

### List databases

```bash
az sql db list --server myServer
```

## Examples

- Example scenario: database name incorrect
- Example scenario: deleted by admin
- Example scenario: elastic pool mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
