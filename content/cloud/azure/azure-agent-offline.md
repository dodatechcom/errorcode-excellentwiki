---
title: "[Solution] AZURE Agent Offline"
description: "AgentOffline when no agents available."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Agent Offline` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Agents not running
- Deployment group offline
- VM agent unresponsive

## How to Fix

### Check agents

```bash
az pipelines agent list --pool-id 1
```

## Examples

- Example scenario: agents not running
- Example scenario: deployment group offline
- Example scenario: vm agent unresponsive

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
