---
title: "[Solution] AZURE Failover Group"
description: "FailoverGroupError for failover groups."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Failover Group` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Group not found
- Failover already triggered
- Data loss warning required

## How to Fix

### List groups

```bash
az sql failover-group list -g myRG -s myServer
```

## Examples

- Example scenario: group not found
- Example scenario: failover already triggered
- Example scenario: data loss warning required

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
