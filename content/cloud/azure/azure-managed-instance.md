---
title: "[Solution] AZURE Managed Instance"
description: "ManagedInstanceError for SQL MI."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Managed Instance` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Instance name taken
- Subnet already in use
- VNet/subnet not delegated

## How to Fix

### List instances

```bash
az sql mi list -g myRG
```

## Examples

- Example scenario: instance name taken
- Example scenario: subnet already in use
- Example scenario: vnet/subnet not delegated

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
