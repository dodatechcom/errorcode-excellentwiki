---
title: "[Solution] AZURE vCore Limit"
description: "vCoreLimitExceeded for vCore."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `vCore Limit` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- vCore count hit limit
- Purchase model does not match

## How to Fix

### Scale up

```bash
az sql db update -g myRG -s myServer -n myDB --service-objective GP_Gen5_8
```

## Examples

- Example scenario: vcore count hit limit
- Example scenario: purchase model does not match

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
