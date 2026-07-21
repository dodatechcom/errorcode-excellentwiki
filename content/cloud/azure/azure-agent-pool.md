---
title: "[Solution] AZURE Agent Pool"
description: "AgentPoolError for agent pools."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Agent Pool` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Pool not found
- All agents offline
- Agent capacity exhausted

## How to Fix

### List pools

```bash
az pipelines pool list
```

## Examples

- Example scenario: pool not found
- Example scenario: all agents offline
- Example scenario: agent capacity exhausted

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
