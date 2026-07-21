---
title: "[Solution] AZURE Workspace Retention"
description: "WorkspaceRetentionError for retention."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Workspace Retention` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Retention < 30 days (free tier)
- Archived logs not accessible
- Retention > 730 days needs trial

## How to Fix

### Update retention

```bash
az monitor log-analytics workspace update -g myRG -n myWorkspace --retention 90
```

## Examples

- Example scenario: retention < 30 days (free tier)
- Example scenario: archived logs not accessible
- Example scenario: retention > 730 days needs trial

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
