---
title: "[Solution] AZURE SQL Pool (Synapse)"
description: "SQLPoolError for dedicated SQL pools."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SQL Pool (Synapse)` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Pool paused/not running
- DWU limit hit
- Restore point not found

## How to Fix

### Resume pool

```bash
az synapse sql pool resume -g myRG -w myWS -n myPool
```

## Examples

- Example scenario: pool paused/not running
- Example scenario: dwu limit hit
- Example scenario: restore point not found

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
