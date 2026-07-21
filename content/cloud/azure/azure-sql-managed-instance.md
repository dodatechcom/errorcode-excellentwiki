---
title: "[Solution] AZURE SQL Managed Instance"
description: "ManagedInstanceError for SQL MI."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SQL Managed Instance` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Managed instance already exists
- Subnet already has MI
- VNet CIDR conflict

## How to Fix

### List MIs

```bash
az sql mi list -g myRG
```

## Examples

- Example scenario: managed instance already exists
- Example scenario: subnet already has mi
- Example scenario: vnet cidr conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
