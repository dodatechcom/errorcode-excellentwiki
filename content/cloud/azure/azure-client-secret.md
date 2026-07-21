---
title: "[Solution] AZURE Client Secret"
description: "ClientSecretError for secrets."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Client Secret` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Secret expired
- Secret deleted
- Application not found

## How to Fix

### Add secret

```bash
az ad app credential reset --id app-id
```

## Examples

- Example scenario: secret expired
- Example scenario: secret deleted
- Example scenario: application not found

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
