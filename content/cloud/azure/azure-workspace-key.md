---
title: "[Solution] AZURE Workspace Key"
description: "WorkspaceKeyError for workspace keys."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Workspace Key` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Key expired
- Primary key disabled
- Workspace not provisioned

## How to Fix

### Get keys

```bash
az monitor log-analytics workspace get-shared-keys -g myRG -n myWorkspace
```

## Examples

- Example scenario: key expired
- Example scenario: primary key disabled
- Example scenario: workspace not provisioned

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
