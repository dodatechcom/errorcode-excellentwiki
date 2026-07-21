---
title: "[Solution] AZURE Sync Group"
description: "SQLSyncGroupError for sync groups."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Sync Group` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Database sync group conflict
- Hub/member mismatch
- Conflict logging disabled

## How to Fix

### List sync groups

```bash
az sql db sync-group list -g myRG -s myServer -n myDb
```

## Examples

- Example scenario: database sync group conflict
- Example scenario: hub/member mismatch
- Example scenario: conflict logging disabled

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
