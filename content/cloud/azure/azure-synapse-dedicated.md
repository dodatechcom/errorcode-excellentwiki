---
title: "[Solution] AZURE Synapse Dedicated"
description: "SynapseDedicatedSQLError for dedicated pools."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Synapse Dedicated` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Dedicated pool paused/not active
- Scale in progress
- DWU limit reached

## How to Fix

### Resume pool

```bash
az synapse sql pool resume -n myPool --workspace myWS
```

## Examples

- Example scenario: dedicated pool paused/not active
- Example scenario: scale in progress
- Example scenario: dwu limit reached

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
