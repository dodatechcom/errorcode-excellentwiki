---
title: "[Solution] AZURE SQL Auth Failure"
description: "SQLAuthFailure for authentication."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SQL Auth Failure` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Username/password wrong
- AAD auth not configured
- Managed identity missing

## How to Fix

### Set admin

```bash
az sql server ad-admin create -g myRG -s myServer --display-name admin --object-id ...
```

## Examples

- Example scenario: username/password wrong
- Example scenario: aad auth not configured
- Example scenario: managed identity missing

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
