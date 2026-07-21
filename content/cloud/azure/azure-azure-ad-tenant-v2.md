---
title: "[Solution] AZURE Azure AD Tenant"
description: "TenantError for Azure AD."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Azure AD Tenant` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Tenant not found
- Domain not verified
- Guest users not allowed

## How to Fix

### Show tenant

```bash
az account show --query tenantId
```

## Examples

- Example scenario: tenant not found
- Example scenario: domain not verified
- Example scenario: guest users not allowed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
