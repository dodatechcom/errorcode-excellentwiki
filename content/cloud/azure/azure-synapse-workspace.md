---
title: "[Solution] AZURE Synapse Workspace"
description: "SynapseWorkspaceError for workspaces."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Synapse Workspace` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Workspace name taken
- Data Lake Storage not linked
- SQL pool provisioning failed

## How to Fix

### List workspaces

```bash
az synapse workspace list -g myRG
```

## Examples

- Example scenario: workspace name taken
- Example scenario: data lake storage not linked
- Example scenario: sql pool provisioning failed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
