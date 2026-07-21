---
title: "[Solution] AZURE Geo-Replication"
description: "GeoReplicationError for geo-replication."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Geo-Replication` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Server not in paired region
- Already a secondary replica
- SKU mismatch

## How to Fix

### List replicas

```bash
az sql db list-replicas -g myRG -s myServer -n myDB
```

## Examples

- Example scenario: server not in paired region
- Example scenario: already a secondary replica
- Example scenario: sku mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
