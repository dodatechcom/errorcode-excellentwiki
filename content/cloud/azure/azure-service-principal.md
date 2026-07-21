---
title: "[Solution] AZURE Service Principal"
description: "ServicePrincipalError for SPN."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Principal` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- SPN already exists
- Application not found
- Credential expiration

## How to Fix

### List SPNs

```bash
az ad sp list
```

## Examples

- Example scenario: spn already exists
- Example scenario: application not found
- Example scenario: credential expiration

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
