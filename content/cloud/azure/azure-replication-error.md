---
title: "[Solution] AZURE Replication Error"
description: "ReplicationError for storage replication."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Replication Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- GRS failover in progress
- LRS to GRS change delayed
- Source/destination sync lag

## How to Fix

### Check replication

```bash
az storage account show -g myRG -n myAccount --query replicationType
```

## Examples

- Example scenario: grs failover in progress
- Example scenario: lrs to grs change delayed
- Example scenario: source/destination sync lag

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
