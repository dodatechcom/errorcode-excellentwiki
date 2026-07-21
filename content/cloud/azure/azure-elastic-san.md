---
title: "[Solution] AZURE Elastic SAN"
description: "ElasticSANError for SAN."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Elastic SAN` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Elastic SAN name taken
- Volume group limit (10) hit
- SKU not available in region

## How to Fix

### List SANs

```bash
az elastic-san list -g myRG
```

## Examples

- Example scenario: elastic san name taken
- Example scenario: volume group limit (10) hit
- Example scenario: sku not available in region

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
