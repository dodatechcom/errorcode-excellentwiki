---
title: "[Solution] AZURE Login Failed"
description: "LoginFailed for SQL authentication."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Login Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Username/password wrong
- AAD auth not enabled
- IP not in firewall rules

## How to Fix

### Reset password

```bash
az sql server update -g myRG -n myServer --admin-password NewPass1
```

## Examples

- Example scenario: username/password wrong
- Example scenario: aad auth not enabled
- Example scenario: ip not in firewall rules

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
