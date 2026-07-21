---
title: "[Solution] AZURE Pipeline Failed"
description: "PipelineFailed for Azure Pipelines."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Pipeline Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Build definition not found
- Agent pool has no agents
- YAML syntax error

## How to Fix

### Run pipeline

```bash
az pipelines run --name myPipeline
```

## Examples

- Example scenario: build definition not found
- Example scenario: agent pool has no agents
- Example scenario: yaml syntax error

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
