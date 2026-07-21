---
title: "[Solution] AZURE GRS Failover"
description: "GRSFailoverError for geo-redundant failover."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GRS Failover` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Failover already in progress
- Account not GRS enabled
- Failover needs 24h cooling

## How to Fix

### Start failover

```bash
az storage account failover -g myRG -n myAccount
```

## Examples

- Example scenario: failover already in progress
- Example scenario: account not grs enabled
- Example scenario: failover needs 24h cooling

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
