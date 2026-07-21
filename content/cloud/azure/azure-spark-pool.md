---
title: "[Solution] AZURE Spark Pool"
description: "SparkPoolError for Apache Spark."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Spark Pool` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Pool not found
- Spark version mismatch
- Auto-scale settings invalid

## How to Fix

### List pools

```bash
az synapse spark pool list -g myRG -w myWS
```

## Examples

- Example scenario: pool not found
- Example scenario: spark version mismatch
- Example scenario: auto-scale settings invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
