---
title: "[Solution] AZURE Elastic Pool"
description: "ElasticPoolError for elastic pools."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Elastic Pool` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Pool name already exists
- Pool storage limit reached
- DTU/vCore limit hit

## How to Fix

### List pools

```bash
az sql elastic-pool list -g myRG -s myServer
```

## Examples

- Example scenario: pool name already exists
- Example scenario: pool storage limit reached
- Example scenario: dtu/vcore limit hit

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
