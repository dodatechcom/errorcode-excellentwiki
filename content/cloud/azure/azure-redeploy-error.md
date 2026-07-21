---
title: "[Solution] AZURE Redeploy Error"
description: "RedeployFailed when VM redeployment fails."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Redeploy Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Azure host hardware issue
- Redeploy count quota reached
- Redeploy blocked by policy

## How to Fix

### Redeploy

```bash
az vm redeploy -n myVM -g myRG
```

## Examples

- Example scenario: azure host hardware issue
- Example scenario: redeploy count quota reached
- Example scenario: redeploy blocked by policy

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
