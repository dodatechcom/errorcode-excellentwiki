---
title: "[Solution] AZURE Geo Replication"
description: "SQLGeoReplicationError for geo-replication."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Geo Replication` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Secondary server not configured
- Seeding in progress
- Failover pending

## How to Fix

### List replicas

```bash
az sql db replica list -g myRG -s myServer -n myDb
```

## Examples

- Example scenario: secondary server not configured
- Example scenario: seeding in progress
- Example scenario: failover pending

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
