---
title: "[Solution] AZURE Blob Tier Error"
description: "BlobTierError for access tiers."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Blob Tier Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Tier transition not allowed
- Account access tier conflict
- Archive rehydration delay

## How to Fix

### Set tier

```bash
az storage blob set-tier --container myContainer --name myBlob --tier Cool
```

## Examples

- Example scenario: tier transition not allowed
- Example scenario: account access tier conflict
- Example scenario: archive rehydration delay

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
