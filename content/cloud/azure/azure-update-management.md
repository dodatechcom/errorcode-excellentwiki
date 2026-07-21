---
title: "[Solution] AZURE Update Management"
description: "UpdateMgmtError for update solutions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Update Management` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Solution not deployed
- Missing dependency agent
- Assessment failed for nodes

## How to Fix

### Check deployments

```bash
az automation software-update-configuration list
```

## Examples

- Example scenario: solution not deployed
- Example scenario: missing dependency agent
- Example scenario: assessment failed for nodes

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
