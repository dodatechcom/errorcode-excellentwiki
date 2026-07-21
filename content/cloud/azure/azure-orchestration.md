---
title: "[Solution] AZURE Orchestration"
description: "OrchestrationError for durable functions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Orchestration` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Max orchestration history exceeded
- Timed out waiting for activity
- Fan-out/fan-in error

## How to Fix

### Terminate instance

```bash
az rest --method post ...
```

## Examples

- Example scenario: max orchestration history exceeded
- Example scenario: timed out waiting for activity
- Example scenario: fan-out/fan-in error

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
