---
title: "[Solution] AZURE Database Not Found"
description: "DatabaseNotFound for Azure SQL databases."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Database Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Database name incorrect
- Deleted
- Server paused

## How to Fix

### List databases

```bash
az sql db list -g myRG -s myServer
```

## Examples

- Example scenario: database name incorrect
- Example scenario: deleted
- Example scenario: server paused

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
