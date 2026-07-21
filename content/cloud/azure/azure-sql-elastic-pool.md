---
title: "[Solution] AZURE SQL Elastic Pool"
description: "SQLElasticPoolError for elastic pools."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SQL Elastic Pool` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Pool name taken
- Edtu limit reached
- All databases cannot fit

## How to Fix

### List pools

```bash
az sql elastic-pool list -g myRG -s myServer
```

## Examples

- Example scenario: pool name taken
- Example scenario: edtu limit reached
- Example scenario: all databases cannot fit

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
