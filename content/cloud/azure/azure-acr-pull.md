---
title: "[Solution] AZURE ACR Pull"
description: "ACRPullError when pulling from ACR."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ACR Pull` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- ACR not in same login server
- Credentials expired
- Repository not found

## How to Fix

### Login ACR

```bash
az acr login -n myACR
```

## Examples

- Example scenario: acr not in same login server
- Example scenario: credentials expired
- Example scenario: repository not found

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
