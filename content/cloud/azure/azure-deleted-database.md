---
title: "[Solution] AZURE Deleted Database"
description: "DeletedDatabaseError for dropped databases."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Deleted Database` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Database already dropped and purged
- Restore window expired (<7 days)

## How to Fix

### List deleted

```bash
az sql db list-deleted -g myRG -s myServer
```

## Examples

- Example scenario: database already dropped and purged
- Example scenario: restore window expired (<7 days)

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
