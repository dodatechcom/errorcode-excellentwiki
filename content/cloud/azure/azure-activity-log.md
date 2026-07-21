---
title: "[Solution] AZURE Activity Log"
description: "ActivityLogError for tenant activity."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Activity Log` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Category filter wrong
- Time range too large
- Tenant admin required

## How to Fix

### Query activity log

```bash
az monitor activity-log list --offset 7d
```

## Examples

- Example scenario: category filter wrong
- Example scenario: time range too large
- Example scenario: tenant admin required

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
