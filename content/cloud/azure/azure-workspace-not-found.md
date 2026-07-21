---
title: "[Solution] AZURE Workspace Not Found"
description: "WorkspaceNotFound for Log Analytics."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Workspace Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Workspace name incorrect
- Deleted by admin
- Region mismatch

## How to Fix

### List workspaces

```bash
az monitor log-analytics workspace list -g myRG
```

## Examples

- Example scenario: workspace name incorrect
- Example scenario: deleted by admin
- Example scenario: region mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
