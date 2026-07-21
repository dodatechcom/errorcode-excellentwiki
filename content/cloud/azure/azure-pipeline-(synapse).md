---
title: "[Solution] AZURE Pipeline (Synapse)"
description: "SynapsePipelineError for pipelines."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Pipeline (Synapse)` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Activity validation failed
- Dataset not found
- Linked service broken

## How to Fix

### Create run

```bash
az synapse pipeline create-run -g myRG -w myWS -n myPipline
```

## Examples

- Example scenario: activity validation failed
- Example scenario: dataset not found
- Example scenario: linked service broken

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
